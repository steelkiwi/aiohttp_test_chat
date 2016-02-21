$(document).ready(function(){

    $('#signin').click(function(){
        window.location.href = "signin"
    });

    function showError(error){
        $('#error').html(error)
    }

    $('#submit').click(function(){
        var login = $('#login').val(),
            password = $('#password').val();
        console.log(login, 'if pass the same');
        if(login && password){
            $.post('login', {'login': login, 'password': password}, function(data){
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
    });
});
