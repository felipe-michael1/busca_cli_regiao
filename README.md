# juntos_somos_mais
Projeto de busca de clientes por região usando Javascript com Python e Django

Informações de acesso da API:

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

Crie um ambiente virtual:

python -m venv venv
source venv/bin/activate  	
No Windows: venv\Scripts\activate

Execute o seguinte comando para rodar o projeto na sua máquina ou servidor:
python manage.py runserver

Como usar a API no Postman?

Linha de Comando: Muitas configurações de servidor envolvem iniciar o servidor por meio de um prompt de comando ou terminal. 
Executar o comando apropriado (específico para a tecnologia do seu servidor) deve iniciar o processo do servidor.
Acesso pelo Navegador: Uma vez que o servidor esteja em funcionamento, abra uma janela do navegador web e navegue até http://localhost:<número da porta>. 
O número da porta pode variar dependendo da sua configuração do servidor, sendo tipicamente algo como 8080 ou 3000. Você deve ver uma resposta do seu servidor local confirmando que está funcionando com sucesso.

Verifique a URL da API instalada na máquina:

Onde foi testado, foi com a seguinte URL:
http://127.0.0.1/busca_cli_json?regiao=norte

Caso não consiga rodar a API no Postman, verifique:
Restrições de Firewall: Alguns firewalls podem bloquear conexões ao localhost por padrão. 
Verifique suas configurações de firewall para garantir que a comunicação entre o Postman e seu servidor local seja permitida.
Conflitos de Processo: Outro aplicativo pode estar usando a mesma porta que seu servidor local. 
Identifique o processo conflitante e pare-o ou configure seu servidor para usar uma porta diferente.

#Licença:
Este código é licenciado para uso somente do seu desenvolvedor e também da equipe de trabalho da Juntos Somos Mais.
