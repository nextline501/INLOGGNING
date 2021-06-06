import { createApp } from 'vue';
import App from './App.vue';

//import css from bootstrap 
import "bootstrap/dist/css/bootstrap.min.css";

import router from './router.js';
import store from './store.js';

createApp(App).use(router).use(store).mount('#app')

