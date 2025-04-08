from src.app_instance import app
from src.layouts import create_layout
import src.callbacks

# Inicializar la app Dash
app.layout = create_layout()

if __name__ == '__main__':
    app.run(debug=True)