

<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container" v-bind:class = "{ContainerLong: active}">

          <div class="modal-header">

            <button @click = "showUnderlineUP = false, showUnderlineIn = true,active = false" v-bind:class = "{ActiveButton: showUnderlineIn}" >SIGN IN</button>

            <button @click = "showUnderlineIn = false, showUnderlineUP = true,active = true" v-bind:class = "{ActiveButton: showUnderlineUP}" >SIGN UP</button>
          </div>

          <div class="modal-body">
            <form action="" method="post" class="sign-in"    v-bind:class = "{SignInLeft: active}">
              <label>USERNAME</label>
              <input class="input-form" type="text" name="username" placeholder="">
              <label>PASSWORD</label>
              <input class="input-form" type="password" name="password" placeholder="">
            </form>

            <form action="" method="post" class="sign-up" v-bind:class = "{SignUpLeft: active}" >
              
              <label for="">EMAIL</label>
              <input class="input-form" type="text" name="email">
              <label for="">USERNAME</label>
              <input class="input-form" type="text" name="username">
              <label for="">PASSWORD</label>
              <input class="input-form" type="password" name="password">
              <label for="">CONFIRM PASSWORD</label>
              <input class="input-form" type="password" name="confirm-password">

            </form>
          </div>

          <div class="modal-footer">
            <slot name="footer">
              <button class="modal-default-button" @click="$emit('close')">
                Sign in
              </button>
            </slot>
          </div>

        </div>
      </div>
    </div>
  </transition>
</template>




<script type="text/x-template" id="modal-template">

  export default{
    props: ['showModal','active','showUnderlineUP','showUnderlineIn'],
}
</script>

<style >
  
  .ActiveButton{
    border-bottom: 1px solid #fff;
  }

  .sign-up{

    top:-168px;
    left:400px;
    position: relative;
    opacity: .0;
    transition:  ease transform .5s, opacity .5s ease; 

  }
  
  .sign-in{
    transition:  ease transform .5s, opacity .5s ease; 
  }
  
  .SignUpLeft{
    transform: translateX(-400px);
    opacity: 1;
  }

  .SignInLeft{
    transform: translateX(-400px);
    opacity: .0;

  }

  .input-form{
    border-radius: 20px;
    border: 1px solid #fff;

  }
  
  .modal-footer{

  }

  .modal-mask {
  padding-top: 6rem;
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  transition: opacity 0.01s ease;
}

.modal-wrapper {
  
}

.modal-container {
  height: 400px;
  overflow: hidden;
  width: 400px;
  margin: 0px auto;
  padding: 20px 30px;
  background: linear-gradient( #585E7F,#2E365E);
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, .33);
  transition: all .3s ease;

}
.ContainerLong{
    height: 600px;
  }

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}


.modal-header a:hover {
  border-bottom: 1px solid #fff;
}

.modal-body {
  margin: 20px 0 0 0;
  color: #fff;





}

.modal-default-button {
  float: right;
}

/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}

.input-form {
  width: 100%;
  background-color: #6D738E;
  border:0px;
  outline: none;
  padding-left: 15px;
}



.modal-body label {
  font-size: 16px;
  margin-left: 18px;
}
</style>