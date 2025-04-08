import pandas as pd

def get_data():
    df = pd.read_csv('./data/dataset.csv')
    df = fix_datetime_columns(df)
    return df

def fix_datetime_columns(df):
    for c in ['date','quarter_start','quarter_end']:
        df[c] = pd.to_datetime(df[c])

    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['quarter'] = df['date'].dt.quarter
    df['year_quarter'] = df['year'].astype(str) + 'Q' + df['quarter'].astype(str)
    df['year_month'] = df['date'].dt.strftime('%Y-%m')

    return df

def calculate_yoy_growth(df, group_col):
    df = df.sort_values([group_col, 'year'])
    df['prev_year_value'] = df.groupby([group_col.split('_')[1] if '_' in group_col else group_col])['value'].shift(1)
    df['yoy_growth'] = (df['value'] - df['prev_year_value']) / df['prev_year_value'] * 100
    
    return df

