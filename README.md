# (Busca de clientes via JSON com Python)
Projeto de busca de clientes por região usando Javascript com Python e Django.

<strong>Informações de acesso da API:</strong>

-Requisitos:

Verifique se você tem o python 3 ou o Django instalados na máquina. Se não tiver, favor realizar o download dos pacotes de instalação 
nos links e repositórios abaixo:

Python:
- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)

Django:

git clone https://github.com/django/django.git

ou no cmd do windows (prompt de comando) digite o seguinte comando para instalar a versão mais recente do Django:

pip install django

<strong>Crie um ambiente virtual:</strong>

python -m venv venv
source venv/bin/activate  	
No Windows: venv\Scripts\activate

Baixe os arquivos deste projeto usando o comando:

git clone https://github.com/felipe-michael1/busca_cli_regiao.git -- acesso via terminal windows ou VS Code
para acesso via ssh: git@github.com:felipe-michael1/juntos_somos_mais.git

- Os arquivos devem ser instalados no repositório onde o Django está instalado em sua máquina ou servidor local.

Execute o seguinte comando para rodar o projeto na sua máquina ou servidor:
<strong>python manage.py runserver.</strong>

Para executar o projeto é necessário que o arquivo manage.py esteja no mesmo diretório onde irá ser realizado o deploy do programa.

<strong>Erros comuns de CSS ou Visualização de página:</strong>

Alguns erros comuns podem aparecer quando o arquivo settings.py é configurado incorretamente para uso do método static. Antes de iniciar a aplicação, ou se apresentar algum erro de CSS, verificar o arquivo settings.py a seguinte estrutura:

Importar o os.

Diretório onde o Django vai procurar arquivos estáticos durante o desenvolvimento:
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'myapp/static'),
]

Diretório onde o Django vai coletar arquivos estáticos para produção:
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

URL para acessar os arquivos estáticos:
STATIC_URL = '/static/'

<strong>Como usar a API no Postman?</strong>

Se for usar em localhost é necessário instalar o PostMan Agent em seu computador. Você pode instalar a partir deste link abaixo:

https://www.postman.com/downloads/postman-agent/

Linha de Comando: Muitas configurações de servidor envolvem iniciar o servidor por meio de um prompt de comando ou terminal. 
Executar o comando apropriado (específico para a tecnologia do seu servidor) deve iniciar o processo do servidor.
Acesso pelo Navegador: Uma vez que o servidor esteja em funcionamento, abra uma janela do navegador web e navegue até http://localhost:<número da porta>. 
O número da porta pode variar dependendo da sua configuração do servidor, sendo tipicamente algo como 8080 ou 3000. Você deve ver uma resposta do seu servidor local confirmando que está funcionando com sucesso.

Verifique a URL da API instalada na máquina:

A aplicação foi testada com a seguinte URL:
http://127.0.0.1/busca_cli_json?regiao=norte

Caso não consiga rodar a API no Postman, verifique:
Restrições de Firewall: Alguns firewalls podem bloquear conexões ao localhost por padrão. 
Verifique suas configurações de firewall para garantir que a comunicação entre o Postman e seu servidor local seja permitida.
Conflitos de Processo: Outro aplicativo pode estar usando a mesma porta que seu servidor local. 
Identifique o processo conflitante e pare-o ou configure seu servidor para usar uma porta diferente.

<strong>#Licença:</strong>
Este código é licenciado para uso somente para fins didáticos.
- Caso tenham alguma dúvida na instalação, favor enviar um email para: felipe.fonseca.michael1@gmail.com
