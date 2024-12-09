from models import app, init_db
import routes  # Import routes to register endpoints

if __name__ == '__main__':
    with app.app_context():
        init_db()  # Initialize the database
    app.run(debug=True)
