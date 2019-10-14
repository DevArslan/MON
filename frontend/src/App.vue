

<template>
  <div>
    <button class="login-button " :showModal=showModal id="show-modal" @click="showModal = true">Log in</button>
    <!-- use the modal component, pass in the prop -->
    <modal v-if="showModal" @close="showModal = false">
    


  </modal>
</div>
</template>


<script>
  import modal from './components/modal.vue';

  export default {
    name: 'App',
    data () {
      return {
        showModal: false,
        active: false,
        showUnderlineIn: false,
        showUnderlineUP:false
      }
    },
    components: {
      modal,
    },

  };
</script>

<style>

.login-button {

  box-shadow: 0px 1px 20px 0px rgba(0,0,0,0.5);
  border: 1px solid #00BFAE;
  background-color:#27293d;
  color: #fff;
  padding:7px;
  border-radius: 5px;
  font-size:20px;
}


</style>