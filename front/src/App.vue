<template>
  <!-- <Header /> -->
  <router-view />
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
@import './assets/fonts/line-awesome.min.css';
@import './assets/fonts/simple-line-icons.min.css';
</style>
<style lang="scss">
@import './styles/styles.scss';
</style>
