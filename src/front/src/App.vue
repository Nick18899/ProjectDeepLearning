<template>
  <div id="app" class="col-md-4">
    <label>Enter some text</label>
    <br>
    <inputAlpha>
      <BaseInput :value="inputString" type="string" v-model="inputString"/>
    </inputAlpha>
    <butAlpha>
      <BaseButton @click="sendInputString">Analyze</BaseButton>
    </butAlpha>
    <br>

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
      inputString: ""
    }
  },
  methods: {
    sendInputString: async function() {

    }
  }

}
</script>


<style scoped>

</style>
