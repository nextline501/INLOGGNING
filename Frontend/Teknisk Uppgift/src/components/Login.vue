<template>
    <div id="login">
        <h1>Login to Secure Page</h1>
        <input class="input-pw" type="text" name="email" v-model="input.email" placeholder="email" />
        <input class="input-pw" type="password" name="password" v-model="input.password" placeholder="Password" />
        <button class="btn btn-outline-secondary" type="button" v-on:click="login()">Login</button>
        <br>
        <button class="btn btn-outline-secondary" type="button" v-on:click="resetPassword()">Reset Password</button>
        <button class="btn btn-outline-secondary" type="button" v-on:click="goToCreateAcc()">Create Account</button>
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
                    password: this.input.password,
                    lastLoggedIn: Date.now(),
                    timesLoggedIn: 1,
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
                    }).catch((error) => {
                        if (error.response) {
                            // Request made and server responded
                            console.log(error.response.data);
                            console.log(error.response.status);
                            console.log(error.response.headers);
                            alert("wrong password or email")
                        } else if (error.request) {
                            // The request was made but no response was received
                            console.log(error.request);
                            alert("wrong password or email")
                        } else {
                            // Something happened in setting up the request that triggered an Error
                            console.log('Error', error.message);
                            alert("wrong password or email")
                        }
                    });
                
                }).catch((error) => {
                    if (error.response) {
                        // Request made and server responded
                        console.log(error.response.data);
                        console.log(error.response.status);
                        console.log(error.response.headers);
                        alert("wrong password or email")
                    } else if (error.request) {
                        // The request was made but no response was received
                        console.log(error.request);
                        alert("wrong password or email")
                        
                    } else {
                        // Something happened in setting up the request that triggered an Error
                        console.log('Error', error.message);
                        alert("wrong password or email")
                    }
                });
            },

            loginRouting(response) {
                //check response in loginRouting
                //Since i use JWT token the password will never reach frontend again
                //The password is verified in the back end so i just check if the email is correct from the response i get from @app.route('/api/secreteData', methods = ['GET'])
                console.log(response.data)
                if(this.input.email == response.data) {

                    //commit bool to store in router.js
                    this.$store.commit("setEmail", response.data);
                    this.$store.commit("setAuthentication", true);
                    this.$router.replace({ name: "Secure"});

                } else {
                    console.log("username is not correct");
                }
            },
            resetPassword(){
                this.$router.replace({ name: "ResetPassword"});
            },

            goToCreateAcc(){
                this.$router.replace({ name: "CreateAcc"})
            }
        }
    }
</script>

<style scoped>
    #login {
        width: auto;
        border: 1px solid #CCCCCC;
        background-color: #FFFFFF;
        margin: auto;
        margin-top: 200px;
        padding: 20px;
    }
</style>