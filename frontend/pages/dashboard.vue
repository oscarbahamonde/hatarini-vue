<template>
  <div v-if="this.$store.state.user" class="p-4">
    <h1 class="text-xl font-sans">Bienvenido! {{ this.$store.state.user.email }}</h1>
    <button @click="logout" class="btn btn-error my-4">Logout</button>
    <Profile />
  </div>
  <div v-else><Login /></div>
</template>
<script>
export default {
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    logout() {
      this.$store.dispatch("LogOut");
    },
  },
};
</script>
