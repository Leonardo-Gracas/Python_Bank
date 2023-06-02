$(document).ready( () => {

    console.log('aaaaaaaa')

    $('.card-user').click( function() {

        const cards_user = $('.card-user');
        cards_user.each( function() {
            if ($(this).hasClass('selecionado')) {
                $(this).removeClass('selecionado');
                $('#idConta1').val()
            }
        });

        if ($('#arg-base').val() != '') {
            id_conta = $(this).find('.id-card').text();

            $(this).addClass("selecionado");
            $('#idConta1').val(id_conta)
        }
    });

    $('button').click((event) => {

        event.preventDefault();

        dados = {
            'arg-base' : $('#arg-base').val(),
            'nome' : $('#nome').val(),
            'renda' : $('#renda').val(),
            'id_conta1' : $('#idConta1').val(),
            'id_conta2' : $('#idConta2').val(),
            'valor' : $('#valor').val()
        }

        if (dados['arg-base'] == 'get') {

            if (dados['id_conta1'] != '') {
                
                $('.card-user').click(function() {
                    enviarFormulario(dados)
                });

            }
        }
    });

});

function alt_arg_base(arg) {
    $('#arg-base').val(arg)
}

function enviarFormulario(dados) {
    
    // if (dados)

    $.ajax({
        url: '/rotaAjax',
        data: dados,
        type: 'POST',
        sucess: () => {
            $('#user-get').find('#get-id').text(response['id']);
            $('#user-get').find('#get-nome').text(response['nome']);
            $('#user-get').find('#get-saldo').text(response['saldo']);
            $('#user-get').find('#get-renda').text(response['renda']);

            $('#user-get').removeClass('invisivel')
        },
        error: () => {
            alert('erro')
        }
    });
}