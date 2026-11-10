# garage-nuxt — Auto-Serwis Kowalski (Nuxt 3 + Tailwind + TypeScript)

Przepisana wersja strony z `C:/Users/anysz/Desktop/garage`
(TanStack Start + React) na **Nuxt 3 + Vue 3 + Tailwind CSS v4 + TypeScript**.
Układ i treści (UI/UX) zachowane 1:1 — dodane są tylko animacje i loadery.

## Start

```sh
cd garage-nuxt
npm install
npm run dev      # http://localhost:3000
npm run build    # produkcja (Nitro, node-server)
npm run preview
```

## Struktura

| Ścieżka | Opis |
|---|---|
| `app.vue` | layout root + PageLoader + Toaster |
| `pages/index.vue` | strona główna (wszystkie sekcje + SEO/JSON-LD) |
| `components/site/` | Navbar, Hero, InfoStrip, About, Services, Advantages, Pricing, Process, Reviews, QuoteForm, Contact, CallBar, PageLoader |
| `composables/useReveal.ts` | globalny reveal-on-scroll (IntersectionObserver) |
| `config/business.ts` | dane firmy (typowane, `as const`) |
| `assets/css/main.css` | design system + animacje/loadery |
| `assets/img/` | hero-workshop.jpg, about-shop.jpg |
| `error.vue` | strona błędu (404/500) po polsku |

## Co dodano względem oryginału (bez zmiany UI/UX)

- **PageLoader** — fullscreen loader z logo, paskiem ładowania i spinnerem, znika z animacją blur/fade po `window.load`.
- **Reveal on scroll** — każda sekcja/karta wjeżdża z fade+rise (IntersectionObserver, `useReveal`, stagger przez `--reveal-delay`, warianty left/right/zoom).
- **Hero** — Ken Burns na zdjęciu, kaskadowe `hero-rise` nagłówek → tagline → przyciski, pulsująca linia glow.
- **Navbar** — cień po scrollu, underline-animacja linków, wysuwane menu mobilne (w oryginale ikona nic nie robiła).
- **Karty usług** — gradientowa poświata `card-glow` na hover, rotacja ikony.
- **Opinie** — gwiazdki `star-pop` po wejściu w viewport.
- **Formularz** — spinner `Loader2` w przycisku podczas „wysyłki”, shake przy błędach, czyszczenie błędu pola przy wpisywaniu.
- **Mapa** — skeleton shimmer + spinner „Ładowanie mapy…” do czasu `load` iframa.
- **CallBar (mobile)** — animowane wejście `callbar-rise`.
- **Przejścia stron** Nuxt `page` + `prefers-reduced-motion` dla wszystkich animacji.
- Lang zmieniony na `pl`, strona 404 po polsku, SEO/JSON-LD przeniesione do `useHead`.
