from swagger_server.configuration.data_mock import data


def get_listar_produto_por_id(id_produto):  # noqa: E501
    """Retorna produto por ID

    Retorna produto por ID # noqa: E501

    :param id_produto: Busca por tabela_origem_dominio do domínio
    :type id_produto: int

    :rtype: Produto
    """
    return 'do some magic!'


def get_listar_produtos(black_friday=None):  # noqa: E501
    """Retorna lista de produtos completa

    Retorna lista de produtos completa # noqa: E501

    :param black_friday: Busca por produtos que fazem parte da Black Friday
    :type black_friday: bool

    :rtype: ProdutoVO
    """
    return data.db
