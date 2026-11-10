<script setup lang="ts">
import { business } from '~/config/business'

const title = 'Auto-Serwis Kowalski – mechanik Lublin, diagnostyka, klimatyzacja'
const description =
  'Warsztat samochodowy w Lublinie: mechanika, diagnostyka komputerowa, serwis klimatyzacji, opony i wymiana oleju. Sprawdź cennik i poproś o wycenę.'

useHead({
  title,
  meta: [
    { name: 'description', content: description },
    { property: 'og:title', content: title },
    { property: 'og:description', content: description },
    { property: 'og:type', content: 'website' },
    { name: 'twitter:card', content: 'summary_large_image' }
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
