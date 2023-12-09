import axios from 'axios'
import { defineStore } from 'pinia'


interface ModuleState {
    logged: boolean;
  }

export const useUserStore = defineStore('user', {
    state: (): ModuleState => ({
        logged: false,
    }),
    getters: {
        isLoggedIn(): boolean {
            return true;
        }
    },
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
        async checkLogin() {
            try {
                // const response = await axios.get('/api/check-login/');
                // this.logged = response.data.logged;
                this.logged = true;
            } catch (error) {
                console.error(error);
            }
        },
      async logout() {
        try {
            await axios.post('/api/logout/', {}, {
                headers: {
                    'Content-Type': 'application/json',
                }
            });
            localStorage.removeItem('token');
            this.logged = false;
        } catch (error) {
            console.error(error);
        }
      },
      onCreated() {
          this.checkLogin();
      }
    },
})