$(function(){
   
    $('.skill-value a.radio-1').hover(
        function(){
            $(this).parent().removeClass('value-1 value-2 value-3 value-4 value-5').addClass('value-1');
        },
        function(){
            $(this).parent().removeClass('value-1 value-2 value-3 value-4 value-5');
        }
    );
    $('.skill-value a.radio-2').hover(
        function(){
            $(this).parent().removeClass('value-1 value-2 value-3 value-4 value-5').addClass('value-2');
        },
        function(){
            $(this).parent().removeClass('value-1 value-2 value-3 value-4 value-5');
        }
    );     
    $('.skill-value a.radio-3').hover(
        function(){
            $(this).parent().removeClass('value-1 value-2 value-3 value-4 value-5').addClass('value-3');
        },
        function(){
            $(this).parent().removeClass('value-1 value-2 value-3 value-4 value-5');
        }
    ); 
    $('.skill-value a.radio-4').hover(
        function(){
            $(this).parent().removeClass('value-1 value-2 value-3 value-4 value-5').addClass('value-4');
        },
        function(){
            $(this).parent().removeClass('value-1 value-2 value-3 value-4 value-5');
        }
    );
    $('.skill-value a.radio-5').hover(
        function(){
            $(this).parent().removeClass('value-1 value-2 value-3 value-4 value-5').addClass('value-5');
        },
        function(){
            $(this).parent().removeClass('value-1 value-2 value-3 value-4 value-5');
        }
    );
    $('.skill-value a.radio-1').click(
        function(){
            $(this).parent().removeClass('set-2 set-3 set-4 set-5').toggleClass('set-1')
        }
    );
    $('.skill-value a.radio-2').click(
        function(){
            $(this).parent().removeClass('set-1 set-2 set-3 set-4 set-5').addClass('set-2')
        }
    );       
    $('.skill-value a.radio-3').click(
        function(){
            $(this).parent().removeClass('set-1 set-2 set-3 set-4 set-5').addClass('set-3')
        }
    );  
    $('.skill-value a.radio-4').click(
        function(){
            $(this).parent().removeClass('set-1 set-2 set-3 set-4 set-5').addClass('set-4')
        }
    );  
    $('.skill-value a.radio-5').click(
        function(){
            $(this).parent().removeClass('set-1 set-2 set-3 set-4 set-5').addClass('set-5')
        }
    );  
   
});



