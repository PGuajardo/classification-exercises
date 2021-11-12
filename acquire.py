import env
import pandas as pd
import os

#Gets connection to Code Up database using env file
def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# Get titanic .csv Data
def get_titanic_data():
    filename = "titanic.csv"

    if os.path.isfile(filename):
        titanic = pd.read_csv(filename)
    else:
        titanic = pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))
        titanic.to_csv(index = False)
    return titanic


# Get iris .csv Data
def get_iris_data():
    filename = "iris.csv"

    if os.path.isfile(filename):
        iris = pd.read_csv(filename)
    else:
        iris = pd.read_sql('SELECT * FROM species JOIN measurements using(species_id)', get_connection('iris_db'))
        iris.to_csv(index = False)
    return iris


def get_telco_data():
    filename = "teleco_churn.csv"

    if os.path.isfile(filename):
        telco_churn = pd.read_csv(filename)
    else:
        telco_churn = pd.read_sql('SELECT * FROM customers JOIN contract_types using(contract_type_id) JOIN internet_service_types using(internet_service_type_id) JOIN payment_types using(payment_type_id)', 
        get_connection('telco_churn'))
        telco_churn.to_csv(index = False)
    return telco_churn