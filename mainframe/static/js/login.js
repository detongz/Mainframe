  $(document).ready(function(){
        $('.log-btn').click(function(){
          $.ajax({
            type:'POST',
            url:'/auth/login',
            dataType: 'json',
            data: {
              'i':$('#UserName').val(),
              'p':$('#Password').val()
            },
            success:  function(data){
              if(data=="1"){
                window.location.href='/relate/uploadmaterial';
              }
              else if (data=="0") {
                $('.log-status').addClass('wrong-entry');
                $('.alert').fadeIn(500);
              }
            },
          });
          setTimeout( "$('.alert').fadeOut(1500);",3000 );
        });
        $('.form-control').keypress(function(){
          $('.log-status').removeClass('wrong-entry');
        });
    });
