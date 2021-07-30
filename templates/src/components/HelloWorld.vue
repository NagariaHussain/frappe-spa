<template>
  <h1>{{ title }}</h1>
</template>

<script>
export default {
  data() {
    return {
      friends: ["Frappe Framework", "Vue"],
    };
  },
  computed: {
    title() {
      return friends[0] + " and " + friends[1];
    },
  },
};
</script>
