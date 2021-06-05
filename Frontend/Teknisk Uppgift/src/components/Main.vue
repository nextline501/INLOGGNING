<template>
    <div id="Main">
        <h1>Main</h1>
        <p>
            This is Main
        </p>
        <router-link to="/secure">
            <button>secure</button>
        </router-link>
        <router-link to="/login">
            <button>login</button>
        </router-link>
        <router-link to="/createAcc">
            <button>Create Account</button>
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