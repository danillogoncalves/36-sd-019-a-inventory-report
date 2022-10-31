import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def __read_csv(path: str):
        with open(path, mode="r", encoding="utf-8") as file:
            file_reader = csv.DictReader(file)
            return list(file_reader)

    def __read_json(path: str):
        with open(path, mode="r", encoding="utf-8") as file:
            return json.loads(file.read())

    def __read_xml(path: str):
        with open(path, mode="r", encoding="utf-8") as file:
            return xmltodict.parse(file.read())["dataset"]["record"]

    def __type_report_switch(type_report, product_list):
        if type_report == "simples":
            return SimpleReport.generate(product_list)

        if type_report == "completo":
            return CompleteReport.generate(product_list)

    @classmethod
    def import_data(cls, path: str, type_report: str):
        if path.endswith(".csv"):
            product_list = cls.__read_csv(path)
        if path.endswith(".json"):
            product_list = cls.__read_json(path)
        if path.endswith(".xml"):
            product_list = cls.__read_xml(path)

        return cls.__type_report_switch(type_report, product_list)
