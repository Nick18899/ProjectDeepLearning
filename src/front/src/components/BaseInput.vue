<template>
  <textarea
      @input="$emit('update:modelValue', $event.target.value)"
      class="form-control">
  </textarea>

</template>

<script>
export default {
  name: "BaseInput",
}
</script>

<style scoped>

</style>
