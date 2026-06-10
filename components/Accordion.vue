<script setup>
import { ref } from 'vue'

const props = defineProps({
  title:       { type: String, required: true },
  open:        { type: Boolean, default: false },
  titleClass:  { type: String, default: '' },
})

const isOpen = ref(props.open)
</script>

<template>
  <div class="accordion">
    <button class="accordion-header" :class="{ open: isOpen }" @click="isOpen = !isOpen">
      <span class="accordion-title" :class="titleClass">{{ title }}</span>
      <span class="accordion-icon">{{ isOpen ? '▲' : '▼' }}</span>
    </button>
    <Transition name="accordion">
      <div v-show="isOpen" class="accordion-body">
        <slot />
      </div>
    </Transition>
  </div>
</template>

<style scoped>
.accordion {
  border: 1px solid #444;
  border-radius: 6px;
  overflow: hidden;
  margin-bottom: 0.5rem;
}

.accordion-header {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.55rem 1rem;
  background: #2a2a2a;
  cursor: pointer;
  border: none;
  text-align: left;
  transition: background 0.2s;
}
.accordion-header:hover  { background: #333; }
.accordion-header.open   { background: #1e3a5f; }

.accordion-title { font-weight: 600; font-size: 0.95em; }
.accordion-icon  { font-size: 0.7em; opacity: 0.7; flex-shrink: 0; margin-left: 0.5rem; }

.accordion-body {
  padding: 0.65rem 1rem;
  background: #1a1a1a;
}

/* height transition */
.accordion-enter-active,
.accordion-leave-active { transition: opacity 0.2s, transform 0.2s; }
.accordion-enter-from   { opacity: 0; transform: translateY(-4px); }
.accordion-leave-to     { opacity: 0; transform: translateY(-4px); }
</style>
