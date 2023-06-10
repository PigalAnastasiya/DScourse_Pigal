from datetime import date
from datetime import datetime

'''Describes the work of the veterinarian , the intake report and recommendations are saved in the file reporte.txt'''


class Veterenar:
    def __init__(self, name):
        self.__name = name

    @property
    def get_name(self) -> None:
        return f"{self.__name}"

    def set_target(self, target):
        self.target = target
        self.examine(target)

    @staticmethod
    def write_report(text) -> None:
        with open("homework18_05/data/reporte.txt", "w", encoding="utf-8")as f:
            f.write(text)

    @staticmethod
    def examine(target) -> None:
        today = date.today()
        print("{}.{}.{}".format(today.day, today.month, today.year))
        print("Data on the subject animal:")
        result = target.description()
        created_report = datetime.now().strftime('%Y_%m_%d')
        report_text = input("Please type the result of the vet examination: ")
        Veterenar.write_report(
            f"{created_report} \n {report_text}")
