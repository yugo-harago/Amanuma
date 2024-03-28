import axios from 'axios'
import { defineStore } from 'pinia'
import router from '../router';

export const useSessionStore = defineStore("session", {
    state: () => ({
        token: localStorage.getItem('token'),
        user: undefined,
        isLogged: !!localStorage.getItem('token'),
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
              this.isLogged = true;
          } catch (error) {
              console.error(error);
          }
        },
        logout() {
            this.isLogged = false;
            localStorage.removeItem('token');
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