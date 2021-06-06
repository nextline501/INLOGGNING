App

<template>
<div>
  <Navbar></Navbar>

  <router-view></router-view>
  
</div>
</template>

<script>
import Navbar from './components/Navbar.vue'

export default {
  name: 'app',
  components: {Navbar}
}
</script>


<style>

#app {
  font-family: 'Open Sans', sans-serif;
  text-align: center;
  color: #000000;
  margin-top: 0px;
}

a.nav-link{
  padding: 0px;
}

</style>