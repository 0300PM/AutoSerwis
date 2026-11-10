<script setup lang="ts">
import { Check, Phone } from 'lucide-vue-next'
import { business } from '~/config/business'
import aboutImage from '~/assets/img/about-shop.jpg'

const bullets = [
  'Bezpłatna wstępna ocena usterki',
  'Oryginalne i zamienniki na życzenie',
  'Auta osobowe i dostawcze',
  'Wycena przed rozpoczęciem prac',
  'Gwarancja na części i robociznę',
  'Krótkie terminy realizacji'
]
</script>

<template>
  <section class="mx-auto max-w-6xl px-5 py-20">
    <div class="grid items-center gap-10 lg:grid-cols-2">
      <div
        class="reveal reveal-left group overflow-hidden rounded-2xl border border-border"
      >
        <img
          :src="aboutImage"
          alt="Mechanik pracujący przy silniku samochodu"
          loading="lazy"
          width="1200"
          height="900"
          class="h-full w-full object-cover transition-transform duration-700 ease-out group-hover:scale-105"
        />
      </div>
      <div class="reveal reveal-right">
        <p class="eyebrow">O warsztacie</p>
        <h2 class="section-title mt-3">Jakość w nowym standardzie</h2>
        <p class="mt-4 text-muted-foreground">
          {{ business.name }} to lokalny warsztat prowadzony przez mechaników z wieloletnim
          doświadczeniem. Łączymy nowoczesną diagnostykę komputerową ze starą szkołą rzetelnej
          roboty — każde auto traktujemy jak własne.
        </p>
        <ul class="mt-6 grid gap-3 sm:grid-cols-2">
          <li
            v-for="(b, i) in bullets"
            :key="b"
            class="reveal flex items-start gap-2 text-sm"
            :style="{ '--reveal-delay': `${i * 70}ms` }"
          >
            <Check class="mt-0.5 h-4 w-4 shrink-0 text-primary" />
            {{ b }}
          </li>
        </ul>
        <a
          :href="`tel:${business.phone}`"
          class="mt-8 inline-flex h-12 items-center gap-2 rounded-full bg-primary px-8 font-semibold text-primary-foreground transition-all duration-300 hover:-translate-y-0.5 hover:shadow-soft"
        >
          <Phone class="h-5 w-5" /> Skontaktuj się
        </a>
      </div>
    </div>
  </section>
</template>
