from dash import html, dcc
import pandas as pd

def create_layout(df: pd.DataFrame) -> html.Div:
    """
    Creates the main layout for the Sales Analysis dashboard.
    
    Args:
        df: DataFrame containing the data for filter options
        
    Returns:
        A Dash HTML Div containing the complete dashboard layout
    """
    layout =  html.Div(
        className="app-container",
        children=[
        html.H1("Sales Analysis", className="app-title"),
        html.Div(
            className="filter-container",
            children=[
                html.Div(
                    className="dropdown-row",
                    children = [
                        html.Div(
                            className="dropdown-container",
                            children=
                            [
                            html.Label("Filter by Segment:", className="filter-label"),
                                dcc.Dropdown(
                                    id='segment-filter',
                                    options=[{'label': seg, 'value': seg} for seg in df['item_segment'].unique()],
                                    multi=True,
                                    placeholder='Select segment',
                                    className='custom-dropdown'
                                )
                            ]),

                        html.Div(
                            className="dropdown-container",
                            children = [
                            html.Label("Filter by Category:", className="filter-label"),
                            dcc.Dropdown(
                                id='category-filter',
                                options=[{'label': cat, 'value': cat} for cat in df['category_name'].unique()],
                                multi=True,
                                placeholder='Select category',
                                className='custom-dropdown'
                                )
                            ]
                            ),
                    ]),

            html.Div(
                className="radio-row",
                children = [
                        html.Label("Frequency:", className="filter-label"),
                        dcc.RadioItems(
                            id='time-resolution',
                            options=[
                                {'label': 'Quarter', 'value': 'quarter'},
                                {'label': 'Month', 'value': 'month'}
                            ],
                            value='quarter',
                            inline=True,
                            labelClassName='radio-option',
                            className='radio-container'
                            )
                        ])
                    ]
                ),

        html.Div(
            className="graphs-container",
            children=[
            dcc.Graph(id='sales-chart'),
            dcc.Graph(id='growth-chart')])
        ]
    )

    return layout