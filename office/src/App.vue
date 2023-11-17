<template>
  <div id="wrapper">
    <sidebar />
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
}
</script>

<style lang="css">
@import './styles/bootstrap.min.css';
@import './assets/fonts/fontawesome-all.min.css';
/* @import './assets/fonts/simple-line-icons.min.css'; */
</style>
