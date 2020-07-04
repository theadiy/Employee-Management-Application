/** Validate email if out of focus */
$(document).ready(function(){
    $(document).on("click", function(event){

        if(!$(event.target).closest("#email").length ){
            var emailInputText = $('#email').val().trim();
            if(!emailInputText=="" && !validEmail(emailInputText)){
                document.getElementById('email').style.border = "solid 1px red";
            }else if(!emailInputText=="" && validEmail(emailInputText)){
                document.getElementById('email').style.border = 'solid 1px white';
            }     
        }else{
            document.getElementById('email').style.border = 'solid 1px white';
        }

    });

});

/** Validate email format */
function validEmail(emailInputText){
    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(emailInputText)){
        return (true)
    }
    return (false)
}

/** Validate email and password on sumbit & request to server */
function validation(){
    var emailInputText = $('#email').val().trim;
    var passwordInputText =$('#password').val().trim();
    var emailValidationSuccessfull = false;
    var passwordValidationSuccessfull = false;
    if(emailInputText=="" || !validEmail(emailInputText)){
        console.log(emailInputText=="");
        console.log(emailInputText.val());
        console.log(!validEmail(emailInputText));
        document.getElementById('email').style.border = "solid 1px red";
        emailValidationSuccessfull = false;
    }else{
        document.getElementById('email').style.border = 'solid 1px white';
        emailValidationSuccessfull = true;
    }
    if(passwordInputText==""){
        document.getElementById('password').style.border = "solid 1px red";
        passwordValidationSuccessfull = false;
    }else{
        document.getElementById('password').style.border = 'solid 1px white';
        passwordValidationSuccessfull = true;
    }
    if(emailValidationSuccessfull && passwordValidationSuccessfull){
        $.ajax({
            type:'POST',
            url:'list',
            data:{
                email:$('#email').val().trim(),
                password:$('#password').val().trim(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
                },
            success:function(data){
                console.log(data)
                //$('#content').replaceWith(data);
                var list = window.open('list');
                list.document.open();
                list.document.write(data);
                list.document.close();
            }
        });
        return true;
    }else{
        return false;
    }
}


function showToast() {
    var toast = document.getElementById("toast");
    toast.className = "show";
    setTimeout(function(){ toast.className = toast.className.replace("show", ""); }, 3000);
  }

