<template>
<div>
    <br>
    <h3>OBS! Denna sida kommer man egentilgen åt genom en länk från sin mail</h3>
    <br>
    <div id="change">
        <h1>Reset Password</h1>
        <p>
        <input type="text" name="email" v-model="changePasswordData.email" placeholder="email" />
        <input id="pw-input" type="password" name="password" v-model="changePasswordData.newPassword" placeholder="New Password" />
        <button class="btn btn-outline-secondary" type="button" v-on:click="changePw()">Change Password</button>
        </p>
    </div>
</div>
</template>

<script>
import DataServices from '../services/DataServices'
import store from '../store'

    export default {
        name: 'Secure',
        data() {
            return {
                changePasswordData: {
                    email: "",
                    newPassword: "",
                },
                deleteAccountData: {
                    email1: "",
                    email2: "",
                },
            };
        },
    
        methods: {
            passwordValidation(){
                let p = document.getElementById('pw-input').value, errors = [];

                if (p.length < 8) {
                    errors.push("Your password must be at least 8 characters"); 
                }
                
                if (p.search(/[a-z]/) < 0) {                     
                    errors.push("Your password must contain at least one lowercase letter.")                     
                } 
                
                if (p.search(/[A-Z]/) < 0) {                         
                    errors.push("Your password must contain at least one uppercase letter.")                     
                }

                if (p.search(/[0-9]/) < 0) {
                    errors.push("Your password must contain at least one digit."); 
                }
                
                if (errors.length > 0) {
                    alert(errors.join("\n"));
                    return false;
                }
                return true;
            },

            changePw(){
                if(this.passwordValidation() == true) {
                    let changePasswordData = {
                    email: this.changePasswordData.email,
                    password: this.changePasswordData.newPassword,
                    }
                    if(this.changePasswordData.email == this.changePasswordData.email){
                        DataServices.sendNewPassword(changePasswordData).then(response => {
                            console.log(response)
                        }).catch((error) => {
                            alert(error);
                        })
                        alert("Password have changed")
                        this.$router.replace({ name: "Login"});
                    } else {
                        alert("That is not your email")
                    }
                }
            },
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
    #change {
        background-color: #FFFFFF;
        border: 1px solid #CCCCCC;
        padding: 20px;
        margin-top: 10px;
    }
    #delete {
        background-color: #FFFFFF;
        border: 1px solid #CCCCCC;
        padding: 20px;
        margin-top: 10px;
    }
</style>