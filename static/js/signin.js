$(document).ready(function(){

    $('#login').click(function(){
        window.location.href = "login"
    });

    function showError(error){
        $('#error').html(error)
    }

    $('#submit').click(function(){
        var login = $('#login_text').val(),
            email = $('#email').val(),
            password = $('#password'),
            password2 = $('#password2');
        console.log(login, email, password.val(), password2.val());
        if(password.val() === password2.val()){
            console.log(login, 'if pass the same');
            if (login && email && password){
                $.post('signin', {'login': login, 'email': email, 'password': password.val()}, function(data){
                    console.log(data);
                    if (data.error){
                        showError(data.error)
                    }else{
                        window.location.href = '/'
                    }
                });
            }else{
                showError('Please fill all fields')
            }
        }else{
            showError('Passwords must be the same');
        }
    });
});
