from application.db.people import *
from application.salary import *
from datetime import *
if __name__ == '__main__':
    get_employees()
    calculate_salary()
    print(datetime.today())
