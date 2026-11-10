// https://nuxt.com/docs/api/configuration/nuxt-config
import tailwindcss from '@tailwindcss/vite'

export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: false },
  css: ['~/assets/css/main.css'],
  vite: {
    plugins: [tailwindcss()]
  },
  ssr: true,
  runtimeConfig: {
    public: {
      // Ustaw w Vercel: NUXT_PUBLIC_SITE_URL=https://twoja-domena.vercel.app
      siteUrl:
        process.env.NUXT_PUBLIC_SITE_URL ||
        (process.env.VERCEL_URL ? `https://${process.env.VERCEL_URL}` : '')
    }
  },
  nitro: {
    prerender: {
      routes: ['/']
    }
  },
  routeRules: {
    '/': { prerender: true }
  },
  app: {
    head: {
      htmlAttrs: { lang: 'pl' },
      title: 'Auto-Serwis Kowalski – warsztat samochodowy w Lublinie',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        {
          name: 'description',
          content:
            'Mechanika, diagnostyka komputerowa i serwis klimatyzacji w Lublinie. Cennik i szybka wycena online.'
        },
        { name: 'author', content: 'Auto-Serwis Kowalski' },
        { name: 'theme-color', content: '#131316' },
        { property: 'og:title', content: 'Auto-Serwis Kowalski – warsztat samochodowy w Lublinie' },
        {
          property: 'og:description',
          content: 'Mechanika, diagnostyka i klimatyzacja. Sprawdź cennik i poproś o wycenę.'
        },
        { property: 'og:type', content: 'website' },
        { name: 'twitter:card', content: 'summary_large_image' },
        { name: 'msapplication-TileColor', content: '#131316' },
        { name: 'msapplication-config', content: '/browserconfig.xml' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
        { rel: 'icon', type: 'image/png', sizes: '16x16', href: '/favicon-16x16.png' },
        { rel: 'icon', type: 'image/png', sizes: '32x32', href: '/favicon-32x32.png' },
        { rel: 'apple-touch-icon', href: '/apple-touch-icon.png' },
        { rel: 'manifest', href: '/site.webmanifest' },
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        {
          rel: 'preconnect',
          href: 'https://fonts.gstatic.com',
          crossorigin: 'anonymous'
        },
        {
          rel: 'stylesheet',
          href: 'https://fonts.googleapis.com/css2?family=Sora:ital,wght@0,400;0,500;0,600;0,700;0,800;1,700;1,800&family=Manrope:wght@400;500;600;700&display=swap'
        }
      ]
    },
    pageTransition: { name: 'page', mode: 'out-in' }
  },
  typescript: { strict: true }
})
