var already = [];
var index = 0;
$(document).ready(function(){
    $('.addButton').on('click',function(){
    console.log('Add button Clicked');
    var start_minute = $('.start-minute').val();
    var start_second = $('.start-second').val();
    var end_minute = $('.end-minute').val();
    var end_second = $('.end-second').val();

    if(start_minute=='' && start_second=='' || end_minute=='' && end_second=='' ){
        console.log("Values are Null");
        return;
    }
    $('.start-minute').val('');
    $('.start-second').val('');
    $('.end-minute').val('');
    $('.end-second').val('');
    req = $.ajax({
        url: '/annotate',
        type: 'POST',
        data: {start_minute: start_minute, start_second: start_second, end_minute: end_minute, end_second: end_second}
    });
    req.done(function(){

        var text = "<span  id='annotation_"+ index +"'>" 
                    + start_minute + ":" + start_second + "-" + end_minute + ":"+ end_second 
                    + "</span><br>";
                    // +"<i  class='fa fa-window-close' aria-hidden='true' onclick='deleteData("+index+")'></i> <br>";
        already.push(text);
        $('#current_annotated').html(already);
        index ++;
    });
    });
});
if (performance.type == performance.TYPE_RELOAD) {
    console.log( "This page is reloaded" );
    already = [];
    index = 0;
    req = $.ajax({
    url: '/annotate',
    type: 'POST',
    data: {is_reloaded: true}
    });
  }

function deleteData(index){
    console.log("To Delete");
    console.log(index);
    req = $.ajax({
        url: '/annotate',
        type: 'POST',
        data: {delete: true, index:index}
    });
    already.pop()
    $('#current_annotated').html(already);
    index --;
}
