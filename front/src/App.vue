<template>
  <AppNavbar />
  <div style="height: 65px"></div>
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

<style lang="css" scoped>
@import './styles/bootstrap.min.css';
@import './styles/styles.css';
@import './styles/index.css';
@import './styles/untitled.css';
@import './styles/worship.css';
@import './assets/fonts/line-awesome.min.css';
@import './assets/fonts/simple-line-icons.min.css';
</style>
