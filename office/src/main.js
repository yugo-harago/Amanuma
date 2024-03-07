import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import axios from 'axios'
import { useSessionStore } from '@/stores/session'

const pinia = createPinia()
const app = createApp(App)
app.use(router)
app.use(pinia)
app.mount('#app')

const sessionStore = useSessionStore();

axios.interceptors.request.use(
    async (config) => {
        if (config.url !== 'api/token/refresh/') {
            await sessionStore.refresh().then((res) => {
                console.log(res)
            }, (error) => {
                sessionStore.logout()
            })
        }
        return config
    },
    (error) => {
        return Promise.reject(error)
    },
);

axios.interceptors.response.use(
    (response) => {
        return response;
    },
    (error) => {
        const status = error?.response?.status;
        
        if (status === 401) {
            // logout
        } else if (status === 503) {
            // service unavailable
        } else if (status === 400) {
            // raise error
        }

        return Promise.reject(error)
    }
)