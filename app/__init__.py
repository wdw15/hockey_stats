# __init__.py
from flask import Flask
from dotenv import load_dotenv

load_dotenv()  # loads .env file once here

# now import utilities which can safely use os.getenv(...)
from app.utilities import nhl_api, data_ingest


def create_app():
    load_dotenv()  # load environment variables once when app starts
    app = Flask(__name__)
    
    from .routes import main
    app.register_blueprint(main)

    return app

