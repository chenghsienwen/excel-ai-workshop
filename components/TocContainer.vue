<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const rootEl = ref(null)

function offsetTopFrom(el, ancestor) {
  let top = 0, cur = el
  while (cur && cur !== ancestor) { top += cur.offsetTop; cur = cur.offsetParent }
  return top
}

function clamp() {
  if (!rootEl.value) return
  const slide = rootEl.value.closest('.slidev-layout')
  if (!slide) return
  const maxH = slide.offsetHeight - offsetTopFrom(rootEl.value, slide) - 24
  rootEl.value.style.maxHeight = maxH > 60 ? `${maxH}px` : ''
}

let ro
onMounted(() => {
  clamp()
  ro = new ResizeObserver(clamp)
  const slide = rootEl.value?.closest('.slidev-layout')
  if (slide) ro.observe(slide)
})
onBeforeUnmount(() => ro?.disconnect())
</script>

<template>
  <div ref="rootEl" class="toc-container">
    <slot />
  </div>
</template>

<style scoped>
.toc-container {
  overflow-y: auto;
  padding-left: 0.75rem;
  padding-right: 0.5rem;
}
.toc-container::-webkit-scrollbar       { width: 6px; }
.toc-container::-webkit-scrollbar-track { background: transparent; }
.toc-container::-webkit-scrollbar-thumb { background: #555; border-radius: 3px; }
.toc-container::-webkit-scrollbar-thumb:hover { background: #777; }
</style>
