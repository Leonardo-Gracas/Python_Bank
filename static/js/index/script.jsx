function getSelectedModel(item) {
    return `<div class="selected-user" id="selected-${item.conta}"><div class="apresentacao">    <p id="Conta">${item.conta}</p>    <p id="Nome">${item.nome}</p><p id="Saldo">R$ ${item.saldo.toFixed(2)}</p><p id="Debito">R$ ${item.debito.toFixed(2)}</p></div><div class="operacoes"><form id="operacao-saque"><label for="valor">R$</label><input required type="number" name="valor"><input type="submit" name="sacar" value="Sacar"></form><form id="operacao-deposito"><label for="valor">R$</label><input required type="number" name="valor"><input type="submit" name="depositar" value="Depositar"></form><form id="operacao-transferencia"><label for="valor">R$</label><input required type="number" name="valor"><label for="conta">Para:</label><input required type="number" name="conta"><input type="submit" name="transferencia" value="Transferir"></form><form id="operacao-emprestimo"><label for="valor">R$</label><input required type="number" name="valor"><input type="submit" name="emprestimo" value="Empréstimo"></form><form id="operacao-pagar-debito"><input type="submit" name="pagar-debito" value="Pagar débitos"></form></div><div class="base"><button id="retornar-para-main">Voltar</button><button id="deletar-user">Deletar User</button></div></div>`
}

function getUserModel(element) {
    return `<div class="user" id="${element.conta}"><p id="conta">${element.conta}</p><p>${element.nome}</p><p>Saldo: R$${element.saldo.toFixed(2)}</div>`
}

function getBankModel(bank) {
    return `<div class="saldo_banco"><p>Saldo Banco</p><p id="Saldo">R$: ${bank.saldo.toFixed(2)}</p></div><div class="saldo_corrente"><p>Saldo Corrente</p><p id="Saldo-Corrente">R$: ${bank.saldoCorrente.toFixed(2)}</p></div><div class="additional-content"><p class="date">Maio de 2023</p><button id="PassarMes">Passar Mês =></button></div>`
}

$(document).ready(() => {
    function reload() {
        $.ajax({
            type: "GET",
            url: "/listar",
            success: function (response) {
                bankData = getBankModel(response[0])
                $('#bank').html(bankData)

                content = ''
                response[1].forEach(element => {
                    content += getUserModel(element)
                })
                content += `<div id="add-new-user"><p>Adicionar</p></div>`
                $('#users-list').html(content)

                //
                //ADICIONA O EVENTO DE LEITURA PARA CADA CARD NA TELA
                //
                $('.user').each(function () {
                    $(this).click(function () {
                        data = { "id": Number(this.id) }
                        $.ajax({
                            type: "POST",
                            url: "/selecionar",
                            contentType: "application/json",
                            data: JSON.stringify(data),
                            success: function (response) {
                                item = response
                                content = getSelectedModel(item)
                                $('#overloads').html(content)
                                $('#overloads').addClass('overload-active')
                                $('#retornar-para-main').click(function () {
                                    $('#overloads').html('')
                                    $('#overloads').removeClass('overload-active')
                                })
                                applyOps()
                            }
                        })
                    });
                });

                //
                // ADICIONA O EVENTO DE CLIQUE AO CARD DE ADICIONAR USUÁRIO
                //
                $('#add-new-user').each(function () {
                    $(this).click(function () {
                        $('#overloads').html(`<div id="cadastro"><div id="cadastro-header"><button id="close-tab">X</button></div><form id="add-user"><label for="add-user-nome">Nome:</label><input required type="text" name="add-user-nome" id="add-user-nome"><label for="add-user-renda">Renda:</label><input required type="number" name="add-user-renda" id="add-user-renda"><input type="submit" name="enviar" id="add-user-enviar"></form></div>`)
                        $('#overloads').addClass('overload-active')
                        $('#close-tab').click(function () {
                            $('#overloads').html('')
                            $('#overloads').removeClass('overload-active')
                        })

                        $('#add-user').submit(function (event) {
                            event.preventDefault()

                            let nome = $('input[name="add-user-nome"]').val()
                            let renda = Number($('input[name="add-user-renda"]').val())

                            let data = {
                                "nome": nome,
                                "renda": renda
                            }

                            $.ajax({
                                type: "POST",
                                url: "/add-user",
                                contentType: "application/json",
                                data: JSON.stringify(data),
                                success: function () {
                                    console.log("Usuário criado!")
                                    reload()
                                    $('#overloads').html('')
                                    $('#overloads').removeClass('overload-active')
                                }
                            })
                        })
                    })
                })

                $('#PassarMes').click(function () {
                    $.ajax({
                        type: "GET",
                        url: "/passar-mes",
                        success: function (message) {
                            console.log(message)
                            reload()
                        }
                    })
                })
            }
        })
    }
    reload()

    function reloadCard(id) {
        id = Number(id)
        data = { "id": id }
        $.ajax({
            type: "POST",
            url: "/selecionar",
            contentType: "application/json",
            data: JSON.stringify(data),
            success: function (response) {
                item = response
                content = getSelectedModel(item)
                $('#overloads').html(content)
                $('#overloads').addClass('overload-active')
                $('#retornar-para-main').click(function () {
                    $('#overloads').html('')
                    $('#overloads').removeClass('overload-active')
                })
                applyOps()
            }
        })
    }

    function applyOps() {
        $('#operacao-saque').submit(function (event) {
            event.preventDefault()

            id = $('.selected-user').first().attr('id')
            id = id.substr(-3)
            value = $('#operacao-saque input[name="valor"]').val()
            $('input[name="valor"]').val(null)

            data = {
                "id": id,
                "value": value
            }

            console.log(data)

            $.ajax({
                type: "POST",
                url: "/sacar",
                contentType: "application/json",
                data: JSON.stringify(data),
                success: function (message) {
                    console.log(message)
                    reload()
                    reloadCard(id)
                }
            })
        })

        $('#operacao-deposito').submit(function (event) {
            event.preventDefault()

            id = $('.selected-user').first().attr('id')
            id = id.substr(-3)
            value = $('#operacao-deposito input[name="valor"]').val()
            $('input[name="valor"]').val(null)

            data = {
                "id": id,
                "value": value
            }

            console.log(data)

            $.ajax({
                type: "POST",
                url: "/depositar",
                contentType: "application/json",
                data: JSON.stringify(data),
                success: function (message) {
                    console.log(message)
                    reload()
                    reloadCard(id)
                }
            })
        })

        $('#operacao-transferencia').submit(function (event) {
            event.preventDefault()

            id = $('.selected-user').first().attr('id')
            id = id.substr(-3)
            value = $('#operacao-transferencia input[name="valor"]').val()
            $('input[name="valor"]').val(null)
            otherId = $('#operacao-transferencia input[name="conta"]').val()
            $('#operacao-transferencia input[name="conta"]').val(null)

            data = {
                "id": id,
                "value": value,
                "otherId": otherId
            }

            console.log(data)

            $.ajax({
                type: "POST",
                url: "/transferir",
                contentType: "application/json",
                data: JSON.stringify(data),
                success: function (message) {
                    console.log(message)
                    reload()
                    reloadCard(id)
                }
            })
        })

        $('#operacao-emprestimo').submit(function (event) {
            event.preventDefault()

            id = $('.selected-user').first().attr('id')
            id = id.substr(-3)
            value = $('#operacao-emprestimo input[name="valor"]').val()
            $('input[name="valor"]').val(null)

            data = {
                "id": id,
                "value": value
            }

            console.log(data)

            $.ajax({
                type: "POST",
                url: "/emprestimo",
                contentType: "application/json",
                data: JSON.stringify(data),
                success: function (message) {
                    console.log(message)
                    reload()
                    reloadCard(id)
                }
            })
        })

        $('#operacao-pagar-debito').submit(function (event) {
            event.preventDefault()

            id = $('.selected-user').first().attr('id')
            id = id.substr(-3)

            data = {
                "id": id,
            }

            console.log(data)

            $.ajax({
                type: "POST",
                url: "/pagar",
                contentType: "application/json",
                data: JSON.stringify(data),
                success: function (message) {
                    console.log(message)
                    reload()
                    reloadCard(id)
                }
            })
        })

        $('#deletar-user').click(function (event) {
            event.preventDefault()

            id = $('.selected-user').first().attr('id')
            id = id.substr(-3)

            data = {
                "id": id,
            }

            console.log(data)

            $.ajax({
                type: "POST",
                url: "/deletar",
                contentType: "application/json",
                data: JSON.stringify(data),
                success: function (message) {
                    console.log(message)
                    reload()
                    $('#overloads').html('')
                    $('#overloads').removeClass('overload-active')
                }
            })
        })
    }
});