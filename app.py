from src.app_instance import app
from src.layouts import create_layout
from src.get_data import load_and_preprocess_data
import src.callbacks

def initialize_app() -> None:
    """
    Initialize and configure the Dash application.
    
    This function:
    1. Loads and preprocesses the data
    2. Creates the application layout
    3. Registers all callbacks (via imports)
    """
    # Load and prepare data
    df = load_and_preprocess_data()
    
    # APP Title
    app.title = "YipitData Sales Analytics Dashboard"

    # Build the UI layout
    app.layout = create_layout(df)
    
    # Callbacks are registered through the src.callbacks import


def run_application() -> None:
    """Run the Dash application with development settings."""
    app.run(debug=True)

if __name__ == '__main__':
    initialize_app()
    run_application()