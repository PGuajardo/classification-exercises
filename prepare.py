import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import splitting and imputing functions
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# turn off pink boxes for demo
import warnings
warnings.filterwarnings("ignore")

# import our own acquire module
import acquire

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

def clean_data(df):
    '''
    This function will clean the data
    '''
    df = df.drop_duplicates()
    
    cols_to_drop = ['deck', 'embarked', 'class', 'age']
    df = df.drop(columns = cols_to_drop)
    
    df['embark_town'] = df.embark_town.fillna(value = 'Southampton')
    
    dummy_df = pd.get_dummies(df[['sex','embark_town']], dummy_na = False, drop_first = [True, True])
    
    df = pd.concat([df, dummy_df], axis = 1)
    
    return df

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#Takes in a dataframe and return train, validate, test subset dataframe
def split_data(df):
    train, test = train_test_split(df, test_size = .2, random_state = 123, stratify = df.survived)
    train, validate = train_test_split(train, test_size =  .3, random_state= 123, stratify = train.survived)
    return train, validate, test


#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

def impute_mode(train, validate, test):
    '''
    Takes in train, validate , test, and uses train to identify the best value to replace nulls in embark_town
    Imputes that values into all three sets and returns all three sets
    '''
    
    imputer = SimpleImputer(missing_values = np.nan, strategy = 'most_frequent')
    
    #imputer = imputer.fit(train[['embark_town']])
    train[['embark_town']] = imputer.fit_transform(train[['embark_town']])
    validate[['embark_town']] = imputer.fit_transform(validate[['embark_town']])
    test[['embark_town']] = imputer.fit_transform(test[['embark_town']])
    return train, validate, test

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
def prep_titanic_data(df):
    '''
    Ultimate dishwasher
    '''
    df = clean_data(df)
    train, validate, test = split_data(df)
    
    return train, validate, test