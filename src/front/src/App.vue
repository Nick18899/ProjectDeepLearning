<template>
  <div id="app">
    <section class="container-fluid bg">
      <section class = "row justify-content-center">
        <section class = "col-12 col-sm-6 col-md-3">
    <form class = "form-container">
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

export default {
  name: 'app',
  components: {BaseNumberInput, BaseButton, BaseInput},
  data(){
    return {
      inputString: "",
      inputNumber: 1,
      outputString: "",
      tags: " "
    }
  },
  methods: {
    sendInputString: async function() {
      console.log("alpha")
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
        this.tags = jsn.hashtags
    }
  }

}
</script>


<style scoped>
  #app { font-family: Roboto, Helvetica, Arial, sans-serif; }
</style>
