Um site simples para expor produtos, com um painel de controle integrado para gerenciamento das informações e das imagens dos produtos em exposição.

<hr>
O site é feito em Django.
No arquivo requirements.txt estão todos os pacotes necessários para o pip.

Caso queria instalar:
Sugiro que use o Django e todas as dependências necessárias dentro de um ambiente virtual. [Aqui](https://docs.python.org/pt-br/3/library/venv.html) está uma explicação sobre criação e uso de ambientes virtuais, na documentação oficial do Python.
Uma vez com a venv criada e ativada, instale os pacotes necessários via pip, com o comando no terminal: 
pip install -r requirements.txt

Quando todos os pacotes estiverem instalados, é necessário criar um superuser. Para isso, use o comando:
python path/to/manage.py createsuperuser

O site é dividido em duas partes, uma que consiste no site propriamente dito, onde são expostos os produtos, e a segunda parte é para manutenção das informações. Para ir para a parte de manutenção, acesse: dominio/manutencao , lembrando que o domínio é definido por você.