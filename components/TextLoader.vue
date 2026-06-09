<script setup lang="ts">
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'

const props = defineProps<{
  path: string
}>()

const mdFiles = import.meta.glob('/app/**/*.md', { query: '?raw', import: 'default', eager: true })

const content = ref('')
const loading = ref(true)
const error = ref('')

const filename = computed(() => props.path.split('/').pop() ?? props.path)

onMounted(async () => {
  try {
    const key = props.path.startsWith('/') ? props.path : `/${props.path}`
    const raw = mdFiles[key] as string | undefined
    if (raw != null) {
      content.value = raw
    } else {
      // Fall back to public asset with BASE_URL for GitHub Pages
      const base = (import.meta.env.BASE_URL ?? '/').replace(/\/$/, '')
      const publicUrl = base + key.replace(/^\/public/, '')
      const res = await fetch(publicUrl)
      if (!res.ok) { error.value = `File not found: ${key}`; loading.value = false; return }
      content.value = await res.text()
    }
  } catch (e) {
    error.value = String(e)
  } finally {
    loading.value = false
  }
})

// ── height clamping ───────────────────────────────────────────────────────
const rootEl = ref<HTMLElement | null>(null)

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
</script>

<template>
  <div ref="rootEl" class="tl-window">
    <!-- title bar -->
    <div class="tl-window__bar">
      <div class="tl-window__dots">
        <span /><span /><span />
      </div>
      <div class="tl-window__title">{{ filename }}</div>
    </div>

    <!-- body -->
    <div v-if="loading" class="tl-window__status">Loading…</div>
    <div v-else-if="error" class="tl-window__status tl-window__status--error">{{ error }}</div>
    <pre v-else class="tl-window__content">{{ content }}</pre>
  </div>
</template>

<style scoped>
.tl-window {
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
.tl-window__bar {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.45rem 0.9rem;
  background: #2d2d2d;
  border-bottom: 1px solid #444;
  flex-shrink: 0;
}
.tl-window__dots {
  display: flex;
  gap: 0.35rem;
  flex-shrink: 0;
}
.tl-window__dots span {
  width: 0.65rem;
  height: 0.65rem;
  border-radius: 50%;
}
.tl-window__dots span:nth-child(1) { background: #ff5f57; }
.tl-window__dots span:nth-child(2) { background: #febc2e; }
.tl-window__dots span:nth-child(3) { background: #28c840; }
.tl-window__title {
  font-size: 0.72rem;
  color: #aaa;
  flex: 1;
  text-align: center;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* ── status ── */
.tl-window__status { padding: 1rem; font-size: 0.85rem; color: #888; }
.tl-window__status--error { color: #f87171; }

/* ── scrollable plain text ── */
.tl-window__content {
  flex: 1;
  min-height: 0;
  overflow-y: auto;
  margin: 0;
  padding: 0.75rem 1rem;
  font-size: 0.68rem;
  line-height: 1.6;
  color: #d4d5da;
  white-space: pre-wrap;
  word-break: break-word;
}
.tl-window__content::-webkit-scrollbar         { width: 10px; }
.tl-window__content::-webkit-scrollbar-track   { background: #111; }
.tl-window__content::-webkit-scrollbar-thumb   { background: #555; border-radius: 4px; border: 2px solid #111; }
.tl-window__content::-webkit-scrollbar-thumb:hover { background: #777; }
</style>
