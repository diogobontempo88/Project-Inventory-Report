import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:

    @staticmethod
    def readCSV(files: str):
        with open(files, encoding="utf-8") as file:
            inventory_reader = csv.DictReader(
                file, delimiter=",", quotechar='"'
            )
            list = []
            for my_file in inventory_reader:
                list.append(my_file)
        return list

    @staticmethod
    def readJSON(path):
        with open(path, encoding="utf-8") as file:
            inventory_reader = file.read()
            list = json.loads(inventory_reader)

        return list

    @staticmethod
    def readXML(path):
        with open(path, encoding="utf-8") as file:
            my_xml = file.read()
            inventory_reader = xmltodict.parse(my_xml)['dataset']['record']
        return inventory_reader

    @classmethod
    def path_extension(cls, file_path):
        if file_path.endswith('.csv'):
            return cls.readCSV(file_path)
        elif file_path.endswith('.json'):
            return cls.readJSON(file_path)
        elif file_path.endswith('.xml'):
            return cls.readXML(file_path)
       
    @classmethod
    def import_data(file, file_path, report_type):
        complete_report = CompleteReport()
        simple_report = SimpleReport()
        companies_list = file.path_extension(file_path)

        reply = (
          complete_report.generate(companies_list)
          if report_type == 'completo'
          else simple_report.generate(companies_list)
          )

        return reply