import sqlite3
import json
from swagger_server.configuration.data_mock.data import table_produtos_rows

db_conn = './db_produtos.db'


def create_table_mock():
    try:
        sqlite_connection = sqlite3.connect(db_conn)
        cursor = sqlite_connection.cursor()
        cursor.execute("CREATE TABLE tb_produto (id int, json_data json)")

    except sqlite3.Error as error:
        print("Error while executing sqlite script", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("sqlite connection is closed")


def insert_table_data_mock():
    try:
        sqlite_connection = sqlite3.connect('db_produtos.db')
        cursor = sqlite_connection.cursor()

        for register in table_produtos_rows.get("Produtos"):
            json_data = json.dumps(table_produtos_rows.get("Produtos").get(register))
            print(f"iniciando registo {register}", type(json_data))

            cursor.execute("INSERT INTO tb_produto(id, json_data)VALUES(?,?)", (register, json_data))

            print(f"Insercao do registro {register} executada com sucesso")
            sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Error while executing sqlite script", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("sqlite connection is closed")
