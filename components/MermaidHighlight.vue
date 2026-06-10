<script setup>
import { computed, inject, onMounted, onUnmounted } from 'vue'
import lz from 'lz-string'

const props = defineProps({
  diagram: { type: String, required: true },
  color: { type: String, default: '#f96' },
})

// Extract unique node IDs in declaration order.
// Matches flowchart node shapes: A[...], A(...), A{...}, A((...)
const KEYWORDS = new Set([
  'flowchart', 'graph', 'subgraph', 'end', 'style', 'classDef',
  'class', 'click', 'LR', 'RL', 'TD', 'TB', 'BT',
])

const nodes = computed(() => {
  const seen = new Set()
  const result = []
  for (const [, id] of props.diagram.matchAll(/\b([A-Za-z_][A-Za-z0-9_]*)\s*[\[({>]/g)) {
    if (!KEYWORDS.has(id) && !seen.has(id)) {
      seen.add(id)
      result.push(id)
    }
  }
  return result
})

// Inject Slidev's per-slide clicks context and register N click steps so
// the slide nav knows how many clicks to consume before advancing.
const clicksCtxRef = inject('$$slidev-clicks-context')
const KEY = {}

onMounted(() => {
  const ctx = clicksCtxRef?.value
  if (!ctx) return
  const n = nodes.value.length
  ctx.register(KEY, { delta: n, max: n })
})

onUnmounted(() => {
  clicksCtxRef?.value?.unregister(KEY)
})

const codeLz = computed(() => {
  // ctx.current reads the underlying reactive ref, so this computed is live.
  const idx = clicksCtxRef?.value?.current ?? 0
  const highlighted = nodes.value[idx - 1]
  const code = highlighted
    ? `${props.diagram}\n    style ${highlighted} fill:${props.color},color:#000`
    : props.diagram
  return lz.compressToBase64(code)
})
</script>

<template>
  <Mermaid :code-lz="codeLz" />
</template>
