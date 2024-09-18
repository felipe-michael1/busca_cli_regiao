$(document).ready(function () {
    // datatable
    var table = $('#tabela_json').DataTable(
        {
            "pageLength": 15, // Número de linhas por página
            "searching": true, // Habilitar a caixa de busca
            "ordering": true,   // Habilitar ordenação das colunas
            "responsive" : true,
            "language" : {
                
                "sEmptyTable": "Nenhum dado disponível na tabela",
                "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
                "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
                "sInfoFiltered": "(filtrado de _MAX_ registros no total)",
                "sInfoPostFix": "",
                "sInfoThousands": ".",
                "sLengthMenu": "Mostrar _MENU_ registros",
                "sLoadingRecords": "Carregando...",
                "sProcessing": "Processando...",
                "sSearch": "Buscar:",
                "sZeroRecords": "Nenhum registro encontrado",
                "oPaginate": {
                    "sFirst": "Primeira",
                    "sLast": "Última",
                    "sNext": "Próxima",
                    "sPrevious": "Anterior"
                },
                "oAria": {
                    "sSortAscending": ": ativar para ordenar colunas de forma crescente",
                    "sSortDescending": ": ativar para ordenar colunas de forma decrescente"
                }
                
            }
        }
    );
  
    // botao de busca por json
    $('.btn-busca-json').click(function (e) {
        e.preventDefault();
        $('.view-json').css('display', 'block');
    });

    /* botão de busca ao selecionar uma região específica */
    $('.btn-busca').click(function (e) {
        e.preventDefault();

        var regiao = $('#regiao option:selected').val();
        var id_regiao = '';

        if (!regiao) {
            alert('Selecione um região');
            return false;
        }

        if (regiao == 1) {
            id_regiao = 'norte';
        }
        if (regiao == 2) {
            id_regiao = 'sul';
        } 
        if (regiao == 3) {
            id_regiao = 'sudeste'
        }
        if (regiao == 4) {
            id_regiao = 'centrooeste'
        }
        if (regiao == 5) {
            id_regiao = 'nordeste'
        } 
        if (regiao == 6) {
            id_regiao = 'outra'
        }
       
        // traz as informações vindas da API
        $.ajax({
            url: "busca_cli_json",
            type: 'GET',
            dataType: 'json',
            data: {
                id_regiao: id_regiao
            },
            success: function (response) {
              /*  console.log(response);*/

              table.clear();

                // Adiciona dados à tabela
                response.clientes.forEach(cliente => {
                    var observacaoClass = '';

                    // Define a classe com base na observação do cliente
                    if (cliente.observacao_cliente === 'trabalhoso') {
                        observacaoClass = 'icon-circle-yellow'; // Amarelo
                    } else if (cliente.observacao_cliente === 'normal') {
                        observacaoClass = 'icon-circle-green'; // Verde
                    } else if (cliente.observacao_cliente === 'especial') {
                        observacaoClass = 'icon-circle-blue'; // Azul
                    }

                    // cria as linhas
                    var row = [
                        cliente.nome.primeiro_nome + ' ' + cliente.nome.segundo_nome,
                        cliente.email,
                        cliente.telefone,
                        cliente.localizacao.regiao,
                        cliente.localizacao.endereco,
                        cliente.localizacao.cep,
                        cliente.localizacao.nacionalidade,
                       `<div class="${observacaoClass}">${cliente.observacao_cliente}</div>`
                    ];

                    // adiciona as linhas na tabela selecionada
                    table.row.add(row).draw();
               });
                $('.legenda_clientes').css('display','block');
            },
            error: function (xhr, status, error) {
                console.error('Ocorreu um erro ao executar a API. Erro:', error);
            }
        });
     
    });
   
});