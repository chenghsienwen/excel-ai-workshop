<script setup lang="ts">
const props = defineProps<{
  path: string
  files: string[]
}>()

const folderName = props.path.split('/').pop()

function fileIcon(name: string) {
  if (/\.xlsx?$/i.test(name)) return '📊'
  if (/\.csv$/i.test(name)) return '📄'
  if (/\.json$/i.test(name)) return '📋'
  return '📄'
}
</script>

<template>
  <div class="file-tree">
    <div class="ft-folder">
      <span class="ft-icon">📂</span>
      <span class="ft-path">{{ path }}</span>
    </div>
    <div class="ft-children">
      <div v-for="(file, i) in files" :key="i" class="ft-file">
        <span class="ft-icon">{{ fileIcon(file) }}</span>
        <span class="ft-name">{{ file }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.file-tree {
  font-family: monospace;
  font-size: 1.15rem;
  line-height: 2;
  margin-top: 1.5rem;
  display: inline-block;
}
.ft-folder {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: 600;
  color: #fff;
}
.ft-children {
  padding-left: 1.5rem;
  border-left: 2px solid #555;
  margin-left: 0.8rem;
}
.ft-file {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #d4d5da;
}
.ft-icon { font-style: normal; }
.ft-path { color: #a8b4c8; }
.ft-name { letter-spacing: 0.01em; }
</style>
