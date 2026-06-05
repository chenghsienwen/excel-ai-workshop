<script setup>
const now = new Date()
const date = `${now.getFullYear()}.${String(now.getMonth() + 1).padStart(2, '0')}.${String(now.getDate()).padStart(2, '0')}`
</script>

<template>
  <Teleport to=".slidev-layout.cover" defer>
    <div class="current-date">{{ date }}</div>
  </Teleport>
</template>

<style scoped>
.current-date {
  position: absolute;
  bottom: 2rem;
  right: 2.4rem;
  font-size: 0.9rem;
  color: #b4b4b4;
  font-family: sans-serif;
  white-space: nowrap;
  z-index: 10;
}
</style>
