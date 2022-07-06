import datetime as dt

class Record:
    def __init__(self, amount, comment, date = ''):
        self.amount = amount
        self.comment = comment
        if date == '':
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class Calculator:
    def __init__(self, limit):
        self.records = []
        self.limit = limit
    
    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        spending = 0
        for i in self.records:
            if i.date == dt.datetime.now().date(): spending += i.amount
        return spending


class CashCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)
        self.USD_RATE = 55
        self.EUR_RATE = 60
    
    def get_today_cash_remained(self, currency):
        left = (self.limit - self.get_today_stats())
        if currency == 'eur':
            left /= self.EUR_RATE
        elif currency == 'usd':
            left /= self.USD_RATE
        
        if (left > 0):
            return (f'На сегодня осталось {left} {currency}')
        elif (self.left == 0):
            return (f'Денег нет, держись')
        else:
            return (f'Денег нет, держись: твой долг – {-left} {currency}')
    
    def get_week_stats(self):
        spending = 0
        for i in self.records:
            if i.date >= (dt.datetime.now().date() - dt.timedelta(weeks = 7))  and i.date <= dt.datetime.now().date(): 
                spending += i.amount
        return spending


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        left = (self.limit - self.get_today_stats())
        if (left > 0):
            return (f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {left} кКал\n')
        else:
            return (f'Хватит есть!\n')


cash_calculator = CashCalculator(1000)

cash_calculator.add_record(Record(amount=145, comment='кофе')) 
cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
cash_calculator.add_record(Record(amount=3000, comment='бар в Танин др', date='08.11.2019'))
                
print(cash_calculator.get_today_cash_remained("eur"))
print(cash_calculator.get_today_cash_remained("rub"))
print(cash_calculator.get_week_stats())




