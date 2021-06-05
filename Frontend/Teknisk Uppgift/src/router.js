import { createRouter, createWebHistory } from 'vue-router'

// Pages
import Main from './components/Main.vue'
import Login from './components/Login.vue'
import Secure from './components/Secure.vue'
import CreateAcc from './components/CreateAcc.vue'
import store from './store'

// Routing to components
const routes = [
    {
        path: '/',
        name: 'Main',
        component: Main,
    },
    {
        path: '/createAcc',
        name: 'CreateAcc',
        component: CreateAcc
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/secure',
        name: 'Secure',
        component: Secure,
        //check if user is authenticated... if false next(false) dont route else route to Secure.vue
        beforeEnter: (to, from, next) => {
            if(store.state.authenticated == false) {
                next(false);
            } else {
                next();
            }
        }
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router