<script setup lang="ts">
import { business } from '~/config/business'
</script>

<template>
  <section id="proces" class="scroll-mt-20 bg-ink text-ink-foreground">
    <div class="checkers h-4 w-full" />
    <div class="mx-auto max-w-6xl px-5 py-20">
      <p class="eyebrow reveal">Jak wygląda wizyta?</p>
      <h2 class="section-title reveal mt-3" style="--reveal-delay: 80ms">Cztery proste kroki</h2>
      <div class="mt-10 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
        <div
          v-for="(step, i) in business.steps"
          :key="step.no"
          class="reveal group rounded-2xl border border-ink-muted/20 bg-ink-foreground/5 p-6 transition-all duration-300 hover:-translate-y-1 hover:border-primary/50 hover:bg-ink-foreground/10"
          :style="{ '--reveal-delay': `${i * 110}ms` }"
        >
          <span
            class="font-display text-3xl font-semibold text-primary transition-transform duration-300 group-hover:scale-110"
          >
            {{ step.no }}
          </span>
          <h3 class="mt-4 text-base font-semibold">{{ step.title }}</h3>
          <p class="mt-2 text-sm text-ink-muted">{{ step.text }}</p>
        </div>
      </div>
    </div>
  </section>
</template>
