from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "ball",
        "sporting-goods-store-ltda",
        "10-30-2022",
        "10-20-2032",
        "LV23 ELDS 2GD5 X19P VCSI K",
        "não deixar em um local umido",
    )

    print(product.id)
    assert product.id == 1
    assert product.nome_do_produto == "ball"
    assert product.nome_da_empresa == "sporting-goods-store-ltda"
    assert product.data_de_fabricacao == "10-30-2022"
    assert product.data_de_validade == "10-20-2032"
    assert product.numero_de_serie == "LV23 ELDS 2GD5 X19P VCSI K"
    assert (
        product.instrucoes_de_armazenamento == "não deixar em um local umido"
    )
