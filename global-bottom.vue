<script setup>
import { useNav } from '@slidev/client'
const { currentPage, total } = useNav()
</script>

<template>
  <div class="progress-track">
    <div class="progress-fill" :style="{ width: `${(currentPage / total) * 100}%` }" />
  </div>
</template>

<style scoped>
.progress-track {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: rgba(255, 255, 255, 0.12);
  z-index: 100;
}
.progress-fill {
  height: 100%;
  background: rgba(99, 179, 237, 0.75);
  transition: width 0.35s ease;
}
</style>
