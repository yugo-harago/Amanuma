<template>
  <div id="wrapper">
    <!-- TODO: Make it visible -->
    <sidebar v-if="isLogged" />
    <!-- <sidebar /> -->
    <router-view />
  </div>
</template>

<script>
import Sidebar from './components/Sidebar.vue'
import { useSessionStore } from '@/stores/session'

export default {
  name: 'App',
  components: {
    Sidebar,
  },
  mounted() {
    const session = useSessionStore()
    return {
      isLogged: session.isLogged
    }
  },
}
</script>

<style lang="css">
@import './styles/bootstrap.min.css';
@import './assets/fonts/fontawesome-all.min.css';
/* @import './assets/fonts/simple-line-icons.min.css'; */
</style>
