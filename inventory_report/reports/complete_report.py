from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __products_stocked_by_company(product_list):
        company_name = [produto["nome_da_empresa"] for produto in product_list]
        quantity_product_per_company = Counter(company_name)
        str_result = "Produtos estocados por empresa:\n"
        for item in quantity_product_per_company:
            str_result += (
                f"- {item}: {quantity_product_per_company.get(item)}\n"
            )

        return str_result

    @classmethod
    def generate(cls, product_list):
        return (
            f"{super().generate(product_list)}\n"
            f"{cls.__products_stocked_by_company(product_list)}"
        )
