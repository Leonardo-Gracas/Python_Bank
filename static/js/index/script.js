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

    $('button').click( function() {

        $('button').each( function() {
            if ($(this).hasClass('active')) {
                $(this).removeClass('active');
            }
        });

        if ($('#arg-base').val() == 'get') {
            id = prompt("Insira o ID para a busca:");

            enviarFormulario(id);
        }

        if ($('#arg-base').val() == 'list') {
            $('.card-user').each( function() {
                $(this).removeClass('invisible');

                $('#user-get').addClass('invisible');
            });
        }

        if ($('#arg-base').val() == 'act') {
            $('#modal').css('display', 'flex');
        }

        $(this).addClass('active');
    });

    $('.dropdown')
});

function alt_arg_base(arg) {
    $('#arg-base').val(arg);
}

function alt_arg_act(arg) {
    $('#arg-act').val(arg)
}

function close_modal() {
    $('#modal').css('display', 'none');
}

function enviarFormulario(id) {

    $.ajax({
        url: `/rotaAjax?id=${id}`,
        type: 'GET',
        success: function(response) {
            $('#user-get').find('#get-id').text(response['conta']);
            $('#user-get').find('#get-nome').text(response['nome']);
            $('#user-get').find('#get-saldo').text(response['saldo']);
            $('#user-get').find('#get-renda').text(response['renda']);

            $('.card-user').each( function() {
                $(this).addClass('invisible')
            });

            $('#user-get').removeClass('invisible')
        },
        error: function(error) {
          alert('Erro de requisição: ', error);
        }
      });
      
}


// 
// 
dados = {
    'arg-base' : $('#arg-base').val(),
    // 'nome' : $('#nome').val(),
    // 'renda' : $('#renda').val(),
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