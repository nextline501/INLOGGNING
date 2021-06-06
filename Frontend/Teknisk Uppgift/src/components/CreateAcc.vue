<template>
    <div id="login">
        <div v-if="!submited">
            <h1>Create Account</h1>
            <input type="text" name="email" v-model="userData.email" placeholder="set email" />
            <input id="pw-input" type="password" name="password" v-model="userData.password" placeholder="set password" />
            <button class="btn btn-outline-secondary" type="button" v-on:click="submit()">Submit</button>
            <h6>{{validEmail}}</h6><h6>{{vaildPassword}}</h6>
        </div>
        <div v-if="submited">
            <h1>Account Created Successfully!</h1>
            <p>
            <button class="btn btn-outline-secondary" type="button" v-on:click="goToLogin()">Login</button>
            <button class="btn btn-outline-secondary" type="button" v-on:click="goToHome()">Go to Homepage</button>
            </p>
        </div>
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
                },
                validEmail: "",
                vaildPassword: "",
                submited: false,
            }
        },
        methods: {
            eMailValidaton(){
                let email = this.userData.email
                let pattern = /^[^ ]+\.[a-z]{2,3}$/;
                console.log("pressing down email key")
                
                if(email.match(pattern)){
                    this.validEmail ="email is valid"
                    return true
                } else {
                    this.validEmail ="email is not valid"
                    return false
                }
            },

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

            submit(){
                if(this.eMailValidaton() == true && this.passwordValidation() == true){
                    let userData = {
                        id: null,
                        email: this.userData.email,
                        password: this.userData.password, 
                        created: Date.now(),
                        lastLoggedIn: null,
                        timesLoggedIn: 0,
                    }

                    DataServices.sendUserInfo(userData).then(response => {
                        console.log(response)
                    });
                    console.log("submited")
                    this.submited = true
                } else {
                    this.eMailValidaton()
                }
           }, 
            
            goToLogin(){
                this.$router.replace({ name: "Login"});
            },

            goToHome(){
                this.$router.replace({ name: "Main"});
            },
        },
        
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