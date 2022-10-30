from datetime import datetime
from operator import itemgetter
import statistics


class SimpleReport:
    def __oldest_manufacture(product_list):
        new_product_list = sorted(
            product_list, key=itemgetter("data_de_fabricacao"), reverse=False
        )
        return new_product_list[0]["data_de_fabricacao"]

    def __nearest_expiration_date(product_list):
        current_date = datetime.today().date()
        lists_unexpired_products = [
            product
            for product in product_list
            if product["data_de_validade"] > str(current_date)
        ]
        new_product_list = sorted(
            lists_unexpired_products,
            key=itemgetter("data_de_validade"),
            reverse=False,
        )
        return new_product_list[0]["data_de_validade"]

    def __company_with_more_products(product_list):
        company_names = [name["nome_da_empresa"] for name in product_list]
        return statistics.mode(company_names)

    @classmethod
    def generate(cls, product_list):
        manufacturing_date = cls.__oldest_manufacture(product_list)
        expiration_date = cls.__nearest_expiration_date(product_list)
        company_name = cls.__company_with_more_products(product_list)

        return (
            f"Data de fabricação mais antiga: {manufacturing_date}\n"
            f"Data de validade mais próxima: {expiration_date}\n"
            f"Empresa com mais produtos: {company_name}"
        )
