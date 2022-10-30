from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product_mock = {
        "id": 26,
        "nome_do_produto": "flour",
        "nome_da_empresa": "food company",
        "data_de_fabricacao": "10-31-2022",
        "data_de_validade": "01-31-2023",
        "numero_de_serie": "D1D4 55FF U8I7 E7W8 9",
        "instrucoes_de_armazenamento": "sheltered from light",
    }

    product = Product(**product_mock)

    expect = (
        "O produto flour fabricado em 10-31-2022"
        " por food company com validade"
        " até 01-31-2023"
        " precisa ser armazenado sheltered from light."
    )

    assert str(product) == expect
