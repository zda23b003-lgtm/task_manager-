from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# -------------------------
# DATABASE CONFIG
# -------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:passw0rd@localhost:3308/task_manager'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# -------------------------
# USER MODEL
# -------------------------
class User(db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship: user → tasks
    tasks = db.relationship("Task", backref="user", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at.isoformat()
        }


# -------------------------
# TASK MODEL
# -------------------------
class Task(db.Model):
    __tablename__ = "tasks_db"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Foreign Key → User
    user_id = db.Column(db.Integer, db.ForeignKey("Users.id"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat(),
            "user_id": self.user_id
        }


# -------------------------
# CREATE TABLES
# -------------------------
with app.app_context():
    db.create_all()
    print("Database tables created!")


# ======================================================
#                 USER CRUD ENDPOINTS
# ======================================================

# CREATE USER
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()

    if not data or 'username' not in data or 'email' not in data:
        return jsonify({"error": "username and email are required"}), 400

    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 201


# GET ALL USERS
@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users]), 200


# GET SINGLE USER
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user.to_dict()), 200


# UPDATE USER
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)

    db.session.commit()
    return jsonify(user.to_dict()), 200


# DELETE USER
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted"}), 200


# GET ALL TASKS OF A USER
@app.route('/api/users/<int:user_id>/tasks', methods=['GET'])
def get_user_tasks(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify([task.to_dict() for task in user.tasks]), 200


# ======================================================
#                     TASK ENDPOINTS
# ======================================================

# CREATE TASK
@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()

    if not data or 'title' not in data or 'user_id' not in data:
        return jsonify({"error": "title and user_id are required"}), 400

    # Check if user exists
    user = User.query.get(data['user_id'])
    if not user:
        return jsonify({"error": "User does not exist"}), 404

    new_task = Task(
        title=data['title'],
        description=data.get('description', ''),
        user_id=data['user_id']
    )

    db.session.add(new_task)
    db.session.commit()

    return jsonify(new_task.to_dict()), 201


# GET COMPLETED TASKS
@app.route('/api/tasks/completed', methods=['GET'])
def get_completed_tasks():
    tasks = Task.query.filter_by(completed=True).all()
    return jsonify([t.to_dict() for t in tasks]), 200


# SEARCH TASKS
@app.route('/api/tasks/search', methods=['GET'])
def search_tasks():
    q = request.args.get('q', '')

    if q == '':
        return jsonify({"error": "Search term 'q' is required"}), 400

    tasks = Task.query.filter(Task.title.ilike(f"%{q}%")).all()
    return jsonify([t.to_dict() for t in tasks]), 200


# ======================================================
#                   RUN APP
# ======================================================
if __name__ == '__main__':
    app.run(debug=True, port=6000)
