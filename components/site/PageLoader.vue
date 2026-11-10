<script setup lang="ts">
import { Car } from 'lucide-vue-next'

defineProps<{ done?: boolean }>()
</script>

<template>
  <div
    class="fixed inset-0 z-[100] flex flex-col items-center justify-center gap-6 bg-ink transition-all"
    :class="done ? 'pageloader-leave pointer-events-none' : ''"
    role="status"
    aria-label="Ładowanie strony"
  >
    <span class="flex h-16 w-16 items-center justify-center rounded-full border-2 border-primary text-primary">
      <Car class="h-7 w-7" />
    </span>
    <p class="font-display text-sm font-extrabold italic uppercase tracking-widest text-ink-foreground">
      Auto-Serwis <span class="text-primary">Kowalski</span>
    </p>
    <!-- pasek ładowania w stylu checkers -->
    <div class="h-1.5 w-48 overflow-hidden rounded-full bg-ink-foreground/10">
      <div class="pageloader-bar h-full w-1/3 rounded-full bg-primary" />
    </div>
    <span class="pageloader-ring h-6 w-6 rounded-full border-2 border-primary border-t-transparent" />
  </div>
</template>
