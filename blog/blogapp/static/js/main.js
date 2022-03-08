$(document).ready(function () {
    $("#cat").click(function () {
        $(".popup").slideToggle();
    })

// EMAIL VALIDATION
$("#email-error").hide()
$("#message").hide()
$("#confirm-password-error").hide()
$("#password-error").hide()
$("#username-error").hide()


$(document).ready(function(){
    $("#register-form").on('submit',function(e){
        e.preventDefault();
        $.ajax({
            url:'/user/create',
            type:"post",
            data:$("#register-form").serialize(),
            success:function(result){
                {
                var username=$("#username").val()
                var email=$("#email").val()
                var password=$("#password").val()
                var confirm_password=$("#confirm_password").val()
                var regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
                var regex_username = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9]))/;
                if (password.length < 8){
                    $("#password-error").slideDown()
                    $("#password").removeClass('border-dark')
                    $("#password").addClass('border-danger')
                    $("#password-lebel").addClass('text-danger')
                }
                else{
                    $("#password-error").hide()
                    $("#password").addClass('border-dark')
                    $("#password").removeClass('border-danger')
                    $("#password-lebel").addClass('text-dark')

                }
                if(!regex.test(email)){
                    $("#email-error").slideDown()
                    $("#email").removeClass('border-dark')
                    $("#email").addClass('border-danger')
                    $("#email-lebel").addClass('text-danger')
                }
                else{
                    $("#email-error").hide()
                    $("#email").addClass('border-dark')
                    $("#email").removeClass('border-danger')
                    $("#email-lebel").addClass('text-dark')
                }
                if (!regex_username.test(username)){
                    $("#username-error").slideDown()
                    $("#username").removeClass('border-dark')
                    $("#username").addClass('border-danger')
                    $("#username-lebel").addClass('text-danger')
                }
                else{
                    $("#username-error").hide()
                    $("#username").addClass('border-dark')
                    $("#username").removeClass('border-danger')
                    $("#username-lebel").addClass('text-dark')
                }
                if(password!=confirm_password){
                    $("#confirm-password-error").slideDown()
                    $("#confirm-password").removeClass('border-dark')
                    $("#confirm_password").addClass('border-danger')
                    $("#confirm-password-lebel").addClass('text-danger')
                }
                else{
                    $("#confirm_password-error").hide()
                    $("#confirm_password").addClass('border-dark')
                    $("#confirm_password").removeClass('border-danger')
                    $("#confirm_password-lebel").addClass('text-dark')
                }
                // alert("User Created")
                
            }
            },
            
        })
    })
})
    


})  
