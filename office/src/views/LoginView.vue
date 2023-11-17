<template>
    <div class="container" style="position:absolute; left:0; right:0; top: 50%; transform: translateY(-50%); -ms-transform: translateY(-50%); -moz-transform: translateY(-50%); -webkit-transform: translateY(-50%); -o-transform: translateY(-50%);">
        <div class="row justify-content-center">
            <div class="col-md-10 col-lg-9 col-xl-9 col-xxl-7">
                <div class="card shadow-lg o-hidden border-0 my-5">
                    <div class="card-body p-0">
                        <div class="row">
                            <div class="col-lg-12">
                                <div class="p-5">
                                    <div class="text-center">
                                        <h4 class="text-dark mb-4">ログイン</h4>
                                    </div>
                                    <form class="user">
                                        <div class="mb-3"><input class="form-control form-control-user" type="email" id="email" aria-describedby="emailHelp" placeholder="メール" name="email" required=""></div>
                                        <div class="mb-3"><input class="form-control form-control-user" type="password" placeholder="パスワード" name="password" required=""></div>
                                        <div class="row mb-3">
                                            <p id="errorMsg" class="text-danger" style="display:none;">Paragraph</p>
                                        </div><button class="btn btn-primary d-block btn-user w-100" id="submitBtn" type="submit">Login</button>
                                        <hr>
                                    </form>
                                    <div class="text-center"><a class="small" href="forgot-password.html">Forgot Password?</a></div>
                                    <div class="text-center"><a class="small" href="register.html">Create an Account!</a></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div><script>
	let email = document.getElementById("email")
	let submitBtn = document.getElementById("submitBtn")
	let errorMsg = document.getElementById('errorMsg')

	function displayErrorMsg(e) {
		errorMsg.style.display = "block"
		errorMsg.innerHTML = e
		submitBtn.disabled = true
	}

	function hideErrorMsg() {
		errorMsg.style.display = "none"
		submitBtn.disabled = false
	}
	
	// Validate email upon change
	email.addEventListener("change", function() {
		// Check if the email is valid using a regular expression (string@string.string)
		if(email.value.match(/^[^@]+@[^@]+\.[^@]+$/))
			hideErrorMsg()
		else
			displayErrorMsg("Invalid email")
	});
</script>
    </div>
</template>
