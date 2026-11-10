<script setup lang="ts">
import { Check } from 'lucide-vue-next'
import { business } from '~/config/business'
</script>

<template>
  <section class="border-y border-border bg-secondary/40">
    <div class="mx-auto max-w-6xl px-5 py-20">
      <p class="eyebrow reveal">Dlaczego my?</p>
      <h2 class="section-title reveal mt-3" style="--reveal-delay: 80ms">Konkret zamiast obietnic</h2>
      <div class="mt-10 grid gap-8 sm:grid-cols-2 lg:grid-cols-4">
        <div
          v-for="(item, i) in business.advantages"
          :key="item.title"
          class="reveal group"
          :style="{ '--reveal-delay': `${i * 100}ms` }"
        >
          <span
            class="flex h-9 w-9 items-center justify-center rounded-full border border-primary/40 text-primary transition-all duration-300 group-hover:bg-primary group-hover:text-primary-foreground"
          >
            <Check class="h-4 w-4" />
          </span>
          <h3 class="mt-4 text-lg font-semibold">{{ item.title }}</h3>
          <p class="mt-1 text-sm text-muted-foreground">{{ item.text }}</p>
        </div>
      </div>
    </div>
  </section>
</template>
