import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path_csv: str, type_report: str):
        with open(path_csv, mode="r", encoding="utf-8") as file:
            file_reader = csv.DictReader(file)
            product_list = list(file_reader)

        if type_report == "simples":
            return SimpleReport.generate(product_list)

        if type_report == "completo":
            return CompleteReport.generate(product_list)
