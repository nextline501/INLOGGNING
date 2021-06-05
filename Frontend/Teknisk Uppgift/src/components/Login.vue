<template>
    <div id="login">
        <h1>Login</h1>
        <input type="text" name="email" v-model="input.email" placeholder="email" />
        <input type="password" name="password" v-model="input.password" placeholder="Password" />
        <button type="button" v-on:click="login()">Login</button>
    </div>
</template>

<script>
import axios from 'axios'
    import DataServices from "../services/DataServices"

    export default {
        name: 'Login',
        data() {
            return {
                input: {
                    email: "",
                    password: ""
                },
                dataUpdate: {
                    lastLoggedIn: "", //time class
                    timesLoggedIn: "", //i++
                }
            }
        },
        methods: {
            login() {
                let inputData = {
                    email: this.input.email,
                    password: this.input.password
                }

                DataServices.sendLoginInfo(inputData).then(response => {
                    console.log("my token: ")
                    console.log(response.data.access_token)
                    
                    const authAxios = axios.create({
                        baseURL: "http://localhost:5000/api",
                        headers: {
                            Authorization: `Bearer ${response.data.access_token}`   
                        }
                    });
                    
                    useCallback(async () => {
                    try {
                        const result = await authAxios.get(`/secreteData`)
                        console.log(result);
                    } catch (error) {
                        console.log(error)
                    }
                    });
                });

                this.loginRouting();
            },

            loginRouting() {
                if(this.input.email == "" && this.input.password == "") {

                    //commit bool to store in router.js
                    this.$store.commit("setAuthentication", true);
                    this.$router.replace({ name: "Secure"});

                } else {
                    console.log("username is not correct");
                }
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