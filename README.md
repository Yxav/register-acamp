# Cadastro-Acampamento
Sistema de cadastro criado com Django (Python), para um retiro de jovens, com a temática militar.

Para iniciar:
```python
virtualenv env
source env/bin/activate
pip install -r requirements.txt

```

Após ativar instalar os requerimentos, faça as migrações:
```python
python manage.py makemigrations
python manage.py migrate
```

Agora rode o servidor:
```python
python manage.py runserver
```

## Como funciona?
O sistema possui um formulário simples, onde o usuário preenche suas informações básicas, validadas, são persistidas no banco de dados

Logo após o cadastro, o usuário recebe uma confirmação de sua inscrição, retornando com algumas de suas informações.

## Admin
Todo gerenciamento do sistema é realizada pelo Django Admin, para criar um super usuário, digite na linha de comando:

```python
python manage.py createsuperuser
```

E siga o passo a passo do utilitário.


Você poderá obter mais detalhes na documentação oficial do [Django](https://docs.djangoproject.com/en/3.0/ "Django")
