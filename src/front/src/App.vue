<template>
  <div id="app">
    <section :class="{'container-fluid': true, 'bg2': !checked, 'bg': checked}">
      <section class = "row justify-content-center">
        <section class = "col-12 col-sm-6 col-md-3 w-50">
          <form :class = "{'form-container-light' :!checked, 'form-container-dark': checked}">
            <div class = "form-group">
              <label>Enter some text here:</label>
            </div>
            <div class = "form-group">
              <BaseInput :value="inputString" type="string" v-model="inputString"/>
            </div>
            <div class = "form-group">
              <BaseNumberInput :value="inputNumber"  type="number" v-model="inputNumber"/>
            </div>
            <BaseButton @click="sendInputString">Analyze</BaseButton>
            <br>
            <label style="margin-top: 10px">Corresponding hashtags for your text:</label>
            <p style="white-space: pre-line">{{tags}}</p>
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
import BaseNumberInput from "@/components/BaseNumberInput";
import BaseFlag from "@/components/BaseFlag";

export default {
  name: 'app',
  components: {BaseFlag, BaseNumberInput, BaseButton, BaseInput},
  data(){
    return {
      inputString: "",
      inputNumber: 1,
      outputString: "",
      tags: " ",
      checked: false,
      theme: "Click to choose the dark side"
    }
  },
  methods: {
    sendInputString: async function() {
      //console.log("alpha")
      const resp = await fetch('http://localhost:5050/gettingTags',{
        method: "POST",
        body: JSON.stringify({
          value: this.inputString,
          number: this.inputNumber
        }),
        headers: {
          "Content-Type": 'application/json'
        }
      })
      const jsn = await resp.json()
      this.tags = jsn.hashtags.toString()
    },
    switchOfTheme: async function(){
      if(this.theme == "Click to choose the dark side") {
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
