<template>
  <div id="wrapper">
    <!-- TODO: Make it visible -->
    <sidebar v-if="isLoggedIn" />
    <router-view />
  </div>
</template>

<script>
import Sidebar from './components/Sidebar.vue'
import { mapState } from 'pinia'
import { useUserStore } from '@/stores/user'

export default {
  name: 'App',
  components: {
    Sidebar,
  },
  data() {
  },
  state: {
    ...mapState(useUserStore, ['isLoggedIn']),
  },
}
</script>

<style lang="css">
@import './styles/bootstrap.min.css';
@import './assets/fonts/fontawesome-all.min.css';
/* @import './assets/fonts/simple-line-icons.min.css'; */
</style>
