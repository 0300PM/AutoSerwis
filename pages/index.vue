<script setup lang="ts">
import { business } from '~/config/business'

const title = 'Auto-Serwis Kowalski – mechanik Lublin, diagnostyka, klimatyzacja'
const description =
  'Warsztat samochodowy w Lublinie: mechanika, diagnostyka komputerowa, serwis klimatyzacji, opony i wymiana oleju. Sprawdź cennik i poproś o wycenę.'

// Absolutny URL strony — na Vercel ustaw NUXT_PUBLIC_SITE_URL,
// lokalnie fallback do localhost.
const siteUrl =
  useRuntimeConfig().public.siteUrl || (import.meta.dev ? 'http://localhost:3000' : '')
const canonical = siteUrl ? `${siteUrl}/` : '/'

useHead({
  title,
  link: [{ rel: 'canonical', href: canonical }],
  meta: [
    { name: 'description', content: description },
    { property: 'og:title', content: title },
    { property: 'og:description', content: description },
    { property: 'og:type', content: 'website' },
    { property: 'og:url', content: canonical },
    { property: 'og:image', content: `${siteUrl}/og-cover.jpg` },
    { property: 'og:image:width', content: '1200' },
    { property: 'og:image:height', content: '630' },
    {
      property: 'og:image:alt',
      content: 'Auto-Serwis Kowalski – mechanika, diagnostyka, klimatyzacja'
    },
    { name: 'twitter:card', content: 'summary_large_image' },
    { name: 'twitter:image', content: `${siteUrl}/og-cover.jpg` }
  ],
  script: [
    {
      type: 'application/ld+json',
      children: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'AutoRepair',
        name: business.name,
        telephone: business.phone,
        email: business.email,
        address: {
          '@type': 'PostalAddress',
          streetAddress: 'ul. Przykładowa 12',
          addressLocality: 'Lublin',
          addressCountry: 'PL'
        },
        openingHours: ['Mo-Fr 08:00-18:00', 'Sa 09:00-14:00']
      })
    }
  ]
})
</script>

<template>
  <div class="min-h-screen pb-24 md:pb-0">
    <SiteNavbar />
    <SiteHero />
    <main>
      <SiteInfoStrip />
      <SiteAbout />
      <SiteServices />
      <SiteAdvantages />
      <SitePricing />
      <SiteProcess />
      <SiteReviews />
      <SiteQuoteForm />
      <SiteContact />
    </main>
    <footer class="border-t border-border py-8 text-center text-xs text-muted-foreground">
      © {{ new Date().getFullYear() }} {{ business.name }} • {{ business.address }}
    </footer>
    <SiteCallBar />
  </div>
</template>
