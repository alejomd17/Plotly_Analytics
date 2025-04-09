import pandas as pd
from typing import Optional, List, Tuple

def get_data(segments: Optional[List[str]] = None,
            categories: Optional[List[str]] = None,
            time_resolution: str = 'quarter'
            ) -> Tuple[pd.DataFrame, pd.DataFrame, str]:
    """
    Load and process data for visualization
    
    Args:
        segments: List of segments to filter the dataframe
        categories: List of categorías to filter the dataframe
        time_resolution: 'quarter' or 'month' for temporary grouping
    
    Returns:
        - sales_data: DataFrame of sales
        - growth_data: DataFrame of year-to-year growth
        - x_col: Name of the column for x axis
    """
    df = load_and_preprocess_data()
    filtered_df = apply_filters(df, segments, categories)
    
    # Procesar datos de ventas
    sales_data = calculate_sales(filtered_df, time_resolution)
    
    # Calcular crecimiento interanual
    growth_data = calculate_growth(filtered_df, time_resolution)
    
    x_col = f'year_{time_resolution}'


    return sales_data, growth_data, x_col

def load_and_preprocess_data() -> pd.DataFrame:
    """Load and preprocess data base"""
    df = pd.read_csv('./data/dataset.csv')

    for c in ['date','quarter_start','quarter_end']:
        df[c] = pd.to_datetime(df[c])

    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['quarter'] = df['date'].dt.quarter
    df['year_quarter'] = df['year'].astype(str) + 'Q' + df['quarter'].astype(str)
    df['year_month'] = df['date'].dt.strftime('%Y%m')
    df = df[(df['year'] != 2022)]

    return df

def apply_filters(df: pd.DataFrame,
    segments: Optional[List[str]],
    categories: Optional[List[str]]
) -> pd.DataFrame:
    """Apply filters to DataFrame"""
    filtered_df = df.copy()
    
    if segments:
        filtered_df = filtered_df[filtered_df['item_segment'].isin(segments)]
    if categories:
        filtered_df = filtered_df[filtered_df['category_name'].isin(categories)]
    
    return filtered_df

def calculate_sales(df: pd.DataFrame, time_resolution: str) -> pd.DataFrame:
    """Calculate tha agreggated sales."""
    sales_data = (
        df.groupby([f'year_{time_resolution}'])['value']
        .sum()
        .reset_index()
    )
    sales_data['value'] = round(sales_data['value'] / 1_000_000, 1)  # Millions
    return sales_data

def calculate_growth(df: pd.DataFrame, time_resolution: str) -> pd.DataFrame:
    """Calculate the year-to-year growth"""
    grouped = df.groupby([f'year_{time_resolution}', time_resolution, 'year'])['value'].sum().reset_index()
    growth_data = calculate_yoy_growth(grouped, time_resolution)
    
    # Limpieza final
    growth_data = (
        growth_data[~growth_data['yoy_growth'].isna()]
        .sort_values([f'year_{time_resolution}'])
    )
    growth_data['yoy_growth'] = round(growth_data['yoy_growth'], 1)
    
    return growth_data

def calculate_yoy_growth(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    """
    Calculates year-over-year (YoY) growth.

    Args:
        df: DataFrame with grouped data
        group_col: Grouping column ('quarter' or 'month')

    Returns:
        DataFrame with calculated 'yoy_growth' column
    """

    df = df.sort_values([group_col, 'year'])
    
    # Calculate last year values
    df['prev_year_value'] = df.groupby([group_col])['value'].shift(1)
    df[f'prev_year_{group_col}'] = df.groupby([group_col])[f'year_{group_col}'].shift(1)
    
    # Format the tags for comparation
    df[f'year_{group_col}'] = (
        df[f'year_{group_col}'] + ' vs ' + df[f'prev_year_{group_col}']
    )
    
    # Calculate the percentage of growth
    df['yoy_growth'] = (
        (df['value'] - df['prev_year_value']) / df['prev_year_value'] * 100
    )
    
    return df

