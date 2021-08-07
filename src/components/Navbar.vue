<template>
    <div class="flex justify-between p-3">
        <h2>
            Dashboard
        </h2>

        <button @click="$auth.logout" class="p-2 bg-blue-700 text-white">Sign Out</button>
    </div>
</template>

<script>
export default {
    inject: ['$auth']
}
</script>