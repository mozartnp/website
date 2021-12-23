# website

Um site simples para expor produtos, com um painel de controle integrado para gerenciando das informações do site, assim como a manutenção dos produtos em exposição.

<hr>
O site é feito em Django.
No arquivo requirements.txt tem todos os pacotes necessários para o pip

Caso queria instalar:
Sugiro que use o Django e todos as depedencias necessarias dentro de uma ambiente virtual. [Aqui](https://docs.python.org/pt-br/3/library/venv.html) está uma explicação sobre criação e uso de ambientes virtuais, na documentação oficial do Python.
Uma vez com a venv criada e ativada, instale os pacotes necessários via pip, com o comando no terminal: 
pip install -r requirements.txt

Quando todos os pacotes estiverem instalados, é necessario criar um superuser, para isso use o comando:
python path/to/manage.py createsuperuser

O site é dividido em duas partes, uma que consite no site proprimente dito onde é exposto os produtos. E a segunda parte é para manutenção das informções do site, para acessar a parte de manutenção é o http://dominio/manutencao , lembrando que o dominio é defindo por você.