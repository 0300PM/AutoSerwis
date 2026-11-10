<script setup lang="ts">
import { Quote, Star } from 'lucide-vue-next'
import { business } from '~/config/business'
</script>

<template>
  <section class="mx-auto max-w-6xl px-5 py-20">
    <p class="eyebrow reveal">Opinie</p>
    <h2 class="section-title reveal mt-3" style="--reveal-delay: 80ms">Co mówią kierowcy</h2>
    <div class="mt-10 grid gap-5 md:grid-cols-3">
      <figure
        v-for="(review, i) in business.reviews"
        :key="review.author"
        class="reveal rounded-xl border border-border bg-card p-7 transition-all duration-300 hover:-translate-y-1 hover:shadow-soft"
        :style="{ '--reveal-delay': `${i * 120}ms` }"
      >
        <Quote class="h-6 w-6 text-primary/50" />
        <div class="mt-4 flex gap-1 text-primary">
          <Star
            v-for="n in 5"
            :key="n"
            class="star-pop h-4 w-4 fill-current"
            :style="{ '--star-delay': `${n * 90}ms` }"
          />
        </div>
        <blockquote class="mt-4 text-sm leading-relaxed">„{{ review.text }}”</blockquote>
        <figcaption class="mt-4 text-xs uppercase tracking-widest text-muted-foreground">
          {{ review.author }}
        </figcaption>
      </figure>
    </div>
  </section>
</template>
