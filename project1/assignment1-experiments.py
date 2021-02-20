import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
if __name__ == '__main__':
    # load data
    path = './data/adult.data'
    adult_data = pd.read_csv(path)
    print(adult_data.head())

    # load amazon customer reviews
    path = './data/amazon-customer-reviews.csv'
    adult_data = pd.read_csv(path)
    print(adult_data.head())
    pass
