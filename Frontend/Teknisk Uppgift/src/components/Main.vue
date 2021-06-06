<template>
    <div id="Main">
        <h1>Main</h1>
        <p>
            This is Main
        </p>
        <router-link to="/secure">
            <button class="btn btn-outline-secondary">Test link to Secure Page (should not work - login needed)</button>
        </router-link>
    </div>
</template>

<script>
    export default {
        name: 'Main',
        data() {
            return {};
        }
    }
</script>

<style scoped>
    #secure {
        background-color: #FFFFFF;
        border: 1px solid #CCCCCC;
        padding: 20px;
        margin-top: 10px;
    }
</style>