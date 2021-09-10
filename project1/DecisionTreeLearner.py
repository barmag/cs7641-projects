import pandas as pd

def load_tic_toe_data(data_path='./data/tic-tac-toe/tic-tac-toe.data'):
    return pd.read_csv(data_path)

if __name__ == '__main__':
    # path = './data/tic-tac-toe/tic-tac-toe.data'
    tic_tac_toe_data = load_tic_toe_data()
    print(tic_tac_toe_data.head())
    print(tic_tac_toe_data.describe())