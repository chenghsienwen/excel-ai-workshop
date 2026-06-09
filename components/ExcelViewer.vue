<script setup lang="ts">
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'
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

function renderSheet(name: string) {
  if (!workbook) return
  tableHtml.value = XLSX.utils.sheet_to_html(workbook.Sheets[name])
  activeSheet.value = name
}

onMounted(async () => {
  try {
    const key = props.path.startsWith('/') ? props.path : `/${props.path}`
    const url = xlsxFiles[key] as string
    let buf: ArrayBuffer
    if (url) {
      buf = await (await fetch(url)).arrayBuffer()
    } else {
      // Fall back to public asset; prepend BASE_URL so GitHub Pages subpath works
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

// ── drag-to-pan ───────────────────────────────────────────────────────────
const isDragging = ref(false)
let dragStart = { x: 0, y: 0, sl: 0, st: 0 }

function onMouseDown(e: MouseEvent) {
  if (!scrollEl.value) return
  isDragging.value = true
  dragStart = { x: e.clientX, y: e.clientY, sl: scrollEl.value.scrollLeft, st: scrollEl.value.scrollTop }
  e.preventDefault()
}

function onMouseMove(e: MouseEvent) {
  if (!isDragging.value || !scrollEl.value) return
  scrollEl.value.scrollLeft = dragStart.sl - (e.clientX - dragStart.x)
  scrollEl.value.scrollTop  = dragStart.st - (e.clientY - dragStart.y)
}

function onMouseUp() { isDragging.value = false }

</script>

<template>
  <div ref="rootEl" class="ev-window">
    <!-- title bar -->
    <div class="ev-window__bar">
      <div class="ev-window__dots">
        <span /><span /><span />
      </div>
      <div class="ev-window__title">{{ filename }}</div>
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
</style>
