<template>
<div>
    <div id="secure">
        <h1>Secure Page</h1>
        <p>
            <button class="btn btn-outline-secondary" type="button" v-on:click="logout()">Logout</button>
        </p>
    </div>
    <div id="change">
        <h1>Change Password</h1>
        <p>
        <input type="text" name="email" v-model="changePasswordData.email" placeholder="email" />
        <input id="pw-input" type="password" name="password" v-model="changePasswordData.newPassword" placeholder="New Password" />
        <button class="btn btn-outline-secondary" type="button" v-on:click="changePw()">Change Password</button>
        </p>
    </div>
    <div id="delete">
        <h1>Delete Account</h1>
        <p>
        <input type="text" name="email" v-model="deleteAccountData.email1" placeholder="email" />
        <input type="text" name="email" v-model="deleteAccountData.email2" placeholder="confirm email" />
        <button class="btn btn-outline-secondary" type="button" v-on:click="deleteAcc()">Delete Account</button>
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
                    if(this.changePasswordData.email == store.state.email){
                        DataServices.sendNewPassword(changePasswordData).then(response => {
                            console.log(response)
                        }).catch((error) => {
                            alert(error);
                        })
                        alert("Password have changed")
                    } else {
                        alert("That is not your email")
                    }
                }
            },

            deleteAcc(){
                let deleteAccountData = {
                    email1: this.deleteAccountData.email1,
                    email2: this.deleteAccountData.email2,
                }
                if(this.deleteAccountData.email1 === this.deleteAccountData.email2) {
                    console.log("my stored data: " + store.state.email)
                    console.log("my delete account email: " + this.deleteAccountData.email1)
                    if(this.deleteAccountData.email1 == store.state.email){
                        DataServices.sendDeleteAccount(deleteAccountData).then(response => {
                            console.log(response)
                        }); 
                    } else {
                        alert("That is not your email")
                    }
                } else {
                    alert("emails don't match!")
                }
                this.logout();
            },

            logout(){
                this.$store.commit("setEmail", null);
                this.$store.commit("setAuthentication", false);
                this.$router.replace({ name: "Main"});
            }
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