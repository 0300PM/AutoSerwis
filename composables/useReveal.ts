/**
 * Globalny system "reveal on scroll".
 * Dodaj klasę `reveal` (+ opcjonalnie `reveal-left/right/zoom`
 * i `style="--reveal-delay:120ms"`) do dowolnego elementu,
 * a pojawi się z animacją, gdy wejdzie w viewport.
 */
export function useReveal() {
  let observer: IntersectionObserver | null = null
  let mutation: MutationObserver | null = null

  const observeAll = (root: ParentNode = document) => {
    if (!observer) return
    root.querySelectorAll('.reveal:not([data-reveal-bound])').forEach((el) => {
      el.setAttribute('data-reveal-bound', 'true')
      observer!.observe(el)
    })
  }

  onMounted(() => {
    if (!('IntersectionObserver' in window)) {
      document.querySelectorAll('.reveal').forEach((el) => el.classList.add('is-visible'))
      return
    }
    observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible')
            observer?.unobserve(entry.target)
          }
        }
      },
      { threshold: 0.12, rootMargin: '0px 0px -8% 0px' }
    )
    observeAll()
    // gdyby treść doszła później (np. po nawigacji)
    mutation = new MutationObserver((records) => {
      for (const record of records) {
        record.addedNodes.forEach((node) => {
          if (node instanceof Element) {
            if (node.classList.contains('reveal')) observeAll(node.parentNode ?? document)
            else if (node.querySelector) observeAll(node)
          }
        })
      }
    })
    mutation.observe(document.body, { childList: true, subtree: true })
  })

  onBeforeUnmount(() => {
    observer?.disconnect()
    mutation?.disconnect()
  })
}
