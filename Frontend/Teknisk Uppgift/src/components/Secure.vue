<template>
<div>
    <div id="secure">
        <h1>Secure Area</h1>
        <p>
            This is a secure area
        </p>
    </div>
    <div id="change">
        <h1>Change Password</h1>
        <p>
        <input type="text" name="email" v-model="changePasswordData.email" placeholder="email" />
        <input type="password" name="password" v-model="changePasswordData.newPassword" placeholder="New Password" />
        <button type="button" v-on:click="changePw()">Change Password</button>
        </p>
    </div>
    <div id="delete">
        <h1>Delete Account</h1>
        <p>
        <input type="text" name="email" v-model="deleteAccountData.email1" placeholder="email" />
        <input type="text" name="email" v-model="deleteAccountData.email2" placeholder="confirm email" />
        <button type="button" v-on:click="deleteAcc()">Delete Account</button>
        </p>
    </div>
</div>
</template>

<script>
import DataServices from '../services/DataServices'
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
                }
            };
        },
        methods: {
            changePw(){
                let changePasswordData = {
                    email: this.changePasswordData.email,
                    password: this.changePasswordData.newPassword,
                }

                DataServices.sendNewPassword(changePasswordData).then(response => {
                    console.log(response)
                })
            }, 

            deleteAcc(){
                let deleteAccountData = {
                    email1: this.deleteAccountData.email1,
                    email2: this.deleteAccountData.email2,
                }
                if(this.deleteAccountData.email1 === this.deleteAccountData.email2) {
                    DataServices.sendDeleteAccount(deleteAccountData).then(response => {
                        console.log(response)
                    }); 
                } else {
                    alert("emails don't match!")
                }
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