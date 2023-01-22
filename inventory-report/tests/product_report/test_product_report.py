from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto = Product(
        11,
        "prateleira",
        "Metalbon",
        "06/10/2022",
        "06/10/2023",
        "12345",
        "manter limpo",
    )
    
    assert produto.id == 11
    assert produto.nome_do_produto == "prateleira"
    assert produto.nome_da_empresa == "Metalbon"
    assert produto.data_de_fabricacao == "06/10/2022"
    assert produto.data_de_validade == "06/10/2023"
    assert produto.numero_de_serie == "12345"
    assert produto.instrucoes_de_armazenamento == "manter limpo"

