<script setup lang="ts">
import { CalendarDays, Phone } from 'lucide-vue-next'
import { business } from '~/config/business'
import heroImage from '~/assets/img/hero-workshop.jpg'
</script>

<template>
  <header id="top" class="relative isolate overflow-hidden bg-ink">
    <img
      :src="heroImage"
      alt="Wnętrze warsztatu samochodowego z autem na podnośniku"
      width="1920"
      height="1088"
      class="hero-img absolute inset-0 -z-20 h-full w-full object-cover opacity-70"
      fetchpriority="high"
    />
    <div class="absolute inset-0 -z-10 bg-gradient-to-r from-ink via-ink/90 to-ink/45" />
    <!-- czerwona poświata -->
    <div
      class="pointer-events-none absolute -left-32 top-1/3 -z-10 h-96 w-96 rounded-full bg-primary/20 blur-[120px]"
    />

    <div class="mx-auto flex min-h-[78vh] max-w-6xl flex-col justify-center px-5 pb-24 pt-24 sm:pt-32">
      <div
        class="hero-glow-line mb-6 h-1 w-24 rounded-full bg-gradient-to-r from-primary to-transparent"
      />
      <h1
        class="hero-rise max-w-3xl font-display text-[clamp(2.5rem,7vw,5rem)] font-extrabold italic uppercase leading-[0.95] tracking-tight text-ink-foreground"
        style="--hero-delay: 80ms"
      >
        Warsztat samochodowy
        <br />
        {{ business.name }}
      </h1>
      <p
        class="hero-rise mt-6 max-w-xl text-base font-bold text-ink-foreground sm:text-lg"
        style="--hero-delay: 220ms"
      >
        {{ business.tagline }}
      </p>

      <div class="hero-rise mt-10 flex flex-col gap-3 sm:flex-row" style="--hero-delay: 360ms">
        <a
          href="#wycena"
          class="inline-flex h-13 items-center justify-center gap-2 rounded-full bg-ink-foreground px-9 text-base font-semibold text-ink transition-all duration-300 hover:-translate-y-0.5 hover:shadow-elegant"
        >
          <CalendarDays class="h-5 w-5" /> Umów wizytę
        </a>
        <a
          :href="`tel:${business.phone}`"
          class="group inline-flex h-13 items-center justify-center gap-2 rounded-full bg-primary px-9 text-base font-semibold text-primary-foreground transition-all duration-300 hover:-translate-y-0.5 hover:shadow-elegant"
        >
          <Phone class="h-5 w-5 transition-transform duration-300 group-hover:rotate-12" />
          Zadzwoń
        </a>
      </div>
    </div>

    <div class="checkers h-5 w-full" />
  </header>
</template>

<style scoped>
.h-13 {
  height: 3.25rem;
}
</style>
