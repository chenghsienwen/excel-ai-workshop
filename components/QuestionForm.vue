<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const MAX_BYTES   = 5 * 1024 * 1024   // 5 MB
const MAX_CHARS   = 300
const STORAGE_KEY = 'slidev-question-log'

const text    = ref('')
const entries = ref([])
const status  = ref('')

const encoder = new TextEncoder()
function byteSize(str) { return encoder.encode(str).length }

function pad(n) { return String(n).padStart(2, '0') }
function timestamp() {
  const d = new Date()
  return `${d.getFullYear()}/${pad(d.getMonth() + 1)}/${pad(d.getDate())} ` +
         `${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}`
}

function persist() {
  localStorage.setItem(STORAGE_KEY, entries.value.join('\n'))
}

onMounted(() => {
  const raw = localStorage.getItem(STORAGE_KEY) || ''
  entries.value = raw.split('\n').filter(Boolean)
})

function submit() {
  const trimmed = text.value.trim().slice(0, MAX_CHARS)
  if (!trimmed) return

  const entry = `${timestamp()} | ${trimmed}`
  entries.value.push(entry)

  // Drop oldest lines until total log fits within 5 MB
  let joined = entries.value.join('\n')
  while (byteSize(joined) > MAX_BYTES && entries.value.length > 1) {
    entries.value.shift()
    joined = entries.value.join('\n')
  }

  persist()
  text.value = ''
  status.value = 'Saved.'
  setTimeout(() => { status.value = '' }, 1500)
}

function download() {
  const blob = new Blob([entries.value.join('\n')], { type: 'text/plain' })
  const url  = URL.createObjectURL(blob)
  const a    = Object.assign(document.createElement('a'), { href: url, download: 'questions.txt' })
  a.click()
  URL.revokeObjectURL(url)
}

function clear() {
  entries.value = []
  persist()
}

// ── height clamping ───────────────────────────────────────────────────────
const rootEl = ref(null)
const logEl  = ref(null)

function offsetTopFrom(el, ancestor) {
  let top = 0, cur = el
  while (cur && cur !== ancestor) { top += cur.offsetTop; cur = cur.offsetParent }
  return top
}

function clampLog() {
  if (!rootEl.value || !logEl.value) return
  const slide = rootEl.value.closest('.slidev-layout')
  if (!slide) return
  const available = slide.offsetHeight - offsetTopFrom(logEl.value, slide) - 16
  logEl.value.style.maxHeight = available > 60 ? `${available}px` : ''
}

let ro
onMounted(() => {
  clampLog()
  ro = new ResizeObserver(clampLog)
  const slide = rootEl.value?.closest('.slidev-layout')
  if (slide) ro.observe(slide)
})
onBeforeUnmount(() => ro?.disconnect())
</script>

<template>
  <div ref="rootEl" class="qf">
    <div class="qf__input-row">
      <textarea
        v-model="text"
        class="qf__textarea"
        :maxlength="MAX_CHARS"
        placeholder="Type your question…"
        rows="3"
        @keydown.ctrl.enter.prevent="submit"
        @keydown.meta.enter.prevent="submit"
      />
      <div class="qf__actions">
        <button class="qf__btn qf__btn--primary" @click="submit">Submit</button>
        <button class="qf__btn" @click="download" :disabled="!entries.length">Download</button>
        <button class="qf__btn qf__btn--danger" @click="clear" :disabled="!entries.length">Clear</button>
      </div>
    </div>

    <div class="qf__meta">
      <span class="qf__count">char count: {{ text.length }} / {{ MAX_CHARS }}</span>
      <span v-if="status" class="qf__status">{{ status }}</span>
      <span class="qf__count">{{ entries.length }} entr{{ entries.length === 1 ? 'y' : 'ies' }}</span>
    </div>

    <div v-if="entries.length" ref="logEl" class="qf__log">
      <div v-for="(e, i) in [...entries].reverse()" :key="i" class="qf__entry">{{ e }}</div>
    </div>
    <div v-else class="qf__empty">No entries yet.</div>
  </div>
</template>

<style scoped>
.qf {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  font-family: monospace;
}
.qf__input-row {
  display: flex;
  gap: 0.75rem;
  align-items: flex-start;
}
.qf__textarea {
  flex: 1;
  background: #1a1a1a;
  border: 1px solid #555;
  border-radius: 6px;
  color: #d4d5da;
  font-size: 0.85rem;
  line-height: 1.5;
  padding: 0.5rem 0.7rem;
  resize: none;
  outline: none;
}
.qf__textarea:focus { border-color: #f96; }

.qf__actions {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}
.qf__btn {
  background: #2d2d2d;
  border: 1px solid #555;
  border-radius: 5px;
  color: #ccc;
  cursor: pointer;
  font-size: 0.75rem;
  padding: 0.3rem 0.8rem;
  white-space: nowrap;
}
.qf__btn:hover:not(:disabled) { background: #3a3a3a; color: #fff; }
.qf__btn:disabled { opacity: 0.4; cursor: default; }
.qf__btn--primary { background: #f96; color: #000; border-color: #f96; font-weight: 600; }
.qf__btn--primary:hover { background: #ffaa66; }
.qf__btn--danger:hover:not(:disabled) { background: #7f1d1d; border-color: #ef4444; color: #fff; }

.qf__meta {
  display: flex;
  justify-content: space-between;
  font-size: 0.65rem;
  color: #666;
}
.qf__status { color: #4ade80; }

.qf__log {
  border: 1px solid #333;
  border-radius: 6px;
  background: #111;
  overflow-y: auto;
  padding: 0.4rem 0.6rem;
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
}
.qf__entry {
  font-size: 0.65rem;
  color: #aaa;
  line-height: 1.5;
  word-break: break-word;
}
.qf__empty { font-size: 0.7rem; color: #555; }

.qf__log::-webkit-scrollbar       { width: 6px; }
.qf__log::-webkit-scrollbar-track { background: #111; }
.qf__log::-webkit-scrollbar-thumb { background: #444; border-radius: 3px; }
</style>
