import datetime as dt

class Record:
    def __init__(self, amount, comment, date = ''):
        self.amount = amount
        self.comment = comment
        if date == '':
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        self.USD_RATE = 55
        self.EUR_RATE = 60

class Calculator:
    def __init__(self, limit):
        self.records = []
        self.limit = limit

class CashCalculator(Calculator):
    #def __init__(self, limit):
        #super().__init__(self, limit)

    def add_record(self, record):
        self.records.append(record)
    
    def get_today_stats(self):
        spending = 0
        for i in self.records:
            if i.date == dt.datetime.now().date(): spending += i.amount
        return spending
    
    def get_today_cash_remained(self, currency):
        spending = self.get_today_stats()
        if (self.limit - spending > 0):
            print(f"На сегодня осталось {self.limit - spending} {currency}\n")
        elif (self.limit - spending == 0):
            print(f"Денег нет, держись\n")
        else:
            print(f"Денег нет, держись: твой долг – {spending - self.limit} {currency}\n")

cash_calculator = CashCalculator(1000)

cash_calculator.add_record(Record(amount=145, comment="кофе")) 
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
                
print(cash_calculator.get_today_cash_remained("rub"))




