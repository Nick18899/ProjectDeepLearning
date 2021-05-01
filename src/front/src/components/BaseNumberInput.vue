<template>
  <input
      @input="$emit('update:modelValue', $event.target.value)"
      v-model="age"
      min="1"
      max="100"
      placeholder="Enter number"
      class="form-control"
  />
</template>

<script>
export default {
name: "BaseNumberInput"
}
</script>

<style scoped>

</style>
