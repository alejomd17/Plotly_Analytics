import dash
app = dash.Dash(__name__, assets_folder='../assets',
    meta_tags=[{
        'name': 'viewport',
        'content': 'width=device-width, initial-scale=1.0'
    }]
)