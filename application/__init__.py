from flask import Flask
from dotenv import load_dotenv
from datetime import timedelta
from logging import Logger
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from logging import Logger
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt 
from flask_jwt_extended import JWTManager
from flask_caching import Cache

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# @cross_origin()

DB_URL="postgresql+psycopg2://qpecxbnk:zNXuEFs0JEA4WvsrArZAjjZtPv8sOUM1@drona.db.elephantsql.com/qpecxbnk"
DB="sqlite:///project.db"
# CORS(app,
#        resources={r"/*": {"origins": "*"}},
#         supports_credentials=True,
#      )
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config["SQLALCHEMY_DATABASE_URI"] = DB
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "your-secret-key"        
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)


bycrypt = Bcrypt(app)
db=SQLAlchemy(app)
migrate = Migrate(app, db)

config ={
    "DEBUG":True,
    "CACHE_TYPE":"SimpleCache",
    "CACHE_DEFAULT_TIMEOUT":300
}
app.config.from_mapping(config)
cache = Cache(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


from application.src.http.controllers.AuthController import auth
from application.src.http.controllers.PaymentController import payment_route
from application.src.http.controllers.TransactionController import transaction
from application.src.http.controllers.ChargeController import charge
from application.src.http.controllers.GatewayController import gateway
from application.src.http.controllers.ProfileController import profile
from application.src.http.controllers.RecipientController import recipient
from application.src.http.controllers.SendMoneyController import send_money

app.register_blueprint(auth)
app.register_blueprint(charge)
app.register_blueprint(gateway)
app.register_blueprint(profile)
app.register_blueprint(payment_route)
app.register_blueprint(recipient)
app.register_blueprint(send_money)
app.register_blueprint(transaction)