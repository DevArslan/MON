

<template>
  <div>
    <button class="login-button block" :showModal=showModal id="show-modal" @click="showModal = true">Show Modal</button>
    <!-- use the modal component, pass in the prop -->
    <modal v-if="showModal" @close="showModal = false">
    <!--
      you can use custom content here to overwrite
      default content
    -->

  </modal>
</div>
</template>


<script>
  import modal from './components/modal.vue';


  export default {
    name: 'App',
    data () {
      return {
        showModal: false
      }
    },
    components: {
      modal
    },

  };
</script>

<style>

.login-button {

  border: 1px solid #00BFAE;
  background-color:#27293d;
  color: #fff;
  padding:0px;
}


</style>