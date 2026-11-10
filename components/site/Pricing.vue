<script setup lang="ts">
import { business } from '~/config/business'
</script>

<template>
  <section id="cennik" class="mx-auto max-w-4xl scroll-mt-20 px-5 py-20">
    <p class="eyebrow reveal">Cennik</p>
    <h2 class="section-title reveal mt-3" style="--reveal-delay: 80ms">Orientacyjne ceny</h2>

    <div class="reveal mt-10 overflow-hidden rounded-xl border border-border bg-card" style="--reveal-delay: 150ms">
      <div
        class="flex items-center justify-between border-b border-border px-6 py-4 text-xs uppercase tracking-widest text-muted-foreground"
      >
        <span>Usługa</span>
        <span>Cena od</span>
      </div>
      <div
        v-for="row in business.pricing"
        :key="row.name"
        class="group flex items-center justify-between border-b border-border/70 px-6 py-4 transition-colors last:border-b-0 hover:bg-secondary/50"
      >
        <span class="text-sm sm:text-base">{{ row.name }}</span>
        <span class="font-semibold text-primary">{{ row.price }}</span>
      </div>
    </div>
    <p class="reveal mt-4 text-sm text-muted-foreground">
      Ostateczna cena zależy od modelu samochodu i zakresu prac.
    </p>
  </section>
</template>
