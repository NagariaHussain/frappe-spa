<template>
  <form @submit.prevent="login">
    <input v-model="email" type="text" placeholder="email" required />
    <input v-model="password" type="password" placeholder="password" required />
    <button type="submit">Login</button>
  </form>
</template>

<script>
export default {
  inject: ["$auth"],
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    async login() {
      if (this.email && this.password) {
        let res = await this.$auth.login(this.email, this.password);
        if (res) {
          this.$router.push({ name: "Home" });
        }
      }
    },
  },
};
</script>
