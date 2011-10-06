$(document).ready(function() {
    $("#loading").ajaxStart(function(){
        $(this).show();
    });
    var options = {
        beforeSubmit:  showRequest,
        success:       showResponse,
        url:     '/edit/',
        type:      'post',
        dataType:  'json'
    };
    var links = new Array();
    $('a').each(function(){
        links.push(this.href);
    });
    $('#persform').ajaxForm(options);


function showRequest(formData, jqForm, options) {
    //var queryString = $.param(formData);
    $('input, button, textarea').attr('disabled', 'disabled');
    $('a').click(function(e) {
        e.preventDefault();});
    //$('.errorlist').remove();
    $('#loading').show();
    return true;
}
function showResponse(data, statusText, xhr, $form)  {
    $('#loading').hide();
    $('a').unbind('click');
    $('input, .butt, textarea').attr('disabled', '');
    $('.errorlist').remove();

    if(data.status != 'ok') { //validation test
        for( k in data.pers_errors){
            out = '<span class="errorlist"><br>';
           for(i in data.pers_errors[k]){
              out += data.pers_errors[k][i];
           }
           $('#id_'+ k).after(out + '</span>')
        }

        for( k in data.cont_errors){
            out = '<span class="errorlist"><br>';
           for(i in data.cont_errors[k]){
              out += data.cont_errors[k][i];
           }
           $('#id_'+ k).after(out + '</span>')
        }


    }
 }
});