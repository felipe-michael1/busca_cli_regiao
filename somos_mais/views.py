# import requests python
# import django Json response
# import classes externas
import requests
from django.shortcuts import render
from .controller import RetornaDadosJson
from .controller import RetornaCoordenadas
from .controller import formatNumeroTelefoneCelular
from .controller import formataEstadoRegiao
from django.http import JsonResponse
import re

# renderizacao para retornar o arquivo html do template SOMOS_MAIS
#template SOMOS_MAIS
def index(request):
    return render(request, 'somos_mais/index.html')

def sobre(request):
     return render(request, 'somos_mais/sobre.html')

# API JSON
# retorna os dados via json via url
def retorna_dados_json(request):
    url_base = 'https://storage.googleapis.com/juntossomosmais-code-challenge/' #criamos uma variavel que contem uma url para processamento
    get_json = RetornaDadosJson(url_base) # enviar para a classe a url externa para processamento

    # criação de um endpoint para proessar a informacao
    url_final = 'input-backend.json' # variavel de endpoint
    try:
        dados = get_json.fetch_data(url_final) # end point
        retorna_data = dados.json() 
        # retorno de erros da aplicação
        # erro 500: Erro de resposta do servidor
    except RuntimeError as e:
        return JsonResponse( 
            {
                'Erro ao processar as informações do Json :' : str(e),
                'Status do erro : ' : 500
            }
        )
    # extrair as informacoes do json

    # retorna as informacoes passadas na regiao selecionada */
    regiao_id = request.GET.get('id_regiao')
    #regiao_id = 'norte'
    if 'results' in retorna_data: # verifica a variavel results par retornar tudo o que está em retorna_dara
        total_clientes = 0
       # total_clientes = len(retorna_data['results'])  # Contar a quantidade total de usuarios (clientes)
        array_resultado = [] # cria um array para tratar as informações vindas do json
      #  print(retorna_data)
        
        for usuarios in retorna_data['results']:
        #inicializa as variaveis para o array
            # verifica a regiao para poder aplicar o filtro
            estado = usuarios['location']['state']
            # retorna a regiao pelo estado fornecido
            retorna_regiao = formataEstadoRegiao(estado)
            regiao = retorna_regiao.retorna_estado()
        
            if regiao_id == regiao:
                total_clientes += 1
                genero = usuarios['gender']
                if genero == 'male':
                        genero = 'M'
                elif genero == 'female':
                    genero = 'F'
                nacionalidade = 'BR'
                primeiro_nome = usuarios['name']['first']
                segundo_nome = usuarios['name']['last']
                email = usuarios['email']
                telefone = usuarios['phone']
                celular = usuarios['cell']
                
                endereco = usuarios['location']['street']
                cep = usuarios['location']['postcode']
                cidade = usuarios['location']['city']
                idade = usuarios['dob']['age']

                # transformado latitude e longitude para float
                latitude = float(usuarios['location']['coordinates']['latitude'])
                longitude = float(usuarios['location']['coordinates']['longitude'])
                retorna_cliente = RetornaCoordenadas(latitude,longitude)
                observacao = retorna_cliente.retorna_tipo_cliente()
            
                # verifica o numero de telefone e celular, formata ambos
                retorna_telefone = formatNumeroTelefoneCelular(telefone,celular)
                telefone_formatado = retorna_telefone.retorna_telefone_formatado()
                celular_formatado = retorna_telefone.retorna_celular_formatado()

                #matriz para organizar os itens no formato json e retornar via ajax no front-end
                matriz = {
                    'nome': {
                            'primeiro_nome' : primeiro_nome,
                            'segundo_nome' : segundo_nome
                        },  
                    'genero' : genero,
                    'idade' : idade,
                    'email': email,
                    'telefone': telefone_formatado,
                    'celular' : celular_formatado,
                    'localizacao' : {
                        'estado': estado,
                        'regiao' : regiao,
                        'endereco': endereco,
                        'cep': cep,
                        'cidade': cidade,
                        'nacionalidade' : nacionalidade
                    },
                    'coordenadas' : {
                        'latitude' : latitude,
                        'longitude' : longitude
                    },
                    'observacao_cliente' : observacao,
                }
                array_resultado.append(matriz)
                
        # retorna o json fora do bloco do for
        return JsonResponse(
            {
                'clientes': array_resultado,
                'total_clientes': total_clientes
            }
        )
       
    else:
        # retorna o erro ao extrair as informações da matriz correspondente
        # Erro 500: Erro de resposta do servidor
        return JsonResponse( 
        {
            'Erro ao extrair as informações da matriz selecionada :' : str(e),
            'Status do erro : ' : 500
        }
    )

