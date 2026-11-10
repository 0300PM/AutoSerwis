<script setup lang="ts">
import { Phone, Send } from 'lucide-vue-next'
import { business } from '~/config/business'
</script>

<template>
  <div
    class="callbar-rise fixed inset-x-0 bottom-0 z-50 border-t border-border bg-background/95 p-3 backdrop-blur md:hidden"
  >
    <div class="flex gap-2">
      <a
        :href="`tel:${business.phone}`"
        class="inline-flex h-12 flex-1 items-center justify-center gap-2 rounded-full bg-primary text-base font-semibold text-primary-foreground transition-transform active:scale-95"
      >
        <Phone class="h-5 w-5" /> Zadzwoń
      </a>
      <a
        href="#wycena"
        class="inline-flex h-12 flex-1 items-center justify-center gap-2 rounded-full border border-input bg-background text-base font-semibold transition-transform active:scale-95"
      >
        <Send class="h-4 w-4" /> Wycena
      </a>
    </div>
  </div>
</template>
