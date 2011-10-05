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

    $('#persform').ajaxForm(options);
});

function showRequest(formData, jqForm, options) {
    //var queryString = $.param(formData);
    $('input, button, textarea').attr('disabled', 'disabled');
    $('span.errors').remove();
    return true;
}
function showResponse(responseText, statusText, xhr, $form)  {
    $('#loading').hide();
    $('input, .butt, textarea').attr('disabled', '');
    if(responseText == null) window.location.href = '/';
    for( var k in responseText){
        $('td:has(#id_'+k+')').append('<span class="errors">'+responseText[k]+'</span>');
       }
}

                jQuery(document).ready(function() {
                    jQuery("#id_birthday").dynDateTime({
                        ifFormat: "%d.%m.%Y",
                        align: "cR",
                        electric: false,
                        singleClick: true
                     //   position:
                    /*	displayArea: ".siblings('.dtcDisplayArea')",*/
                     //   button: ".next()" //next sibling
                    });
                });



