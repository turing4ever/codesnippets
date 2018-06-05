import pandas as pd

def lego(df):
    print('passed in: ', id(df))
    df = df[df['a']==1]
    print('after assignment: ', id(df))
    print(df)

if __name__ == '__main__':
    a = pd.DataFrame({'a':[1,2], 'b':[3,4]})
    print('a: ', id(a))
    lego(a)
