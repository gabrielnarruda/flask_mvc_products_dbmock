#!/usr/bin/env python3

import connexion
from swagger_server.configuration.logger import create_logger

db_conn = './db_produtos.db'

#logger = create_logger()

def main():
    app = connexion.FlaskApp(__name__, specification_dir='./swagger/')
    app.add_api('swagger.yaml')
    app.run(port=8080)


if __name__ == '__main__':
    main()
