from datetime import date
class Date:
    @classmethod
    def date_to_num(cls, date):
        return ".".join(date.split("-"))
    @staticmethod
    def validation(dateq):
        try:
            q = date(int(str(dateq).split("-")[2]), int(str(dateq).split("-")[1]), int(str(dateq).split("-")[0]))
            return "число существует"
        except:
            return "не существуещее число"


print(Date.date_to_num("01-01-1024"))
print(Date.validation("31-12-2013"))
