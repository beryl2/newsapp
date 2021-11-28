
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options


bootstrap = Bootstrap()
def create_app(Config_name):
    app = Flask(__name__,instance_relative_config = True)

#check on this line 11 
    app.config.from_object(config_options[Config_name])
    
    bootstrap.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    from .requests import configure_request
    configure_request(app)


    return app

    