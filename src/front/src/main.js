import {createApp} from "vue";
import App from "./App.vue";
import 'mdb-vue-ui-kit/css/mdb.min.css'
import "./assets/sass/main.scss";
import ElementPlus from 'element-plus';
import 'element-plus/lib/theme-chalk/index.css';


createApp(App)
    .use(ElementPlus)
    .mount("#app");
