$(document).ready(function() {
    $("#loading").ajaxStart(function(){
        $(this).show();
    });
    var options = {
        beforeSubmit:  showRequest,
        success:       showResponse,
        type:      'post',
        dataType:  'json'
    };

    $('#persform').ajaxForm(options);
});

function showRequest(formData, jqForm, options) {
    $('input, button, textarea').attr('disabled', 'disabled');
    $('a').click(function(e) {
        e.preventDefault();});
    $('#loading').show();
    return true;
}

function showResponse(data, statusText, xhr, $form)  {
    $('#loading').hide();
    $('a').unbind('click');
    $('input, .butt, textarea').attr('disabled', '');
    $('.errorlist').remove();

    if(data.status == 'fail') { //validation test
        for( k in data.pers_errors){
            out = '<span class="errorlist"><br>';
           for(i in data.pers_errors[k]){
              out += data.pers_errors[k][i];
           }
           $('#id_'+ k).after(out + '</span>')
        }
    }
 }
