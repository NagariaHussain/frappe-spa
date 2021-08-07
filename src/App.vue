<template>
  <div>
    <div class="font-sans antialiased text-gray-900">
      <div class="flex h-screen overflow-hidden">
        <div class="flex flex-1 overflow-y-auto" :class="'sm:bg-gray-50'">
          <div class="flex-1">
            <div class="container mx-auto">
              <Navbar v-if="$auth.isLoggedIn" />
              <router-view />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";

export default {
  inject: ["$auth"],
  components: {
    Navbar,
  },
};
</script>
