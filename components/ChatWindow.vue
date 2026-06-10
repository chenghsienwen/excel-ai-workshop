<script setup>
import { useSlots, computed, ref, onMounted, onBeforeUnmount } from 'vue'

const slots = useSlots()

const turns = computed(() =>
  [1, 2, 3, 4, 5]
    .filter(n => slots[n === 1 ? 'question' : `question${n}`])
    .map(n => ({
      q: n === 1 ? 'question' : `question${n}`,
      r: n === 1 ? 'response' : `response${n}`,
    }))
)

const rootEl  = ref(null)
const zoom    = ref(1)
const zoomIn  = () => { zoom.value = Math.min(2,   +(zoom.value + 0.1).toFixed(1)) }
const zoomOut = () => { zoom.value = Math.max(0.5, +(zoom.value - 0.1).toFixed(1)) }

// Sum offsetTop values walking up from el to ancestor (CSS pixels, scale-safe).
function offsetTopFrom(el, ancestor) {
  let top = 0
  let cur = el
  while (cur && cur !== ancestor) {
    top += cur.offsetTop
    cur = cur.offsetParent
  }
  return top
}

function clampToSlide() {
  if (!rootEl.value) return
  const slide = rootEl.value.closest('.slidev-layout')
  if (!slide) return
  const slideH   = slide.offsetHeight
  const chatTop  = offsetTopFrom(rootEl.value, slide)
  const maxH     = slideH - chatTop - 24   // 24 px bottom breathing room
  rootEl.value.style.maxHeight = maxH > 60 ? `${maxH}px` : ''
}

let ro
onMounted(() => {
  clampToSlide()
  ro = new ResizeObserver(clampToSlide)
  const slide = rootEl.value?.closest('.slidev-layout')
  if (slide) ro.observe(slide)
})
onBeforeUnmount(() => ro?.disconnect())
</script>

<template>
  <div ref="rootEl" class="chat-window border border-[#2f2f2f] rounded-2xl overflow-hidden shadow-2xl w-full max-w-3xl mx-auto bg-[#171717] font-sans text-[15px] text-[#ececec]">

    <!-- Title bar -->
    <div class="flex-none bg-[#171717] px-4 py-3 border-b border-[#2f2f2f] flex items-center justify-between">
      <div class="flex space-x-1.5">
        <span class="w-3 h-3 rounded-full bg-[#ff5f56]"></span>
        <span class="w-3 h-3 rounded-full bg-[#ffbd2e]"></span>
        <span class="w-3 h-3 rounded-full bg-[#27c93f]"></span>
      </div>
      <div class="flex items-center space-x-1 text-sm font-medium text-[#b4b4b4] hover:text-white cursor-pointer transition">
        <span>ChatGPT 4o</span>
        <i class="fa-solid fa-chevron-down text-xs"></i>
      </div>
      <div class="flex items-center space-x-3 text-[#b4b4b4]">
        <button class="zoom-btn" title="Zoom out" @click="zoomOut">−</button>
        <span class="zoom-label">{{ Math.round(zoom * 100) }}%</span>
        <button class="zoom-btn" title="Zoom in" @click="zoomIn">+</button>
        <i class="fa-regular fa-pen-to-square hover:text-white cursor-pointer ml-1"></i>
      </div>
    </div>

    <!-- Message area — grows to fill remaining height, scrolls when content overflows -->
    <div class="chat-messages p-6 space-y-6 bg-[#171717]" :style="{ zoom }">
      <template v-for="turn in turns" :key="turn.q">
        <!-- User bubble -->
        <div class="flex items-start flex-row-reverse gap-4">
          <div class="flex-shrink-0 w-8 h-8 rounded-full bg-[#ab5cf0] flex items-center justify-center text-white font-semibold text-xs shadow-sm">U</div>
          <div class="bg-[#2f2f2f] text-[#ececec] px-4 py-3 rounded-2xl rounded-tr-sm max-w-[75%] border border-[#3e3e3e] text-left leading-relaxed">
            <slot :name="turn.q"></slot>
          </div>
        </div>
        <!-- AI response -->
        <div class="flex items-start gap-4">
          <div class="flex-shrink-0 w-8 h-8 rounded-full bg-[#19c37d] flex items-center justify-center text-white shadow-md">
            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M21.1 11.2C21.7 10.4 21.9 9.3 21.6 8.3C21.3 7.3 20.6 6.5 19.6 6.1C19.5 6.0 19.3 6.0 19.2 6.0C19.2 4.9 18.7 3.8 17.8 3.1C16.9 2.4 15.7 2.1 14.6 2.3C14.5 2.3 14.3 2.4 14.2 2.4C13.5 1.7 12.5 1.3 11.5 1.3C10.5 1.3 9.5 1.7 8.8 2.4C8.7 2.4 8.5 2.3 8.4 2.3C7.3 2.1 6.1 2.4 5.2 3.1C4.3 3.8 3.8 4.9 3.8 6.0C3.7 6.0 3.5 6.0 3.4 6.1C2.4 6.5 1.7 7.3 1.4 8.3C1.1 9.3 1.3 10.4 1.9 11.2C1.3 12.0 1.1 13.1 1.4 14.1C1.7 15.1 2.4 15.9 3.4 16.3C3.5 16.4 3.7 16.4 3.8 16.4C3.8 17.5 4.3 18.6 5.2 19.3C6.1 20.0 7.3 20.3 8.4 20.1C8.5 20.1 8.7 20.0 8.8 20.0C9.5 20.7 10.5 21.1 11.5 21.1C12.5 21.1 13.5 20.7 14.2 20.0C14.3 20.0 14.5 20.1 14.6 20.1C15.7 20.3 16.9 20.0 17.8 19.3C18.7 18.6 19.2 17.5 19.2 16.4C19.3 16.4 19.5 16.4 19.6 16.3C20.6 15.9 21.3 15.1 21.6 14.1C21.9 13.1 21.7 12.0 21.1 11.2ZM11.5 18.5C11.1 18.5 10.8 18.3 10.5 18.0L14.0 14.5L14.7 15.2C15.1 15.6 15.1 16.2 14.7 16.6L12.5 18.0C12.2 18.3 11.8 18.5 11.5 18.5ZM5.9 14.8C5.6 14.5 5.5 14.1 5.5 13.7L5.5 8.7L6.5 9.2C7.0 9.5 7.3 10.0 7.3 10.6L7.3 13.7C7.3 14.3 7.0 14.8 6.5 15.1L5.9 14.8ZM6.8 6.1C7.1 5.8 7.5 5.7 7.9 5.8L12.9 7.4L12.9 8.4C12.9 9.0 12.6 9.5 12.1 9.8L9.0 11.6C8.5 11.9 7.9 11.9 7.4 11.6L6.8 11.2C6.4 10.8 6.4 10.2 6.8 9.8L6.8 6.1ZM13.8 8.9L10.3 6.9L11.0 5.8C11.3 5.4 11.9 5.2 12.4 5.5L15.5 7.3C16.0 7.6 16.3 8.1 16.3 8.7L16.3 11.2L13.8 8.9ZM16.7 13.7C16.7 14.1 16.5 14.5 16.1 14.8L11.1 18.0L11.1 17.0C11.1 16.4 11.4 15.9 11.9 15.6L15.0 13.8C15.5 13.5 16.1 13.5 16.6 13.8L17.2 14.2C17.6 14.6 17.6 15.2 17.2 15.6L16.7 13.7ZM18.1 10.3C18.4 10.6 18.5 11.0 18.5 11.4L18.5 16.4L17.5 15.9C17.0 15.6 16.7 15.1 16.7 14.5L16.7 11.4C16.7 10.8 17.0 10.3 17.5 10.0L18.1 10.3Z" fill="currentColor"/>
            </svg>
          </div>
          <div class="text-left leading-relaxed max-w-[85%] space-y-2 pt-1">
            <slot :name="turn.r"></slot>
          </div>
        </div>
      </template>
    </div>

    <!-- Footer -->
    <div class="flex-none px-5 pb-5 pt-2 bg-[#171717]">
      <div class="bg-[#2f2f2f] rounded-3xl px-4 py-3 flex items-center justify-between text-sm text-[#b4b4b4] border border-[#3e3e3e]">
        <div class="flex items-center space-x-3 w-full">
          <i class="fa-solid fa-paperclip hover:text-white cursor-pointer transition text-base"></i>
          <span class="text-sm select-none truncate">Message ChatGPT...</span>
        </div>
        <div class="flex items-center space-x-3.5 pl-2">
          <i class="fa-solid fa-globe hover:text-white cursor-pointer transition text-base"></i>
          <i class="fa-regular fa-face-smile hover:text-white cursor-pointer transition text-base"></i>
          <div class="w-8 h-8 rounded-full bg-white text-black flex items-center justify-center cursor-pointer hover:bg-neutral-200 transition">
            <i class="fa-solid fa-arrow-up text-xs"></i>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.chat-window {
  display: flex;
  flex-direction: column;
}

/* Fills the remaining height between title bar and footer; scrolls on overflow */
.chat-messages {
  flex: 1;
  min-height: 0;
  overflow-y: auto;
}

.chat-messages::-webkit-scrollbar        { width: 4px; }
.chat-messages::-webkit-scrollbar-track  { background: transparent; }
.chat-messages::-webkit-scrollbar-thumb  { background: #444; border-radius: 2px; }
.chat-messages::-webkit-scrollbar-thumb:hover { background: #666; }

.zoom-btn {
  background: none;
  border: 1px solid #444;
  border-radius: 4px;
  color: #b4b4b4;
  width: 1.3rem;
  height: 1.3rem;
  line-height: 1;
  font-size: 0.95rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
  transition: color 0.15s, border-color 0.15s;
}
.zoom-btn:hover { color: #fff; border-color: #888; }
.zoom-label {
  font-size: 0.7rem;
  min-width: 2.4rem;
  text-align: center;
  color: #888;
  font-variant-numeric: tabular-nums;
}
</style>
