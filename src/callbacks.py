from dash.dependencies import Input, Output
import plotly.express as px
from src.app_instance import app
from src.get_data import calculate_yoy_growth
from src.get_data import get_data

@app.callback(
    [Output('sales-chart', 'figure'),  
     Output('growth-chart', 'figure')],
    [Input('segment-filter', 'value'), 
     Input('category-filter', 'value'),     
     Input('time-resolution', 'value')])

def update_charts(segments, categories, time_resolution):
    df = get_data()

    filtered_df = df.copy()
    if segments:
        filtered_df = filtered_df[filtered_df['item_segment'].isin(segments)]
    if categories:
        filtered_df = filtered_df[filtered_df['category_name'].isin(categories)]
    
    # Actualizar datos agregados
    if time_resolution == 'quarter':
        sales_data = filtered_df.groupby(['year_quarter', 'quarter_start'])['value'].sum().reset_index()
        growth_data = calculate_yoy_growth(
            filtered_df.groupby(['quarter', 'year'])['value'].sum().reset_index(), 
            'quarter'
        )
        x_col = 'year_quarter'
        growth_x_col = 'quarter'
    else:
        sales_data = filtered_df.groupby(['year_month', 'year', 'month'])['value'].sum().reset_index()
        growth_data = calculate_yoy_growth(
            filtered_df.groupby(['month', 'year'])['value'].sum().reset_index(),
            'month'
        )
        x_col = 'year_month'
        growth_x_col = 'month'
    
    # Crear gráficos
    sales_fig = px.bar(
        sales_data,
        x=x_col,
        y='value',
        title=f'Total Sales by {"Trimestre" if time_resolution == "quarter" else "Mes"}',
        labels={'value': 'Total Sales (USD)', x_col: 'Período'}
    )
    
    growth_fig = px.line(
        growth_data,
        x=growth_x_col,
        y='yoy_growth',
        color='year',
        title=f'Crecimiento Interanual por {"Trimestre" if time_resolution == "quarter" else "Mes"}',
        labels={'yoy_growth': 'Crecimiento (%)', growth_x_col: 'Período'}
    )
    
    return sales_fig, growth_fig