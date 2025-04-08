from dash import html, dcc
from src.get_data import get_data


def create_layout():
    df = get_data()

    layout =  html.Div(
        className="app-container",
        children=[
        html.H1("Sales Analysis", className="app-title"),
        
        html.Div(
            className="filter-container",
            children=[
            html.Div([
                html.Label("Filter by Segment:", className="filter-label"),
                    dcc.Dropdown(
                        id='segment-filter',
                        options=[{'label': seg, 'value': seg} for seg in df['item_segment'].unique()],
                        multi=False,
                        placeholder='Select segment',
                        className='custom-dropdown'
                    )
                ]),

            html.Div([
                html.Label("Filter by Category:", className="filter-label"),
                dcc.Dropdown(
                    id='category-filter',
                    options=[{'label': cat, 'value': cat} for cat in df['category_name'].unique()],
                    multi=False,
                    placeholder='Select category',
                    className='custom-dropdown'
                    )
                ]),

            html.Div([
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
            dcc.Graph(id='growth-chart')
        ]
        )
    ])

    return layout