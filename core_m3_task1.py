import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        current_date = datetime.today().date()
        diff = current_date - input_date
        return diff.days
    except ValueError:
        return "Неправильний формат дати. Очікується 'РРРР-ММ-ДД'."