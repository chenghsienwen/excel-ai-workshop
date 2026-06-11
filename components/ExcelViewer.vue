<script setup lang="ts">
import { ref, computed, onMounted, onBeforeUnmount, nextTick } from 'vue'
import * as XLSX from 'xlsx'

const props = defineProps<{
  path: string
  sheet?: string | number
  defaultZoom?: number
}>()

const xlsxFiles = import.meta.glob('/app/**/*.xlsx', { query: '?url', import: 'default', eager: true })

const tableHtml = ref('')
const sheetNames = ref<string[]>([])
const activeSheet = ref('')
const loading = ref(true)
const error = ref('')
const zoom = ref(props.defaultZoom ?? 1)

const filename = computed(() => props.path.split('/').pop() ?? props.path)
const zoomLabel = computed(() => `${Math.round(zoom.value * 100)}%`)

function zoomIn()    { zoom.value = Math.min(3, parseFloat((zoom.value + 0.1).toFixed(1))) }
function zoomOut()   { zoom.value = Math.max(0.3, parseFloat((zoom.value - 0.1).toFixed(1))) }
function zoomReset() { zoom.value = 1 }

let workbook: XLSX.WorkBook | null = null

// ── cell tagging ──────────────────────────────────────────────────────────
// Synchronous — callers must ensure scrollEl is in the DOM before calling.
function tagCells() {
  scrollEl.value?.querySelectorAll('tr').forEach((tr, rIdx) => {
    tr.querySelectorAll('td, th').forEach((td, cIdx) => {
      ;(td as HTMLElement).dataset.row = String(rIdx)
      ;(td as HTMLElement).dataset.col = String(cIdx)
    })
  })
}

// ── cell highlight ────────────────────────────────────────────────────────
const selStart = ref<{ r: number; c: number } | null>(null)
const selEnd   = ref<{ r: number; c: number } | null>(null)
const isSelecting = ref(false)

const hasHighlight = computed(() => selStart.value !== null)
const highlightLabel = computed(() => {
  if (!selStart.value || !selEnd.value) return ''
  const rows = Math.abs(selEnd.value.r - selStart.value.r) + 1
  const cols = Math.abs(selEnd.value.c - selStart.value.c) + 1
  return `${rows}×${cols}`
})

function applyHighlight() {
  if (!selStart.value || !selEnd.value) return
  const r1 = Math.min(selStart.value.r, selEnd.value.r)
  const r2 = Math.max(selStart.value.r, selEnd.value.r)
  const c1 = Math.min(selStart.value.c, selEnd.value.c)
  const c2 = Math.max(selStart.value.c, selEnd.value.c)
  scrollEl.value?.querySelectorAll('[data-row]').forEach(cell => {
    const r = parseInt((cell as HTMLElement).dataset.row ?? '0')
    const c = parseInt((cell as HTMLElement).dataset.col ?? '0')
    cell.classList.toggle('ev-cell--highlight', r >= r1 && r <= r2 && c >= c1 && c <= c2)
  })
}

function clearHighlight() {
  scrollEl.value?.querySelectorAll('.ev-cell--highlight').forEach(cell =>
    cell.classList.remove('ev-cell--highlight')
  )
  selStart.value = null
  selEnd.value   = null
}

function renderSheet(name: string) {
  if (!workbook) return
  clearHighlight()
  tableHtml.value = XLSX.utils.sheet_to_html(workbook.Sheets[name])
  activeSheet.value = name
  // scrollEl already in DOM when switching sheets; wait for v-html to re-render
  nextTick(tagCells)
}

onMounted(async () => {
  try {
    const key = props.path.startsWith('/') ? props.path : `/${props.path}`
    const url = xlsxFiles[key] as string
    let buf: ArrayBuffer
    if (url) {
      buf = await (await fetch(url)).arrayBuffer()
    } else {
      const base = (import.meta.env.BASE_URL ?? '/').replace(/\/$/, '')
      const publicUrl = base + key.replace(/^\/public/, '')
      const res = await fetch(publicUrl)
      if (!res.ok) { error.value = `File not found: ${key}`; loading.value = false; return }
      buf = await res.arrayBuffer()
    }
    workbook = XLSX.read(buf, { type: 'array' })
    sheetNames.value = workbook.SheetNames
    const target = typeof props.sheet === 'number'
      ? workbook.SheetNames[props.sheet]
      : (props.sheet ?? workbook.SheetNames[0])
    renderSheet(target)
  } catch (e) {
    error.value = String(e)
  } finally {
    loading.value = false
    // Wait for v-else scrollEl to mount, then tag cells for selection
    await nextTick()
    tagCells()
  }
})

// ── height clamping (same pattern as ChatWindow) ──────────────────────────
const rootEl   = ref<HTMLElement | null>(null)
const scrollEl = ref<HTMLElement | null>(null)

function offsetTopFrom(el: HTMLElement, ancestor: HTMLElement) {
  let top = 0, cur: HTMLElement | null = el
  while (cur && cur !== ancestor) { top += cur.offsetTop; cur = cur.offsetParent as HTMLElement }
  return top
}

function clampToSlide() {
  if (!rootEl.value) return
  const slide = rootEl.value.closest('.slidev-layout') as HTMLElement | null
  if (!slide) return
  const maxH = slide.offsetHeight - offsetTopFrom(rootEl.value, slide) - 24
  rootEl.value.style.maxHeight = maxH > 60 ? `${maxH}px` : ''
}

let ro: ResizeObserver
onMounted(() => {
  clampToSlide()
  ro = new ResizeObserver(clampToSlide)
  const slide = rootEl.value?.closest('.slidev-layout')
  if (slide) ro.observe(slide)
})
onBeforeUnmount(() => ro?.disconnect())

// ── drag-to-pan & cell selection ──────────────────────────────────────────
const isDragging = ref(false)
let dragStart = { x: 0, y: 0, sl: 0, st: 0 }

function onMouseDown(e: MouseEvent) {
  const cell = (e.target as HTMLElement).closest('td, th') as HTMLElement | null
  if (cell) {
    isSelecting.value = true
    isDragging.value  = false
    const r = parseInt(cell.dataset.row ?? '0')
    const c = parseInt(cell.dataset.col ?? '0')
    selStart.value = { r, c }
    selEnd.value   = { r, c }
    applyHighlight()
    e.preventDefault()
  } else {
    if (!scrollEl.value) return
    isDragging.value  = true
    isSelecting.value = false
    dragStart = { x: e.clientX, y: e.clientY, sl: scrollEl.value.scrollLeft, st: scrollEl.value.scrollTop }
    e.preventDefault()
  }
}

function onMouseMove(e: MouseEvent) {
  if (isSelecting.value) {
    const cell = (e.target as HTMLElement).closest('td, th') as HTMLElement | null
    if (!cell) return
    const r = parseInt(cell.dataset.row ?? '0')
    const c = parseInt(cell.dataset.col ?? '0')
    if (selEnd.value?.r === r && selEnd.value?.c === c) return
    selEnd.value = { r, c }
    applyHighlight()
  } else if (isDragging.value && scrollEl.value) {
    scrollEl.value.scrollLeft = dragStart.sl - (e.clientX - dragStart.x)
    scrollEl.value.scrollTop  = dragStart.st - (e.clientY - dragStart.y)
  }
}

function onMouseUp() {
  isDragging.value  = false
  isSelecting.value = false
}
</script>

<template>
  <div ref="rootEl" class="ev-window">
    <!-- title bar -->
    <div class="ev-window__bar">
      <div class="ev-window__dots">
        <span /><span /><span />
      </div>
      <div class="ev-window__title">{{ filename }}</div>
      <transition name="ev-fade">
        <div v-if="hasHighlight" class="ev-highlight-badge" @click="clearHighlight">
          <span class="ev-highlight-badge__label">{{ highlightLabel }}</span>
          <span class="ev-highlight-badge__clear">✕</span>
        </div>
      </transition>
      <div class="ev-zoom">
        <button class="ev-zoom__btn" @click="zoomOut">−</button>
        <span class="ev-zoom__label" @click="zoomReset">{{ zoomLabel }}</span>
        <button class="ev-zoom__btn" @click="zoomIn">+</button>
      </div>
    </div>

    <!-- sheet tabs -->
    <div v-if="!loading && !error && sheetNames.length > 1" class="ev-window__tabs">
      <button
        v-for="name in sheetNames"
        :key="name"
        class="ev-window__tab"
        :class="{ 'ev-window__tab--active': name === activeSheet }"
        @click="renderSheet(name)"
      >{{ name }}</button>
    </div>

    <!-- body -->
    <div v-if="loading" class="ev-window__status">Loading…</div>
    <div v-else-if="error" class="ev-window__status ev-window__status--error">{{ error }}</div>
    <div
      v-else
      ref="scrollEl"
      class="ev-window__scroll"
      :class="{ 'ev-window__scroll--dragging': isDragging }"
      @mousedown="onMouseDown"
      @mousemove="onMouseMove"
      @mouseup="onMouseUp"
      @mouseleave="onMouseUp"
    >
      <div :style="{ zoom }" v-html="tableHtml" />
    </div>
  </div>
</template>

<style scoped>
.ev-window {
  display: flex;
  flex-direction: column;
  border: 1px solid #444;
  border-radius: 8px;
  overflow: hidden;
  background: #1a1a1a;
  margin-top: 0.75rem;
  font-family: monospace;
}

/* ── title bar ── */
.ev-window__bar {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.45rem 0.9rem;
  background: #2d2d2d;
  border-bottom: 1px solid #444;
  flex-shrink: 0;
}
.ev-window__dots {
  display: flex;
  gap: 0.35rem;
  flex-shrink: 0;
}
.ev-window__dots span {
  width: 0.65rem;
  height: 0.65rem;
  border-radius: 50%;
}
.ev-window__dots span:nth-child(1) { background: #ff5f57; }
.ev-window__dots span:nth-child(2) { background: #febc2e; }
.ev-window__dots span:nth-child(3) { background: #28c840; }
.ev-window__title {
  font-size: 0.72rem;
  color: #aaa;
  flex: 1;
  text-align: center;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* ── highlight badge ── */
.ev-highlight-badge {
  display: flex;
  align-items: center;
  gap: 0.3rem;
  padding: 0.1rem 0.45rem;
  border-radius: 3px;
  border: 1px solid rgba(255, 153, 102, 0.5);
  background: rgba(255, 153, 102, 0.12);
  cursor: pointer;
  flex-shrink: 0;
}
.ev-highlight-badge:hover {
  background: rgba(255, 153, 102, 0.22);
  border-color: rgba(255, 153, 102, 0.8);
}
.ev-highlight-badge__label {
  font-size: 0.6rem;
  color: #ff9966;
  font-family: monospace;
}
.ev-highlight-badge__clear {
  font-size: 0.55rem;
  color: rgba(255, 153, 102, 0.7);
}
.ev-fade-enter-active,
.ev-fade-leave-active { transition: opacity 0.15s; }
.ev-fade-enter-from,
.ev-fade-leave-to    { opacity: 0; }

/* ── zoom controls ── */
.ev-zoom {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  flex-shrink: 0;
}
.ev-zoom__btn {
  width: 1.3rem;
  height: 1.3rem;
  border: 1px solid #555;
  border-radius: 3px;
  background: #3a3a3a;
  color: #ccc;
  font-size: 0.85rem;
  line-height: 1;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
}
.ev-zoom__btn:hover { background: #555; color: #fff; }
.ev-zoom__label {
  font-size: 0.65rem;
  color: #aaa;
  min-width: 2.4rem;
  text-align: center;
  cursor: pointer;
  user-select: none;
}
.ev-zoom__label:hover { color: #fff; }

/* ── sheet tabs ── */
.ev-window__tabs {
  display: flex;
  gap: 0.3rem;
  padding: 0.3rem 0.6rem;
  background: #222;
  border-bottom: 1px solid #444;
  flex-shrink: 0;
}
.ev-window__tab {
  font-size: 0.68rem;
  padding: 0.15rem 0.6rem;
  border-radius: 3px;
  border: 1px solid #555;
  background: transparent;
  color: #aaa;
  cursor: pointer;
  font-family: monospace;
}
.ev-window__tab--active { background: #3a3a3a; color: #fff; border-color: #777; }

/* ── scrollable body ── */
.ev-window__scroll {
  flex: 1;
  min-height: 0;
  overflow: scroll;
  cursor: grab;
  user-select: none;
}
.ev-window__scroll--dragging {
  cursor: grabbing;
}
.ev-window__scroll::-webkit-scrollbar         { width: 10px; height: 10px; }
.ev-window__scroll::-webkit-scrollbar-track   { background: #111; }
.ev-window__scroll::-webkit-scrollbar-thumb   { background: #555; border-radius: 4px; border: 2px solid #111; }
.ev-window__scroll::-webkit-scrollbar-thumb:hover { background: #777; }
.ev-window__scroll::-webkit-scrollbar-corner  { background: #111; }

.ev-window__status { padding: 1rem; font-size: 0.85rem; color: #888; }
.ev-window__status--error { color: #f87171; }

/* ── table ── */
.ev-window__scroll :deep(table) {
  border-collapse: collapse;
  font-size: 0.68rem;
  color: #d4d5da;
  white-space: nowrap;
}
.ev-window__scroll :deep(td),
.ev-window__scroll :deep(th) {
  border: 1px solid #333;
  padding: 0.18rem 0.55rem;
  text-align: left;
  cursor: cell;
}
.ev-window__scroll :deep(tr:first-child td) {
  background: #2d2d2d;
  color: #fff;
  font-weight: 600;
  position: sticky;
  top: 0;
  z-index: 1;
}
.ev-window__scroll :deep(tr:nth-child(even)) { background: #1e1e1e; }
.ev-window__scroll :deep(tr:nth-child(odd))  { background: #181818; }

/* ── cell highlight (same orange as cards default) ── */
.ev-window__scroll :deep(.ev-cell--highlight) {
  background: rgba(255, 153, 102, 0.18) !important;
  outline: 1px solid rgba(255, 153, 102, 0.55);
  outline-offset: -1px;
}
</style>
