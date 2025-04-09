import dash
def create_dash_app():
    """Create and configurate an instance of the Dash app
    Returns:
        dash.Dash: Instance of the Dash app configurated.
    """
    # Configuración de metatags para responsividad
    meta_tags = [
        {
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1.0'
        }
    ]
    
    # Creación de la aplicación Dash
    app = dash.Dash(
        __name__,
        assets_folder='../assets',
        meta_tags=meta_tags
    )
    
    return app


# Instancia principal de la aplicación
app = create_dash_app()