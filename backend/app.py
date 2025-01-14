from flask import Flask, request, jsonify
from models import db, User, Application
from auth import login_required, authenticate_user
from analytics import generate_trends

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password1@localhost:5432/applyplacid'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    return authenticate_user(data['email'], data['password'])

@app.route('/applications', methods=['POST'])
@login_required
def add_application(user_id):
    data = request.json
    new_application = Application(user_id=user_id, **data)
    db.session.add(new_application)
    db.session.commit()
    return jsonify({"message": "Application added successfully!"}), 201

@app.route('/applications', methods=['GET'])
@login_required
def get_applications(user_id):
    applications = Application.query.filter_by(user_id=user_id).all()
    return jsonify([app.to_dict() for app in applications])

@app.route('/analytics', methods=['GET'])
@login_required
def analytics(user_id):
    trends = generate_trends(user_id)
    return jsonify(trends)

if __name__ == '__main__':
    app.run(debug=True)
