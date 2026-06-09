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
  background: #2a2a2a;
  border-radius: 0.75rem;
  padding: 1.5rem 1.8rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  overflow: hidden;
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
