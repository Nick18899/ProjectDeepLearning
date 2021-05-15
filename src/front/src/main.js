import ElementPlus from 'element-plus';
import App from "./App.vue";
import {createApp} from "vue";
import "./assets/sass/main.scss";
import 'element-plus/lib/theme-chalk/index.css';


createApp(App)
    .use(ElementPlus)
    .mount("#app");
