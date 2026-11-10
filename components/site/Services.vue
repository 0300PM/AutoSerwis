<script setup lang="ts">
import { CircleDot, Droplets, ScanLine, Snowflake, Wrench } from 'lucide-vue-next'
import { business } from '~/config/business'

const icons: Record<string, unknown> = {
  wrench: Wrench,
  scan: ScanLine,
  snowflake: Snowflake,
  tire: CircleDot,
  oil: Droplets
}
</script>

<template>
  <section id="uslugi" class="mx-auto max-w-6xl scroll-mt-20 px-5 py-20">
    <p class="eyebrow reveal">Katalog usług</p>
    <h2 class="section-title reveal mt-3" style="--reveal-delay: 80ms">Czym się zajmujemy</h2>

    <div class="mt-10 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
      <article
        v-for="(service, i) in business.services"
        :key="service.name"
        class="reveal card-glow group flex flex-col rounded-2xl border border-border bg-card p-7 transition-all duration-300 hover:-translate-y-1.5 hover:border-primary/40 hover:shadow-soft"
        :style="{ '--reveal-delay': `${(i % 3) * 110}ms` }"
      >
        <span
          class="flex h-12 w-12 items-center justify-center rounded-full bg-accent text-primary transition-all duration-300 group-hover:rotate-6 group-hover:bg-primary group-hover:text-primary-foreground"
        >
          <component :is="icons[service.icon] ?? Wrench" class="h-6 w-6" />
        </span>
        <h3 class="mt-6 text-xl font-semibold">{{ service.name }}</h3>
        <p class="mt-2 flex-1 text-sm leading-relaxed text-muted-foreground">
          {{ service.description }}
        </p>
        <p class="mt-6 text-lg font-semibold text-primary">{{ service.price }}</p>
      </article>
    </div>
  </section>
</template>
