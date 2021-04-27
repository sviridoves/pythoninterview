$.get( "/index_new", function ( data ) {
    let out = ''
    let dat = JSON.parse(data);
    dat.forEach(function (item){
        out +=  '<tr>
                <td>${item.fields.title}</td>
                <td>${item.fields.price}</td>
                <td>${item.fields.receipted_date}</td>
                <td>${item.fields.measure}</td>
                <td>${item.fields.vendor}</td>
                </tr>'
    });
    $( "#test" ).html( out );
})

$(document).ready(function ($){
    $('.js-add-item').click(function (){
        $('.modal-fade').fadeIn();
        return false;
    });

    $('.modal-close').click(function (){
        $(this).parents(elem, '.modal-fade').fadeOut();
        return false;
    });

    $(document).keydown(function (e){
        if (e.keyCode === 27) {
            e.stopPropagation();
            $('.modal-fade').fadeOut();
        }
    });

    $('.js-add-item').click(function (e){
        if ($(e.target).closest(selectors, '.modal-dialog').length == 0) {
            $(this).fadeOut();
        }
    });
});
