<template>
  <div>
    <main>
      <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <div class="px-4 py-4 sm:px-0">
          <div>
            <p>Result: {{ pong }}</p>
          </div>
          <button
            class="bg-red-500 rounded px-2 py-2 text-white"
            @click="$resources.ping.reload()"
          >
            Ping
          </button>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {};
  },
  resources: {
    ping() {
      return {
        method: "frappe.ping",
      };
    },
  },
  computed: {
    pong() {
      if (!this.$resources.ping.data) {
        return "No data";
      }

      return this.$resources.ping.data;
    },
    isLoading() {
      return this.$resources.ping.loading;
    },
  },
};
</script>
