# Classe controller, para trazer a url da aplicação

import requests
import re
from requests.exceptions import RequestException
# classe para retornar a resposta vinda de um servidor externo. Retorna json
class RetornaDadosJson:
    def __init__(self, base_url): # passar como parametro a url
        self.base_url = base_url # retonar a url

    def fetch_data(self, endpoint):
        url = f"{self.base_url}{endpoint}" # faz um slice na url e divide a url em duas

        #bloco try para tratar a url selecionada e informar se tem algum erro
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except RequestException as e:
            raise RuntimeError(f"Foram encontrados os seguintes erros: {e}")
            
# retorna coordenadas para verificar se o cliente é do nível especial ou não
class RetornaCoordenadas:

    def __init__(self, latitude, longitude):

        # inicia a variavel latitude e longitude
        self.latitude = float(latitude)
        self.longitude = float(longitude)

        # converte de string para float
        # regra de coordenadas 1 cliente especial
        minlon_especial_pos1 = float(-2.196998)
        minlat_especial_pos1 = float(-46.361899)
        maxlon_especial_pos1 = float(-15.411580)
        maxlat_especial_pos1 = float(-34.276938)

        # regra de coordenadas 2 cliente especial
        minlon_especial_pos2 = float(-19.766959)
        minlat_especial_pos2 = float(-52.997614)
        maxlon_especial_pos2 = float(-23.966413)
        maxlat_especial_pos2 = float(-44.428305)

        # regra de coordenadas cliente 3 normal
        minlon_especial_pos3 = float(-26.155681)
        minlat_especial_pos3 = float(-54.777426)
        maxlon_especial_pos3 = float(-34.016466)
        maxlat_especial_pos3 = float(-46.603598)

        #insere todas as nossas variavies em uma matriz
        self.verifica_regras = [
            {
                'tipo_cliente' : 'especial',
                'minlon': minlon_especial_pos1,
                'minlat': minlat_especial_pos1,
                'maxlon': maxlon_especial_pos1,
                'maxlat': maxlat_especial_pos1
            }, 
            {
                'tipo_cliente' : 'especial',
                'minlon': minlon_especial_pos2,
                'minlat': minlat_especial_pos2,
                'maxlon': maxlon_especial_pos2,
                'maxlat': maxlat_especial_pos2
            },
            {
                'tipo_cliente' : 'normal',
                'minlon': minlon_especial_pos3,
                'minlat': minlat_especial_pos3,
                'maxlon': maxlon_especial_pos3,
                'maxlat': maxlat_especial_pos3
            },
        ]

    def retorna_tipo_cliente(self):

        # retorna o tipo de cliente por regra, se é normal especial ou cliente do tipo trabalhoso
        for regras_clientes in self.verifica_regras:        
                if (regras_clientes['minlon'] <= self.longitude <= regras_clientes['maxlon'] and regras_clientes['minlat'] <= self.latitude <= regras_clientes['maxlat']):
                        return regras_clientes['tipo_cliente']
                
        return 'trabalhoso' # retorna cliente trabalhoso (se em não for em nenhum dos casos o tipo de cliente normal ou especial)

# classe para retornar o numero do telefone formatado para o padrão Brasil +55
class formatNumeroTelefoneCelular:

    def __init__(self, numero_telefone, numero_celular):
        
        # inicia as variaveis e retira todos os caracteres 
        self.numero_telefone = re.sub(r'\D', '', numero_telefone)
        self.numero_celular = re.sub(r'\D', '', numero_celular)

        # retorna o codigo do pais que é o Brasil, junto com o telefone sem os caracteres
        self.codigo_do_pais = '55'

        #mascara_padrao
        self.padrao = r"(\d{2})(\d{4,5})(\d{4})"

    def formata_numeros(self,numero):
        match = re.match(self.padrao, numero)
        if match:
            return '+{}{}{}{}'.format(
                self.codigo_do_pais,
                match.group(1),
                match.group(2),
                match.group(3)
            )
        else:
            return None
        
    def retorna_telefone_formatado(self):
        # Formata e retorna o número de telefone
        telefone_formatado = self.formata_numeros(self.numero_telefone)
        if telefone_formatado:
            return telefone_formatado
        else:
            return 'Número telefone não é 55 (Brasil)!'

    def retorna_celular_formatado(self):
        # Formata e retorna o número de celular
        celular_formatado = self.formata_numeros(self.numero_celular)
        if celular_formatado:
            return celular_formatado
        else:
            return 'Número de celular não válido!'

#classe para retornar a regiao a partir do estado 
#   
class formataEstadoRegiao:

    def __init__(self, estado):

        self.estado_formatado = estado.replace(" ", "") #replace para tirar o espacao

    def retorna_estado(self):

        regiao = None
        #verifica todos os estados da federação e retorna a região
        if self.estado_formatado == 'parana' or self.estado_formatado == 'santacatarina' or self.estado_formatado == 'riograndedosul':
            regiao = 'sul'
        elif self.estado_formatado == 'sãopaulo' or self.estado_formatado == 'saopaulo' or self.estado_formatado == 'riodejaneiro' or self.estado_formatado == 'minasgerais' or self.estado_formatado == 'espiritosanto':
            regiao = 'sudeste'
        elif self.estado_formatado == 'matogrosso' or self.estado_formatado == 'matogrossodosul' or self.estado_formatado == 'goiás' or self.estado_formatado == 'goias' or self.estado_formatado == 'distritofederal':
            regiao = 'centrooeste'
        elif self.estado_formatado == 'amazonas' or self.estado_formatado == 'acre' or self.estado_formatado == 'tocantins' or self.estado_formatado == 'roraima' or self.estado_formatado == 'rondônia' or self.estado_formatado == 'rondonia':
            regiao = 'norte'
        elif self.estado_formatado == 'bahia' or self.estado_formatado == 'pernambuco' or self.estado_formatado == 'sergipe' or self.estado_formatado == 'ceará' or self.estado_formatado == 'ceara' or self.estado_formatado == 'maranhão' or self.estado_formatado == 'maranhao' or self.estado_formatado == 'riograndedonorte' or self.estado_formatado == 'paraiba' or self.estado_formatado == 'alagoas':
            regiao = 'nordeste' 
        else:
            return 'outra região'

        return regiao





        