from flask import Flask
from flask_migrate import Migrate
from models import db, Employee, Department

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection to the local file app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# Configure flag to disable modification tracking and use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

# Initialize the Flask application to use the database
db.init_app(app)

# Define routes or views here if needed
@app.route('/')
def index():
    return "Welcome to the Flask Application with Migrations!"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
