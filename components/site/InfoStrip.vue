<script setup lang="ts">
import { Clock, MapPin, Phone } from 'lucide-vue-next'
import { business } from '~/config/business'
</script>

<template>
  <section class="bg-ink text-ink-foreground">
    <div class="mx-auto grid max-w-6xl gap-10 px-5 py-14 sm:grid-cols-3">
      <div class="reveal text-center" style="--reveal-delay: 0ms">
        <span
          class="mx-auto flex h-14 w-14 items-center justify-center rounded-full border-2 border-primary text-primary transition-transform duration-300 hover:scale-110"
        >
          <Phone class="h-6 w-6" />
        </span>
        <h3 class="mt-4 font-display text-lg font-extrabold italic uppercase">Kontakt</h3>
        <a
          :href="`tel:${business.phone}`"
          class="mt-2 block text-sm font-semibold transition-colors hover:text-primary"
        >
          {{ business.phoneDisplay }}
        </a>
        <a
          :href="`mailto:${business.email}`"
          class="mt-1 block text-sm text-ink-muted transition-colors hover:text-primary"
        >
          {{ business.email }}
        </a>
      </div>

      <div class="reveal text-center" style="--reveal-delay: 120ms">
        <span
          class="mx-auto flex h-14 w-14 items-center justify-center rounded-full border-2 border-primary text-primary transition-transform duration-300 hover:scale-110"
        >
          <MapPin class="h-6 w-6" />
        </span>
        <h3 class="mt-4 font-display text-lg font-extrabold italic uppercase">Lokalizacja</h3>
        <p class="mt-2 text-sm font-semibold">{{ business.address }}</p>
        <a
          href="#kontakt"
          class="mt-1 block text-sm text-ink-muted transition-colors hover:text-primary"
        >
          Zobacz mapę dojazdu
        </a>
      </div>

      <div class="reveal text-center" style="--reveal-delay: 240ms">
        <span
          class="mx-auto flex h-14 w-14 items-center justify-center rounded-full border-2 border-primary text-primary transition-transform duration-300 hover:scale-110"
        >
          <Clock class="h-6 w-6" />
        </span>
        <h3 class="mt-4 font-display text-lg font-extrabold italic uppercase">Godziny</h3>
        <p v-for="h in business.hours" :key="h.days" class="mt-1 text-sm text-ink-muted">
          <span class="font-semibold text-ink-foreground">{{ h.days }}:</span> {{ h.time }}
        </p>
      </div>
    </div>
    <div class="checkers h-4 w-full" />
  </section>
</template>
