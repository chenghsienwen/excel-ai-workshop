<script setup lang="ts">
const date = (__GIT_DATE__ as string)
</script>

<template>
  <Teleport to=".slidev-layout.cover" defer>
    <div class="last-modified-date">Last updated: {{ date }}</div>
  </Teleport>
</template>

<style scoped>
.last-modified-date {
  position: absolute;
  bottom: 0.4rem;
  right: 2.4rem;
  font-size: 0.9rem;
  color: #b4b4b4;
  font-family: sans-serif;
  white-space: nowrap;
  z-index: 10;
}
</style>
