import pandas as pd

def load_data():
    train = pd.read_csv('./data/redwine_train.csv')
    test = pd.read_csv('./data/redwine_test.csv')

    return train, test

def save_data(df1, df2, STUDENT_ID):
    df1.to_csv(f'{STUDENT_ID}_simple_seq.p1.answer.csv')
    df2.to_csv(f'{STUDENT_ID}_simple_seq.p2.answer.csv')
