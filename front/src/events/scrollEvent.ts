import { onMounted, onUnmounted } from 'vue'

export function useScrollEvent(handler) {
  const handleScroll = () => {
    handler(window.scrollY)
  }

  onMounted(() => {
    window.addEventListener('scroll', handleScroll)
  })

  onUnmounted(() => {
    window.removeEventListener('scroll', handleScroll)
  })
}
