<template>
	<div>
		<main>
			<div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
				<div class="px-4 py-4 sm:px-0">
					<div>
						<p>$resources.ping.loading: {{ $resources.ping.loading }}</p>
						<p>loading computed: {{ isLoading }}</p>
						<p>pong computed property: {{ pong }}</p>
						<p>this.$resources.ping.data: {{ this.$resources.ping.data }}</p>
					</div>
					<button
						class="bg-red-500 rounded px-2 py-2 text-white"
						@click="$resources.ping.reload()"
					>
						Click me
					</button>
				</div>

				<div>User is logged in: {{ this.$auth.isLoggedIn }}</div>
			</div>
		</main>
	</div>
</template>

<script>

export default {
	name: 'Home',
	inject: ['$auth', '$socket'],
	data() {
		return {};
	},
	resources: {
		ping() {
			return {
				method: 'doppio.api.main.ping',
			};
		},
	},
	computed: {
		pong() {
			if (!this.$resources.ping.data) {
				return 'No data';
			}

			return this.$resources.ping.data;
		},
		isLoading() {
			return this.$resources.ping.loading;
		},
	},
};
</script>
