#from application.salary import calculate_salary
#from application.db.people import get_employees

#calculate_salary()
#get_employees()

import datetime as dt
import application.db.people as ap
import application.salary as asy

if __name__ == "__main__":
    print(f'''
    Сегодняшняя дата и время: {dt.datetime.today()}
    ''')
    ap.get_employees()
    asy.calculate_salary()


