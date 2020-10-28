# Taller Práctico

## Introduction

El objetivo de esta practica es comenzar a utilizar python con mongo, para ello usarermos una libreria llamada pymongo.
Para ello importaremos datos mock sobre usuarios de una aplicación. Lo podeis encontrar en el fichero [MOCK_DATA.json](MOCK_DATA.json)


### Apartado 0
Preparando en entorno
```bash

python3 -m venv myvenv
pip install pymongo
pip install -r requirements.txt
```


### Apartado 1
	Importar los datos a un base datos llamada upsa1 en la collecion users
	Se puede usar mongoimport o este fragmento de código python (recomiendo usar el código para aprender a importar desde python)
	
```python
MONGO_HOST = "127.0.0.1:27017"
def import_json(database, collection):
    client = MongoClient(MONGO_HOST)
    db = client[database]
    with open('MOCK_DATA.json') as f:
        file_data = json.load(f)
        db.get_collection(collection).insert_many(file_data)

```

### Apartado 2 
Insertar los siguientes objetos en la base de datos usando python
Podeis consultar el fichero [mongo_utils.py](mongo_utils.py), donde podeis ver un ejemplo básico de cada tipo de operación.
	
	{
	"first_name" : "Manuel",
	"last_name" : "Gomez",
	"email" : "manogo@gmail.com",
	"gender" : "Male",
	"ip_address" : "15.208.64.26",
	"Latitude" : 43.6342238,
	"Altitude" : -3.41144,
	"City" : "Madrid",
	"University" : "Upsa"
	}
	{
	"first_name" : "Lucia",
	"last_name" : "Sanchez",
	"email" : "lucisan@gmail.com",
	"gender" : "Female",
	"ip_address" : "5.208.64.76",
	"Latitude" : 43.1342238,
	"Altitude" : -2.41144,
	"City" : "Salamanca",
	"University" : "UPSA"
	}
	{
	"first_name" : "Sergio",
	"last_name" : "Suarez",
	"email" : "sergiosua@gmail.com",
	"gender" : "Male",
	"ip_address" : "5.208.65.29",
	"Latitude" : 43.1342238,
	"Altitude" : -2.61144,
	"City" : "Salamanca",
	"University" : "UPSA"
	}




### Apartado 3

In this repo you can find a Makefile to help you to deploy and test in local.

* **ABS integration**:
Basicly you can launch, this command deploy gater, dormer, mongodb,abs-dapter, abs-speedster and also
provision all the platform to launch the e2e tests. For more details see at Makefile and docker-compose used there.
	
	```bash
	make deploy_abs
	```

	To launch the tests:
	
	```bash
	make test-abs
	```

* **Sipr integration**:
Basicly you can launch, this command deploy gater, dormer, mongodb,sipr-dapter, spir-speedster and also
provision all the platform to launch the e2e tests. For more details see at Makefile and docker-compose used there.
	
	```bash
	make deploy_sipr
	```

	To launch the tests:
	
	```bash
	make test-sipr
	```

* **Nucleus Batcher**:
Basicly you can launch, this command deploy all SD components needed to launch the tests and provision. 
For more details see at Makefile and docker-compose used there.
	
	```bash
	make deploy_nucleus
	```

	To launch the tests:
	
	```bash
	make test-nucleus
	```

* **Reuse Batcher**:
Basicly you can launch, this command deploy all SD components needed to launch the tests and provision. 
For more details see at Makefile and docker-compose used there.
	
	```bash
	make deploy_reuse
	```

	To launch the tests:

	```bash
	make test-reuse
	```
* **Netcracker**:
Basicly you can launch, this command deploy all SD components needed to launch the tests and provision. 
For more details see at Makefile and docker-compose used there.
	
	```bash
	make deploy_netcracker
	```

	To launch the tests:

	```bash
	make test-netcracker


* **Urm-filter-cron**:
Basicly you can launch, this command deploy all SD components needed to launch the tests and provision. 
For more details see at Makefile and docker-compose used there.
	
	```bash
	make deploy_cron
	```

	To launch the tests:

	```bash
	make test-netcracker

 