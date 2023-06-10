

<template>
  <div id="wrapper">
    <Header/>
    <router-view />
  </div>
</template>

<script>
import Header from './components/Header.vue'

export default {
  name: 'App',
  components: {
    Header,
  },
}
</script>

<style lang="css">
@import './styles/bootstrap.min.css';
@import './assets/fonts/fontawesome-all.min.css';
/* @import './assets/fonts/simple-line-icons.min.css'; */
</style>
