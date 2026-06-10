<script setup lang="ts">
defineProps<{
  leftTitle?: string
  rightTitle?: string
}>()
</script>

<template>
  <div class="two-cols">
    <div class="two-cols__card">
      <div v-if="leftTitle" class="two-cols__title">{{ leftTitle }}</div>
      <slot name="left" />
    </div>
    <div class="two-cols__card">
      <div v-if="rightTitle" class="two-cols__title">{{ rightTitle }}</div>
      <slot name="right" />
    </div>
  </div>
</template>

<style scoped>
.two-cols {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
  margin-top: 1rem;
  height: calc(100% - 5rem);
}
.two-cols__card {
  position: relative;
  background: #2a2a2a;
  border-radius: 0.75rem;
  padding: 1.5rem 1.8rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  overflow: hidden;
  transition: box-shadow 0.2s, transform 0.2s;
  cursor: default;
}
.two-cols__card::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: transparent;
  pointer-events: none;
  transition: background 0.2s;
}
.two-cols__card:hover {
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
  transform: translateY(-2px);
  background: #5a3520;
}
.two-cols__card:hover::before {
  background: rgba(255, 153, 102, 0.18);
}
.two-cols__title {
  font-size: 1.1rem;
  font-weight: 600;
  color: #fff;
  border-bottom: 1px solid #444;
  padding-bottom: 0.5rem;
  margin-bottom: 0.25rem;
}
</style>
