<template>
  <div id="app">
    <section :class="{'container-fluid': true, 'bg2': !checked, 'bg': checked}">
      <section class = "row justify-content-center">
        <section class = "col-12 col-sm-6 col-md-3 w-50">
          <form :class = "{'form-container-light' :!checked, 'form-container-dark': checked}">
            <div class="form-group form-check1 form-switch">
              <BaseFlag @click="switchSendingMethod" id="flexSwitchCheckDefault"></BaseFlag>
              <label class="form-check-label" for="flexSwitchCheckDefault">{{sendingMethod}}</label>
            </div>
            <div class = "form-group">
              <label>{{info}}</label>
              <label style="margin-top: 10px">{{info}}</label>
              <p style="white-space: pre-line">{{ inputString }}</p>
            </div>
            <div class = "form-group">
              <BaseInput :value="typingString" @input = "stringCheck" type="string" v-model="typingString"/>
            </div>
            <BaseButton @click="sendInputString">Send Text/Path</BaseButton>
            <br>
            <div class="form-group form-check1 form-switch">
              <BaseFlag @click="switchOfTheme" id="flexSwitchCheckDefault"></BaseFlag>
              <label class="form-check-label" for="flexSwitchCheckDefault">{{theme}}</label>
            </div>
          </form>
        </section>
      </section>
    </section>
  </div>
</template>

<script>
import BaseInput from "@/components/BaseInput.vue";
import BaseButton from "@/components/BaseButton.vue";
import BaseFlag from "@/components/BaseFlag";

export default {
  name: 'app',
  components: {BaseFlag, BaseButton, BaseInput},
  data(){
    return {
      typingString: "",
      inputString: "",
      inputText: "",
      inputNumber: 1,
      outputString: "",
      info: "Enter path or text here:",
      method: false,
      tex: false,
      checked: false,
      sendingMethod: "Text",
      theme: "Click to choose the dark side"
    }
  },
  methods: {
    stringCheck: async function() {
      if(this.tex) {
        const resp = await fetch('http://localhost:5050/checkOfInput', {
          method: "POST",
          body: JSON.stringify({
            inputString: this.typingString,
            currentString: this.inputString
          }),
          headers: {
            "Content-Type": 'application/json'
          }
        })
        const jsn = await resp.json()
        this.typingString = jsn.newString
        console.log(this.inputString);
      }
      //this.inputString = this.inputString.replaceAll(/[./*+?^${}()|[\]\\]/g, "");
      //console.log(this.inputString);
    },

    sendInputString: async function() {
      if(this.sendingMethod === "Text")  {
        await fetch('http://localhost:5050/getText',{
          method: "POST",
          body: JSON.stringify({
            value: this.inputString,
            number: this.inputNumber
          }),
          headers: {
            "Content-Type": 'application/json'
          }
        })
      } else {
        await fetch('http://localhost:5050/sendPath',{
          method: "POST",
          body: JSON.stringify({
            value: this.typingString,
            number: this.inputNumber
          }),
          headers: {
            "Content-Type": 'application/json'
          }
        })
      }
      const resp = await fetch('http://localhost:5050/sendText', {
        method: "GET",
        headers: {
          "Content-Type": 'application/json'
        }
      })
      const jsn = await resp.json()
      console.log(jsn.newString)
      this.inputString = jsn.newString
      this.typingString = ""
      this.tex = true
    },
    switchSendingMethod: async function(){
      if(this.sendingMethod === "Text") {
        this.sendingMethod = "Path"
      }
      else{
        this.sendingMethod = "Text"
      }
      if(this.method){
        this.method = false
      }
      else{
        this.method = true
      }
    },
    switchOfTheme: async function(){
      if(this.theme === "Click to choose the dark side") {
        this.theme = "Click to choose the light side"
      }
      else{
        this.theme = "Click to choose the dark side"
      }
      if(this.checked){
        this.checked = false
      }
      else{
        this.checked = true
      }
      console.log(this.checked)
    }
  }

}
</script>


<style scoped>
#app { font-family: Roboto, Helvetica, Arial, sans-serif; }
</style>
