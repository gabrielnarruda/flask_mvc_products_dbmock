#!/usr/bin/env python3

import connexion



def main():
    app = connexion.FlaskApp(__name__, specification_dir='./swagger/')
    app.add_api('swagger.yaml')
    app.run(port=8080)


if __name__ == '__main__':
    main()
