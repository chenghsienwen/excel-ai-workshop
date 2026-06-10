<script setup>
import { computed } from 'vue'
import { encode } from 'uqr'

const props = defineProps({
  url:     { type: String, required: true },
  size:    { type: Number, default: 200 },
  light:   { type: String, default: '#ffffff' },
  dark:    { type: String, default: '#000000' },
})

const matrix = computed(() => encode(props.url).data)
const cells  = computed(() => matrix.value.length)
</script>

<template>
  <svg
    :width="size"
    :height="size"
    :viewBox="`0 0 ${cells} ${cells}`"
    shape-rendering="crispEdges"
    xmlns="http://www.w3.org/2000/svg"
  >
    <rect width="100%" height="100%" :fill="light" />
    <template v-for="(row, y) in matrix" :key="y">
      <rect
        v-for="(on, x) in row"
        v-show="on"
        :key="x"
        :x="x" :y="y"
        width="1" height="1"
        :fill="dark"
      />
    </template>
  </svg>
</template>
