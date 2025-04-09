from dash.dependencies import Input, Output
import plotly.express as px
from plotly.colors import n_colors
from src.app_instance import app
from src.get_data import get_data
from typing import Optional, List, Tuple

@app.callback(
    [Output('sales-chart', 'figure'),  
     Output('growth-chart', 'figure')],
    [Input('segment-filter', 'value'), 
     Input('category-filter', 'value'),     
     Input('time-resolution', 'value')])

def update_charts(segments: Optional[List[str]],
                    categories: Optional[List[str]],
                    time_resolution: str
                ):
    """
    Updates sales and growth charts based on user filters.
    
    Args:
        segments: Selected item segments to filter by
        categories: Selected categories to filter by
        time_resolution: Time period resolution ('quarter' or 'month')
    
    Returns:
        Tuple containing:
        - sales_fig: Figure object for sales chart
        - growth_fig: Figure object for growth chart
    """
    # Get filtered data
    sales_data, growth_data, x_col = get_data(segments, categories, time_resolution)

    # Create graphs
    # Sales graph
    sales_fig = px.bar(
        sales_data,
        x = x_col,
        y ='value',
        text ='value',
        color='value',
        color_continuous_scale= px.colors.sequential.YlGn,
        title = f'Total Sales by {"Quarter" if time_resolution == "quarter" else "Month"} (MM)',
        labels = {'value': 'Total Sales (USD)', x_col: 'Period'}
    )

    sales_fig = update_graph(sales_fig)

    # Growth graph
    growth_fig = px.bar(
        growth_data,
        x = x_col,
        y ='yoy_growth',
        text ='yoy_growth',
        color='yoy_growth',
        color_continuous_scale= n_colors('rgb(245, 24, 32)', 'rgb(0,128,0)', len(growth_data), colortype='rgb'),
        title =f'Year-on-year growth by {"Quarter" if time_resolution == "quarter" else "Month"} (%)',
        labels ={'yoy_growth': 'Growth (%)', x_col: 'Period'},
    )
    growth_fig = update_graph(growth_fig, 'growth')

    return sales_fig, growth_fig

def update_graph(graph_fig, graph_type=''):
    """
    Updates sales and growth graphs withan specific and burned style.
    
    Args:
        graph_fig: Selected item segments to filter by
        graph_type: Graph type for choosing how many decimals
          will be showed in the plot ('sales':0 decimal or 'growth':1 decimal)
    
    Returns:
        - graph_fig: Figure object for sales or growth chart
    """
    _texttemplate = ['%{text:,.1f}' if graph_type == 'growth'
                      else '%{text:,.0f}'][0]

    return graph_fig.update_layout(coloraxis_showscale=False,
            title={
                'y':0.95,
                'x':0.5,
                'font': {
                    'family': "Camphor Pro Heavy, sans-serif",
                    'size': 24,
                    'color': '#306B7E'
                }
            },
            # paper_bgcolor='rgba(0,0,0,0)',
            # plot_bgcolor='#ffffff',
            plot_bgcolor='white',  # Fondo blanco
            yaxis=dict(
                showgrid=True,
                gridcolor='#f0f0f0',
            ),
            ).update_traces(
            texttemplate=_texttemplate,
            textposition='outside'
        )