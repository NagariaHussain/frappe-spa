<template>
  <div>
    <div class="font-sans antialiased text-gray-900">
      <div class="flex h-screen overflow-hidden">
        <div class="flex flex-1 overflow-y-auto" :class="'sm:bg-gray-50'">
          <div class="flex-1">
            <div class="container mx-auto">
              <router-view />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  inject: ["$auth"],
};
</script>
