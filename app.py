from flask import Flask
from flasgger import Swagger
from flask_cors import CORS
from api.schema import ma

from api.routes.rifa_route import rifa_api
from api.routes.ticket_route import tickets_api

from api.models import db, migrate
from api.models.ticket_model import Ticket
from api.models.rifa_model import Rifa

def create_app():
    app = Flask(__name__)
    app.config['SWAGGER'] = {'title': 'Tickets API'}
    app.config['SECRET_KEY'] = 'the main key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sorteos.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    swagger = Swagger(app)
    # Swagger.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)
    cors = CORS(app)
    # CORS.init_app(app)
    ma.init_app(app)

    app.register_blueprint(rifa_api, url_prefix='/rifas')
    app.register_blueprint(tickets_api, url_prefix='/tickets')

    setup_db(app)
    return app

def setup_db(app):
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()
    db.create_all()

    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db, Ticket=Ticket, Rifa=Rifa)
    
    app.run(host='0.0.0.0', port=port,debug=True)