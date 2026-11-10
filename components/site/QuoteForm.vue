<script setup lang="ts">
import { computed, ref } from 'vue'
import { z } from 'zod'
import { toast } from 'vue-sonner'
import { Loader2, Send } from 'lucide-vue-next'
import { business } from '~/config/business'

const schema = z.object({
  name: z.string().trim().min(2, 'Podaj imię').max(80),
  phone: z
    .string()
    .trim()
    .min(7, 'Podaj numer telefonu')
    .max(20)
    .regex(/^[0-9+\s-]+$/, 'Nieprawidłowy numer telefonu'),
  brand: z.string().trim().min(1, 'Podaj markę').max(50),
  model: z.string().trim().min(1, 'Podaj model').max(50),
  year: z.string().trim().regex(/^(19|20)\d{2}$/, 'Podaj rok, np. 2015'),
  service: z.string().trim().min(1, 'Wybierz usługę'),
  message: z.string().trim().max(1000).optional()
})

type FormValues = {
  name: string
  phone: string
  brand: string
  model: string
  year: string
  service: string
  message: string
}

const empty: FormValues = {
  name: '',
  phone: '',
  brand: '',
  model: '',
  year: '',
  service: business.services[0].name,
  message: ''
}

const values = ref<FormValues>({ ...empty })
const errors = ref<Record<string, string>>({})
const submitting = ref(false)
const shakeKey = ref(0)

const hasErrors = computed(() => Object.keys(errors.value).length > 0)

function set<K extends keyof FormValues>(key: K, value: string) {
  values.value[key] = value
  if (errors.value[key]) {
    const next = { ...errors.value }
    delete next[key]
    errors.value = next
  }
}

async function onSubmit(event: Event) {
  event.preventDefault()
  const result = schema.safeParse(values.value)
  if (!result.success) {
    const fieldErrors: Record<string, string> = {}
    for (const issue of result.error.issues) {
      fieldErrors[String(issue.path[0])] = issue.message
    }
    errors.value = fieldErrors
    shakeKey.value += 1
    toast.error('Uzupełnij poprawnie formularz')
    return
  }
  errors.value = {}
  submitting.value = true
  // krótki loader — daje odczucie wysyłki, mimo że otwieramy klienta poczty
  await new Promise((resolve) => setTimeout(resolve, 800))
  const d = result.data
  const body = [
    `Imię: ${d.name}`,
    `Telefon: ${d.phone}`,
    `Samochód: ${d.brand} ${d.model} (${d.year})`,
    `Usługa: ${d.service}`,
    '',
    `Opis problemu: ${d.message || '-'}`
  ].join('\n')

  window.location.href = `mailto:${business.email}?subject=${encodeURIComponent(
    `Zapytanie o wycenę – ${d.brand} ${d.model}`
  )}&body=${encodeURIComponent(body)}`
  submitting.value = false
  toast.success('Otwieramy Twój program pocztowy z gotowym zapytaniem.')
}

const fields: Array<{
  key: 'name' | 'phone' | 'brand' | 'model' | 'year'
  label: string
  placeholder: string
  type?: string
}> = [
  { key: 'name', label: 'Imię', placeholder: 'Jan' },
  { key: 'phone', label: 'Telefon', placeholder: '500 600 700', type: 'tel' },
  { key: 'brand', label: 'Marka samochodu', placeholder: 'Volkswagen' },
  { key: 'model', label: 'Model', placeholder: 'Passat' },
  { key: 'year', label: 'Rok produkcji', placeholder: '2015' }
]
</script>

<template>
  <section id="wycena" class="border-y border-border bg-secondary/40">
    <div class="mx-auto max-w-3xl scroll-mt-20 px-5 py-20">
      <p class="eyebrow reveal">Poproś o wycenę</p>
      <h2 class="section-title reveal mt-3" style="--reveal-delay: 80ms">
        Opisz usterkę — oddzwonimy
      </h2>
      <p class="reveal mt-3 text-sm text-muted-foreground" style="--reveal-delay: 140ms">
        Wypełnij formularz, a przygotujemy wstępną wycenę naprawy.
      </p>

      <form
        :key="shakeKey"
        novalidate
        class="reveal mt-10 grid gap-5 sm:grid-cols-2"
        :class="{ 'field-error': hasErrors && shakeKey > 0 }"
        style="--reveal-delay: 180ms"
        @submit="onSubmit"
      >
        <div v-for="f in fields" :key="f.key" class="space-y-2">
          <label :for="f.key" class="text-sm font-medium leading-none">{{ f.label }}</label>
          <input
            :id="f.key"
            :type="f.type ?? 'text'"
            :value="values[f.key]"
            :placeholder="f.placeholder"
            :aria-invalid="Boolean(errors[f.key])"
            :disabled="submitting"
            class="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm shadow-xs outline-none transition-colors placeholder:text-muted-foreground focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 disabled:opacity-60"
            :class="errors[f.key] ? 'border-destructive' : ''"
            @input="set(f.key, ($event.target as HTMLInputElement).value)"
          />
          <p v-if="errors[f.key]" class="text-xs text-destructive">{{ errors[f.key] }}</p>
        </div>

        <div class="space-y-2">
          <label for="service" class="text-sm font-medium leading-none">Wybierz usługę</label>
          <select
            id="service"
            :value="values.service"
            :disabled="submitting"
            class="flex h-10 w-full rounded-md border border-input bg-background px-3 py-1 text-sm shadow-xs outline-none focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 disabled:opacity-60"
            @change="set('service', ($event.target as HTMLSelectElement).value)"
          >
            <option v-for="s in business.services" :key="s.name" :value="s.name">
              {{ s.name }}
            </option>
          </select>
        </div>

        <div class="space-y-2 sm:col-span-2">
          <label for="message" class="text-sm font-medium leading-none">Opis problemu</label>
          <textarea
            id="message"
            rows="5"
            maxlength="1000"
            :value="values.message"
            :disabled="submitting"
            placeholder="Np. stuka przednie zawieszenie przy nierównościach…"
            class="flex min-h-[80px] w-full rounded-md border border-input bg-background px-3 py-2 text-sm shadow-xs outline-none placeholder:text-muted-foreground focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 disabled:opacity-60"
            @input="set('message', ($event.target as HTMLTextAreaElement).value)"
          />
        </div>

        <button
          type="submit"
          :disabled="submitting"
          class="inline-flex h-12 items-center justify-center gap-2 rounded-full bg-primary px-8 text-sm font-semibold text-primary-foreground transition-all duration-300 hover:-translate-y-0.5 hover:shadow-soft disabled:translate-y-0 disabled:opacity-70 sm:col-span-2"
        >
          <Loader2 v-if="submitting" class="btn-spinner h-4 w-4" />
          <Send v-else class="h-4 w-4" />
          {{ submitting ? 'Przygotowywanie…' : 'Poproś o wycenę' }}
        </button>
      </form>
    </div>
  </section>
</template>
