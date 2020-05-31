from swagger_server.models.produtos_model import tb_produto
import json


def listar_produtos(black_friday=None):
    lista_de_produtos = []
    if black_friday:
        pass
    else:
        query = tb_produto.select()

    for row in query:
        json_data = json.loads(row.json_data)
        produto = {
            row.id: json_data
        }
        lista_de_produtos.append(produto)

    return lista_de_produtos
