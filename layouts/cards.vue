<script setup lang="ts">
import { computed, useId } from 'vue'
import { useSlideContext } from '@slidev/client'
import { bgStyle } from 'slidev-theme-viewsonic-proav/composables/background'
import { themeImage } from 'slidev-theme-viewsonic-proav/composables/assets'

// themeImage returns user paths unchanged (e.g. "/images/foo.jpg"), which
// breaks when the site is served under a sub-path (GitHub Pages base URL).
// Prepend BASE_URL for absolute user paths so the URL becomes correct in
// both dev (base = "/") and production (base = "/excel-ai-workshop/").
function resolveImage(ref?: string): string | undefined {
  const src = themeImage(ref)
  if (!src) return undefined
  if (src.startsWith('/') && !src.startsWith('//'))
    return import.meta.env.BASE_URL.replace(/\/$/, '') + src
  return src
}
import ConfidentialMark from 'slidev-theme-viewsonic-proav/components/ConfidentialMark.vue'
import PageNumber from 'slidev-theme-viewsonic-proav/components/PageNumber.vue'
import gridBg from 'slidev-theme-viewsonic-proav/assets/content-grid-bg.png'
import mark from 'slidev-theme-viewsonic-proav/assets/viewsonic-mark.png'

interface Card {
  image?: string
  title?: string
  text?: string
  items?: string[]
  tags?: string[]
}

const props = defineProps<{
  background?: string
  cards?: Card[]
  fill?: boolean
  cols?: number
}>()

const { $frontmatter } = useSlideContext()
const cards = computed<Card[]>(() => props.cards ?? $frontmatter?.value?.cards ?? [])
const fill  = computed<boolean>(() => props.fill  ?? $frontmatter?.value?.fill  ?? false)
const cols  = computed<number>(() => props.cols  ?? $frontmatter?.value?.cols  ?? (cards.value.length || 1))
const rows  = computed<number>(() => Math.ceil(cards.value.length / cols.value))
const style = computed(() => bgStyle(props.background || gridBg))

const uid = useId()
const imgClipId = `vs-card-clip-${uid}`
const bodyClipId = `vs-card-body-clip-${uid}`
</script>

<template>
  <div class="slidev-layout cards" :style="style">
    <svg width="0" height="0" aria-hidden="true" style="position:absolute">
      <defs>
        <clipPath :id="imgClipId" clipPathUnits="objectBoundingBox">
          <path d="M0,0 L0.8674,0 L0.8982,0.0095 C0.958,0.0346 1,0.0933 1,0.1618 L1,1 L0,1 Z" />
        </clipPath>
        <clipPath :id="bodyClipId" clipPathUnits="objectBoundingBox">
          <path d="M1,1 L0.1326,1 L0.1018,0.9905 C0.042,0.9654 0,0.9067 0,0.8382 L0,0 L1,0 Z" />
        </clipPath>
      </defs>
    </svg>

    <ConfidentialMark />

    <div class="vs-cards__head">
      <slot />
    </div>

    <div class="vs-cards__grid" :style="{ '--cols': cols, '--rows': rows, '--col-size': fill ? '1fr' : 'minmax(0, 18rem)' }">
      <div
        v-for="(card, i) in cards"
        :key="i"
        class="vs-card"
        :class="{
          'vs-card--image-only': card.image && !card.title && !card.text && !card.items,
          'vs-card--text-only':  !card.image,
        }"
      >
        <img
          v-if="card.image"
          class="vs-card__img"
          :src="resolveImage(card.image)"
          :alt="card.title || ''"
          :style="{ clipPath: `url(#${imgClipId})` }"
        >
        <div
          v-if="card.title || card.text || card.items"
          class="vs-card__body"
          :style="{ clipPath: `url(#${bodyClipId})` }"
        >
          <h3 v-if="card.title" class="vs-card__title">{{ card.title }}</h3>
          <p v-if="card.text" class="vs-card__text">{{ card.text }}</p>
          <ul v-if="card.items" class="vs-card__items">
            <li v-for="(item, j) in card.items" :key="j">{{ item }}</li>
          </ul>
          <div v-if="card.tags?.length" class="vs-card__tags">
            <span v-for="(tag, j) in card.tags" :key="j" class="vs-card__tag">#{{ tag }}</span>
          </div>
        </div>
      </div>
    </div>

    <img :src="mark" class="vs-cards__logo" alt="ViewSonic">
    <PageNumber />
  </div>
</template>

<style scoped>
.slidev-layout.cards {
  position: relative;
  height: 100%;
  padding: 2rem 3.6rem 3.4rem 6%;
  display: grid;
  grid-template-rows: auto 1fr;
  gap: 0.6rem;
  background-size: cover;
  background-position: center;
  overflow: hidden;
}
.vs-cards__head {
  max-width: 76.5%;
  z-index: 2;
}
.vs-cards__head :deep(h1) {
  font-size: 3rem;
  line-height: 1.2;
  margin: 0 0 0.5rem;
}
.vs-cards__head :deep(h1)::after {
  content: none;
}
.vs-cards__head :deep(p) {
  font-size: 1rem;
  line-height: 1.4;
  color: #fff;
  margin: 0;
}

.vs-cards__grid {
  display: grid;
  grid-template-columns: repeat(var(--cols, 1), var(--col-size, minmax(0, 18rem)));
  gap: 1.6rem;
  align-self: start;
  justify-content: center;
  margin-top: 2rem;
  z-index: 2;
}
.vs-card {
  position: relative;
  display: grid;
  grid-template-rows: 1fr 1fr;
  min-height: calc(27rem / var(--rows, 1));
  max-height: calc(29rem / var(--rows, 1));
}
.vs-card--image-only {
  grid-template-rows: 1fr;
}
.vs-card--text-only {
  grid-template-rows: 1fr;
}
.vs-card__img {
  position: relative;
  z-index: 1;
  width: 100%;
  height: 100%;
  min-height: 0;
  object-fit: cover;
  display: block;
}
.vs-card__body {
  position: relative;
  z-index: 0;
  min-height: 0;
  overflow: hidden;
  padding: 8% 0.9rem 1.1rem 7%;
  background: #404041;
  clip-path: url(#vs-card-body-clip);
}
.vs-card__title {
  font-size: 1.05rem;
  font-weight: 600;
  color: #fff;
  margin: 0 0 0.4rem;
}
.vs-card__items {
  margin: 0;
  font-size: 0.8rem;
  line-height: 1.4;
}
.vs-card__text {
  font-size: 0.8rem;
  font-weight: 300;
  line-height: 1.5;
  color: #d4d5da;
  margin: 0 0 0.5rem;
}
.vs-card__tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.3rem;
  margin-top: 0.4rem;
}
.vs-card__tag {
  font-size: 0.7rem;
  font-family: monospace;
  color: #7dd3fc;
  background: rgba(125, 211, 252, 0.1);
  border: 1px solid rgba(125, 211, 252, 0.25);
  border-radius: 4px;
  padding: 0.1rem 0.45rem;
  white-space: nowrap;
}
.vs-cards__logo {
  position: absolute;
  right: 2.4rem;
  bottom: 1.5rem;
  height: 1.3rem;
  width: auto;
  z-index: 3;
}
</style>
