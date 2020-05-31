# O

## Overview

Este servidor foi criado utilizando  Flask como WSGI, 
Connexion como  Handler de requests, Peewee como ORM, 
SQLite3 com banco de dados e Swagger


## Requirements
Python 3.5.2+

flask
#### API requirements
werkzeug==0.16.0
connexion==1.5.3
setuptools >= 21.0.0

#### DB requirements
peewee==3.13.3

#### webhook signal
blinker==1.4

## Usage
To run the server, please execute the following from the root directory:

```
pip install -r requirements.txt
python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:8080/v2/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/v1/swagger.json
```


## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
```