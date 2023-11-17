<template>
  <div id="wrapper">
    <sidebar v-if="isLoggedIn" />
    <router-view />
  </div>
</template>

<script>
import Sidebar from './components/Sidebar.vue'

export default {
  name: 'App',
  components: {
    Sidebar,
  },
  data() {
    return {
      isLoggedIn: false,
    };
  },
  created() {
    this.isLoggedIn = !!localStorage.getItem('token');
  },
}
</script>

<style lang="css">
@import './styles/bootstrap.min.css';
@import './assets/fonts/fontawesome-all.min.css';
/* @import './assets/fonts/simple-line-icons.min.css'; */
</style>
