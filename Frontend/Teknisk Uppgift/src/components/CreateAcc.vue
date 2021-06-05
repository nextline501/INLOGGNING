<template>
    <div id="login">
        <h1>Create Acc</h1>
        <input type="text" name="email" v-model="userData.email" placeholder="set email" />
        <input type="password" name="password" v-model="userData.password" placeholder="set password" />
        <button type="button" v-on:click="submit()">Submit</button>
    </div>
</template>

<script>
    import DataServices from "../services/DataServices"
    
    export default {
        name: 'CreateAcc',
        data() {
            return {
                userData: {
                    id: null,
                    email: "", //set by user 
                    password: "", //set by user 
                    created: "", //time class
                    lastLoggedIn: "", //time class
                    timesLoggedIn: "", //i++
                }
            }
        },
        methods: {
            submit(){
                let userData = {
                    id: null,
                    email: this.userData.email,
                    password: this.userData.password, 
                    created: Date.now(),
                    lastLoggedIn: null,
                    timesLoggedIn: null,
                }

                DataServices.sendUserInfo(userData).then(response => {
                    console.log(response)
                });

                console.log("submited")
            }
        }
    }
</script>

<style scoped>
    #login {
        width: 500px;
        border: 1px solid #CCCCCC;
        background-color: #FFFFFF;
        margin: auto;
        margin-top: 200px;
        padding: 20px;
    }
</style>