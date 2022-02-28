$(document).ready(function () {
    $("#cat").click(function () {
        $(".popup").slideToggle();
    })

// EMAIL VALIDATION
$("#email-error").hide()
$("#password-error").hide()
$("#submit").click(function(){
        var email = $("#email").val()
        var regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        if (regex.test(email)){
            if($("#password").val().length > 8){
                $("#submit").attr('type','submit')
            }
            else{
                $("#password-error").slideDown()
                $("#password").removeClass('border-dark')
                $("#password").addClass('border-danger')
                $("#password-lebel").addClass('text-danger')
            }
        }
        else{
            $("#email-error").slideDown()
            $("#email").removeClass('border-dark')
            $("#email").addClass('border-danger')
            $("#email-lebel").addClass('text-danger')
        }
    })
})  
