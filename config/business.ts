export const business = {
  name: 'Auto-Serwis Kowalski',
  tagline: 'Mechanika samochodowa • Diagnostyka • Serwis klimatyzacji',
  intro: 'Profesjonalny serwis samochodów osobowych i dostawczych.',
  city: 'Lublin',
  address: 'ul. Przykładowa 12, Lublin',
  phone: '+48 500 600 700',
  phoneDisplay: '500 600 700',
  email: 'kontakt@autoserwis.pl',
  hours: [
    { days: 'Poniedziałek – Piątek', time: '8:00 – 18:00' },
    { days: 'Sobota', time: '9:00 – 14:00' },
    { days: 'Niedziela', time: 'Nieczynne' }
  ],
  mapEmbed: 'https://www.google.com/maps?q=Lublin%20ul.%20Przykladowa%2012&output=embed',
  services: [
    {
      icon: 'wrench',
      name: 'Mechanika samochodowa',
      description: 'Naprawy zawieszenia, hamulców, układu kierowniczego itd.',
      price: 'od 100 zł'
    },
    {
      icon: 'scan',
      name: 'Diagnostyka komputerowa',
      description: 'Odczyt i analiza błędów ECU.',
      price: 'od 80 zł'
    },
    {
      icon: 'snowflake',
      name: 'Serwis klimatyzacji',
      description: 'Napełnianie, diagnostyka i odgrzybianie klimatyzacji.',
      price: 'od 150 zł'
    },
    {
      icon: 'tire',
      name: 'Wymiana opon',
      description: 'Wymiana, wyważanie i naprawa opon.',
      price: 'od 80 zł'
    },
    {
      icon: 'oil',
      name: 'Wymiana oleju',
      description: 'Olej + filtry + kontrola podstawowych parametrów.',
      price: 'od 120 zł + materiały'
    }
  ],
  advantages: [
    { title: 'Szybkie terminy', text: 'Nie musisz czekać tygodniami.' },
    { title: 'Doświadczenie', text: 'Wieloletnia praktyka w naprawie samochodów.' },
    { title: 'Uczciwe ceny', text: 'Przed rozpoczęciem naprawy informujemy o kosztach.' },
    { title: 'Gwarancja', text: 'Gwarancja na każdą wykonaną usługę.' }
  ],
  pricing: [
    { name: 'Diagnostyka komputerowa', price: '80 zł' },
    { name: 'Wymiana oleju', price: '120 zł' },
    { name: 'Wymiana klocków hamulcowych', price: '150 zł' },
    { name: 'Wymiana opon', price: '80 zł' },
    { name: 'Serwis klimatyzacji', price: '150 zł' }
  ],
  steps: [
    { no: '01', title: 'Kontaktujesz się z nami', text: 'Telefonicznie lub przez formularz.' },
    { no: '02', title: 'Ustalamy termin', text: 'Wybieramy dogodny dzień i godzinę.' },
    { no: '03', title: 'Diagnozujemy samochód', text: 'Informujemy Cię o znalezionych problemach.' },
    { no: '04', title: 'Wykonujemy naprawę', text: 'Po akceptacji kosztów przystępujemy do pracy.' }
  ],
  reviews: [
    { text: 'Szybka diagnoza i konkretna obsługa. Polecam.', author: 'Marek K.' },
    {
      text: 'Samochód zrobiony w jeden dzień. Cena zgodna z wcześniejszą wyceną.',
      author: 'Anna W.'
    },
    { text: 'Bardzo dobry kontakt i profesjonalna obsługa.', author: 'Piotr S.' }
  ]
} as const

export type Business = typeof business
