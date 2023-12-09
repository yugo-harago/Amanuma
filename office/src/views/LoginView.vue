<template>
    <div class="container"
        style="position:absolute; left:0; right:0; top: 50%; transform: translateY(-50%); -ms-transform: translateY(-50%); -moz-transform: translateY(-50%); -webkit-transform: translateY(-50%); -o-transform: translateY(-50%);">
        <div class="row justify-content-center">
            <div class="col-md-10 col-lg-9 col-xl-9 col-xxl-7">
                <div class="card shadow-lg o-hidden border-0 my-5">
                    <div class="card-body p-0">
                        <div class="row">
                            <div class="col-lg-12">
                                <div class="p-5">
                                    <div class="text-center">
                                        <h4 class="text-dark mb-4">SDA天沼オフィス</h4>
                                    </div>
                                    <form class="user" @submit.prevent="_login()">
                                        <div class="mb-3"><input v-model="email" class="form-control form-control-user"
                                                type="email" id="email" aria-describedby="emailHelp" placeholder="メール"
                                                name="email" required=""></div>
                                        <div class="mb-3"><input v-model="password" class="form-control form-control-user"
                                                type="password" placeholder="パスワード" name="password" required=""></div>
                                        <div class="row mb-3">
                                            <p id="errorMsg" class="text-danger" style="display:none;">Paragraph</p>
                                        </div><button class="btn btn-primary d-block btn-user w-100" id="submitBtn"
                                            type="submit">ログイン</button>
                                        <hr>
                                    </form>
                                    <!-- <div class="text-center"><a class="small" href="forgot-password.html">Forgot
                                            Password?</a></div>
                                    <div class="text-center"><a class="small" href="register.html">Create an Account!</a>
                                    </div> -->
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
import { mapActions } from 'pinia'
import { useUserStore } from '@/stores/user'

export default {
    data() {
        return {
            email: '',
            password: '',
        };
    },
    methods: {
        ...mapActions(useUserStore, ['login']),
        async _login() {
            await this.login({ email: this.email, password: this.password });
            this.$router.push('/');  // Redirect to home page
        },
    },
};
</script>
  
<style scoped>
.container {
    position: absolute;
    left: 0;
    right: 0;
    top: 50%;
    transform: translateY(-50%);
    -ms-transform: translateY(-50%);
    -moz-transform: translateY(-50%);
    -webkit-transform: translateY(-50%);
    -o-transform: translateY(-50%);
}
</style>