<template>
  <div id="app" class="col-md-4">
    <br>
    <labelAplpha>
      <label>Enter some text here:</label>
    </labelAplpha>
    <br>
    <inputAlpha>
      <BaseInput :value="inputString" type="string" v-model="inputString"/>
    </inputAlpha>
    <inputNumberAlpha>
      <BaseNumberInput :value="inputNumber"  type="number" v-model="inputNumber"/>
    </inputNumberAlpha>
    <butAlpha>
      <BaseButton @click="sendInputString">Analyze</BaseButton>
    </butAlpha>
    <br>
      <label style="margin-left: 20px; margin-top: 10px">Corresponding hashtags for your text:</label>
      <p style="white-space: pre-line; margin-left: 20px; margin-top: 10px">{{tags}}</p>
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
      tags: "1"
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

</style>
