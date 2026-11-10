<script setup lang="ts">
import type { NuxtError } from '#app'

defineProps<{ error: NuxtError }>()

const handleClear = () => clearError({ redirect: '/' })
</script>

<template>
  <div class="flex min-h-screen items-center justify-center bg-background px-4">
    <div class="max-w-md text-center">
      <h1 class="text-7xl font-bold text-foreground">
        {{ error?.statusCode === 404 ? '404' : 'Ups' }}
      </h1>
      <h2 class="mt-4 text-xl font-semibold text-foreground">
        {{ error?.statusCode === 404 ? 'Nie znaleziono strony' : 'Coś poszło nie tak' }}
      </h2>
      <p class="mt-2 text-sm text-muted-foreground">
        {{
          error?.statusCode === 404
            ? 'Strona, której szukasz, nie istnieje lub została przeniesiona.'
            : 'Spróbuj odświeżyć stronę lub wróć na stronę główną.'
        }}
      </p>
      <div class="mt-6 flex flex-wrap justify-center gap-2">
        <button
          class="inline-flex items-center justify-center rounded-md bg-primary px-4 py-2 text-sm font-medium text-primary-foreground transition-colors hover:bg-primary/90"
          @click="handleClear"
        >
          Wróć na stronę główną
        </button>
      </div>
    </div>
  </div>
</template>
