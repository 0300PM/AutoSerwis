<script setup lang="ts">
import { Car, Menu, Phone, X } from 'lucide-vue-next'
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { business } from '~/config/business'

const links = [
  { label: 'Usługi', href: '#uslugi' },
  { label: 'Cennik', href: '#cennik' },
  { label: 'Jak działamy', href: '#proces' },
  { label: 'Kontakt', href: '#kontakt' }
]

const open = ref(false)
const scrolled = ref(false)

const onScroll = () => {
  scrolled.value = window.scrollY > 24
}

onMounted(() => {
  window.addEventListener('scroll', onScroll, { passive: true })
  onScroll()
})
onBeforeUnmount(() => window.removeEventListener('scroll', onScroll))
</script>

<template>
  <nav
    class="sticky top-0 z-40 border-b bg-ink/90 backdrop-blur transition-all duration-300"
    :class="scrolled ? 'border-primary/30 shadow-soft' : 'border-border/60'"
  >
    <div class="mx-auto grid max-w-6xl grid-cols-[1fr_auto_1fr] items-center gap-4 px-5 py-4">
      <div
        class="hidden items-center gap-8 text-sm font-semibold uppercase tracking-wide text-ink-muted lg:flex"
      >
        <a
          v-for="link in links"
          :key="link.href"
          :href="link.href"
          class="nav-link transition-colors hover:text-primary"
        >
          {{ link.label }}
        </a>
      </div>
      <button
        class="flex w-10 items-center justify-start lg:hidden"
        :aria-label="open ? 'Zamknij menu' : 'Otwórz menu'"
        :aria-expanded="open"
        @click="open = !open"
      >
        <component :is="open ? X : Menu" class="h-5 w-5 text-ink-muted" />
      </button>

      <a href="#top" class="flex items-center justify-center gap-3">
        <span
          class="flex h-11 w-11 items-center justify-center rounded-full border-2 border-primary bg-ink text-primary"
        >
          <Car class="h-5 w-5" />
        </span>
        <span
          class="font-display text-sm font-extrabold italic uppercase leading-tight tracking-tight text-ink-foreground"
        >
          Auto-Serwis
          <br />
          <span class="text-primary">Kowalski</span>
        </span>
      </a>

      <div class="flex justify-end">
        <a
          :href="`tel:${business.phone}`"
          class="hidden items-center gap-2 rounded-full bg-primary px-6 py-2 text-sm font-semibold text-primary-foreground transition-all hover:-translate-y-0.5 hover:shadow-soft sm:inline-flex"
        >
          <Phone class="h-4 w-4" /> {{ business.phoneDisplay }}
        </a>
      </div>
    </div>

    <!-- mobilne menu -->
    <Transition
      enter-active-class="transition-all duration-300 ease-out"
      enter-from-class="opacity-0 -translate-y-2"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition-all duration-200 ease-in"
      leave-from-class="opacity-100 translate-y-0"
      leave-to-class="opacity-0 -translate-y-2"
    >
      <div v-if="open" class="border-t border-border/60 px-5 py-4 lg:hidden">
        <div class="flex flex-col gap-1">
          <a
            v-for="(link, i) in links"
            :key="link.href"
            :href="link.href"
            :style="{ transitionDelay: `${i * 60}ms` }"
            class="rounded-lg px-3 py-3 text-sm font-semibold uppercase tracking-wide text-ink-muted transition-colors hover:bg-secondary hover:text-primary"
            @click="open = false"
          >
            {{ link.label }}
          </a>
        </div>
      </div>
    </Transition>
  </nav>
</template>
