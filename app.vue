<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { Toaster } from 'vue-sonner'

const loading = ref(true)
const leaving = ref(false)

useReveal()

onMounted(() => {
  // loader znika po załadowaniu strony (min. czas dla efektu)
  const hide = () => {
    leaving.value = true
    setTimeout(() => {
      loading.value = false
    }, 550)
  }
  if (document.readyState === 'complete') {
    setTimeout(hide, 600)
  } else {
    window.addEventListener('load', () => setTimeout(hide, 600), { once: true })
    // awaryjnie — gdyby event load już przeszedł
    setTimeout(() => {
      if (loading.value && !leaving.value) hide()
    }, 3500)
  }
})
</script>

<template>
  <div>
    <SitePageLoader v-if="loading" :done="leaving" />
    <NuxtPage />
    <Toaster position="top-center" rich-colors close-button />
  </div>
</template>
