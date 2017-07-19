$(function() {
    $('#btnRegister').click(function() {
        var user = $('#username').val();
        var pass = $('#password').val();
        $.ajax({
            url: '/register',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
