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
                    
                    //setting header with access_token, very important!
                    const authAxios = axios.create({
                        baseURL: "http://localhost:5000/api",
                        headers: {
                            Authorization: `Bearer ${response.data.access_token}`
                        }
                    });

                    authAxios.get("/secreteData").then(response => {
                        console.log(response);
                        this.loginRouting(response);
                    })
                });
            },

            loginRouting(response) {
                //check response in loginRouting
                //Since i use JWT token the password will never reach frontend again
                //The password is verified in the back end so i just check if the email is correct from the response i get from @app.route('/api/secreteData', methods = ['GET'])
                console.log(response.data)
                if(this.input.email == response.data) {

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