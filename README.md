# Tutorial
```bash
git clone git@github.com:pedromadureira000/fight-gym.git
cd fight-gym
python -m venv .venv
# if necessary: sudo docker compose up -d
source .venv/bin/activate && sudo systemctl start docker
pip install -r requirements.txt
cp contrib/env-sample .env
psql postgres://admin_ph:asdf@localhost:5432/postgres
postgres=# create database soluma_boleto;
postgres=# \q
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
## running web
```bash
python manage.py runserver  
flutter run -d chrome --dart-define-from-file=.env --web-port=33885 --dart-define=BACKEND_IP=127.0.0.1:8000 --dart-define=SCHEME=http
```
## running android
```bash
python manage.py runserver 192.168.1.6:8000
flutter run -d chrome --dart-define-from-file=.env --web-port=33885 --dart-define=BACKEND_IP=192.168.1.6:8000 --dart-define=SCHEME=http
```

## Running celery
```bash
celery -A fight-gym worker -l INFO --pool=gevent --concurrency=8 --hostname=worker -E --queues=send_completion_to_user
```

## admin commands
```bash
python manage.py admin_generator core
```

Curl
===========
## Get Auth Token
request:
```
curl -X POST -d '
    {
        "username": "admin@admin.com",
        "password": "asdf"
    }
    ' -H "Content-Type: application/json;" http://127.0.0.1:8000/api/user/gettoken
```
response:
```
{"token":"68ecbf05e4949217f80c514545d8dd05ed898881"}
```

## Login
```
curl -X POST -d '
    {
        "username": "admin@admin.com",
        "password": "asdf"
    }
    ' -H "Content-Type: application/json;" http://127.0.0.1:8000/api/user/login
```

## Logout
```
curl -X POST -d '
    {
        ???
    }
    ' -H "Content-Type: application/json;" http://127.0.0.1:8000/api/user/logout
```

## Gerar boleto
* api/boleto'
```
curl -X POST -H "Authorization: Token 68ecbf05e4949217f80c514545d8dd05ed898881" -d '
    {
       "comando": "boleto",
       "modelo": "1",
       "campos": {
           "banco": "sicoob",
           "codigo_banco": "333dx6",
           "linha_digitavel": "7569100330070010480040000000095000000000000000000000000000x61",
           "codigo_barras": "7569187460000268000133000104804950000069444",
           "CNPJ_beneficiario": "111111111111111x18",
           "beneficiario": "es em Inform oluCorpoSma Solucoffffffffffffffffffffffffffffx62",
           "agencia": "3305588x10",
           "codigo_cedente": "4899988888x13",
           "endereco_beneficiario": "PAULO, QAV. SAO D. - VILA LT.08 AP.02 BRA. A-GO - 7490SILIA 55DE GOIANI555775-8P5-x85",
           "pagador": "ALUCEL DE ALUM6666666NTRO CENTRA6667777777777777777777778888888888888888x75",
           "nosso_numero": "0000000000004-x17",
           "documento": "00700000000000000675",
           "parcela": "444affggggfffffffffffffx20",
           "vencimento": "10/09/2098",
           "valor_documento": "5.906,1833333333333",
           "local_pagamento": "PAGAVEL PREFERENCIALMENTE NO SICOOB aaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbb",
           "codigo_beneficiario": "123456fffffffffff",
           "especie_documento": "DMaaaaaaaaaa",
           "aceite": "Naaaaaa",
           "data_processamento": "10/01/aa2002aaaa",
           "data_documento": "10/01/aa2002aaaa",
           "carteira": "1aaaaaaaaaaaaaaaaa",
           "quantidade": "10000000000000",
           "xvalor": "xvalor-aaaaaaaaa",
           "especie": "232311,00",
           "instrucoes_responsabilidade_1": "aaaa bbeeeeeeeeeeeeeeeeeeeeeeeeeeaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbb",
           "instrucoes_responsabilidade_2": "aaaa bbeeeeeeeeeeeeeeeeeeeeeeeeeeaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbb",
           "instrucoes_responsabilidade_3": "aaaa bbeeeeeeeeeeeeeeeeeeeeeeeeeeaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbb",
           "instrucoes_responsabilidade_4": "aaaa bbeeeeeeeeeeeeeeeeeeeeeeeeeeaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbb",
           "instrucoes_responsabilidade_5": "aaaa bbeeeeeeeeeeeeeeeeeeeeeeeeeeaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbb",
           "instrucoes_responsabilidade_6": "aaaa bbeeeeeeeeeeeeeeeeeeeeeeeeeeaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbb",
           "instrucoes_responsabilidade_7": "aaaa bbeeeeeeeeeeeeeeeeeeeeeeeeeeaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbb",
           "instrucoes_responsabilidade_8": "aaaa bbeeeeeeeeeeeeeeeeeeeeeeeeeeaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbb",
           "desconto_abatimento": "aaaaaaaaaaaaaaaaaaaaaaa",
           "outras_deducoes": "aaaaaaaaaaaaaaaaaaaaaaa",
           "mora_multa": "aaaaaaaaaaaaaaaaaaa",
           "outros_acrescimos": "aaaaaaaaaaaaaaaaaaa",
           "valor_cobrado": "aaaaaaaaaaaaaaaaaaaaaa",
           "CNPJ_pagador": "3908240984208402",
           "endereco_pagador": "asjdflkaj alfdjlfdja afdljaaaaadljfdaaaaaaaa aaaaaa alfjalfdj fljjaaaaaaaaaaa  aaaaaa  aaaaaaaaaaaaaaaaaaaaaaaaaaaa"
       }
    }
    ' -H "Content-Type: application/json;" http://127.0.0.1:8000/api/boleto
```

* payload
```
```
