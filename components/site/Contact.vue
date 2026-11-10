<script setup lang="ts">
import { ref } from 'vue'
import { Clock, Mail, MapPin, Phone } from 'lucide-vue-next'
import { business } from '~/config/business'

const mapLoaded = ref(false)
</script>

<template>
  <section id="kontakt" class="mx-auto max-w-6xl scroll-mt-20 px-5 py-20">
    <p class="eyebrow reveal">Kontakt</p>
    <h2 class="section-title reveal mt-3" style="--reveal-delay: 80ms">{{ business.name }}</h2>

    <div class="mt-10 grid gap-8 lg:grid-cols-2">
      <div
        class="reveal reveal-left rounded-xl border border-border bg-card p-7 transition-all duration-300 hover:shadow-soft"
      >
        <ul class="space-y-5 text-sm">
          <li class="flex gap-3">
            <MapPin class="mt-0.5 h-5 w-5 shrink-0 text-primary" />
            <span>{{ business.address }}</span>
          </li>
          <li class="flex gap-3">
            <Phone class="mt-0.5 h-5 w-5 shrink-0 text-primary" />
            <a :href="`tel:${business.phone}`" class="transition-colors hover:text-primary">
              {{ business.phoneDisplay }}
            </a>
          </li>
          <li class="flex gap-3">
            <Mail class="mt-0.5 h-5 w-5 shrink-0 text-primary" />
            <a :href="`mailto:${business.email}`" class="transition-colors hover:text-primary">
              {{ business.email }}
            </a>
          </li>
          <li class="flex gap-3">
            <Clock class="mt-0.5 h-5 w-5 shrink-0 text-primary" />
            <div class="space-y-1">
              <p v-for="h in business.hours" :key="h.days">
                <span class="text-muted-foreground">{{ h.days }}: </span>
                {{ h.time }}
              </p>
            </div>
          </li>
        </ul>
        <a
          :href="`tel:${business.phone}`"
          class="mt-7 inline-flex h-12 w-full items-center justify-center gap-2 rounded-full bg-primary text-sm font-semibold text-primary-foreground transition-all duration-300 hover:-translate-y-0.5 hover:shadow-soft"
        >
          <Phone class="h-5 w-5" /> Zadzwoń
        </a>
      </div>

      <div class="reveal reveal-right relative min-h-72 overflow-hidden rounded-xl border border-border">
        <!-- skeleton loader mapy -->
        <div v-if="!mapLoaded" class="absolute inset-0 flex flex-col gap-3 bg-card p-6" aria-hidden="true">
          <div class="skeleton h-8 w-2/3 rounded-md" />
          <div class="skeleton h-4 w-1/2 rounded" />
          <div class="skeleton h-full min-h-48 flex-1 rounded-lg" />
          <p class="flex items-center gap-2 text-xs text-muted-foreground">
            <span class="pageloader-ring inline-block h-3.5 w-3.5 rounded-full border-2 border-primary border-t-transparent" />
            Ładowanie mapy…
          </p>
        </div>
        <iframe
          :title="`Mapa dojazdu – ${business.name}`"
          :src="business.mapEmbed"
          loading="lazy"
          class="h-full min-h-72 w-full"
          referrerpolicy="no-referrer-when-downgrade"
          @load="mapLoaded = true"
        />
      </div>
    </div>
  </section>
</template>
