<template>
  <AppNavbar />
  <router-view />
</template>

<script>
import AppNavbar from './components/AppNavbar.vue'

export default {
  name: 'App',
  components: {
    AppNavbar,
  },
}
</script>

<style lang="css">
@import './styles/bootstrap.min.css';
@import './assets/fonts/line-awesome.min.css';
@import './assets/fonts/simple-line-icons.min.css';
</style>
<style lang="scss">
@import './styles/styles.scss';
</style>
