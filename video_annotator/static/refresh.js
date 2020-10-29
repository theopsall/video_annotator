var already = [];
$(document).ready(function(){
    $('.addButton').on('click',function(){
    console.log('Clicked');
    var start_minute = $('.start-minute').val();
    var start_second = $('.start-second').val();
    var end_minute = $('.end-minute').val();
    var end_second = $('.end-second').val();

    console.log(start_minute);
    console.log(start_second);
    console.log(end_minute);
    console.log(end_second);

    req = $.ajax({
        url: '/annotate',
        type: 'POST',
        data: {start_minute: start_minute, start_second: start_second, end_minute: end_minute, end_second: end_second}
    });
    req.done(function(){
        already.push(start_minute + ':'+ start_second + '  -  ' + end_minute + ':'+ end_second + '<br>');
        $('#current_annotated').html(already);
        console.log(already);
    });
    });
});
