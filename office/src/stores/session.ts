import axios from 'axios'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router';

export const useSessionStore = defineStore("session", {
    state: () => ({
        token: localStorage.getItem('token'),
        user: undefined,
        redirectTo: undefined,
        isServiceUnavailable: false,
        isServerError: false
    }),
    actions: {
        async login(payload: { email: string, password: string }) {
          try {
              const response = await axios.post('/api/login/', payload, {
                    headers: {
                        'Content-Type': 'application/json',
                    }
              });
              // TODO: use HttpOnly cookies
              localStorage.setItem('token', response.data.token);
              this.logged = true;
          } catch (error) {
              console.error(error);
          }
        },
        logout() {
            const router = useRouter();
            router.push('/login');
        },
        setLoginState(token: string, user: User) {
            this.token = token;
            this.user = user;
            axios.defaults.common.Authorization = "JWT " + token;
        },
        setLogoutState() {
            this.token = null;
            this.user = undefined;
            delete axios.defaults.common.Authorization;
        },
        setRedirectTo(to: RouteLocationNormalized| undefined) {
            this.redirectTo = to
        },
        resetRedirectTo() {
            this.redirectTo = undefined
        },
        refresh() {
            return axios.post ('api/token/refresh/', {
                token: this.token
            })
        },

    }
})