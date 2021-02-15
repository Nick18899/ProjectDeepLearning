<template>
  <div id="app" class="col-md-4">
    <br>
    <labelAplpha>
      <label>Enter some text</label>
    </labelAplpha>
    <br>
    <inputAlpha>
      <BaseInput :value="inputString" type="string" v-model="inputString"/>
    </inputAlpha>
    <butAlpha>
      <BaseButton @click="sendInputString">Analyze</BaseButton>
    </butAlpha>
    <labelAlpha>
      <h3>Corresponding hash-tegs for your text:</h3>
      <br>
      <p style="white-space: pre-line">{{tags}}</p>
    </labelAlpha>
  </div>
</template>

<script>
import BaseInput from "@/components/BaseInput.vue";
import BaseButton from "@/components/BaseButton.vue";

export default {
  name: 'app',
  components: {BaseButton, BaseInput},
  data(){
    return {
      inputString: "",
      inputNumber: 0,
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
