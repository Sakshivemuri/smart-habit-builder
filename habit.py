# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///habits.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# -------------------- MODELS --------------------

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

class HabitLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    habit_id = db.Column(db.Integer, nullable=False)
    log_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Boolean, nullable=False)

# -------------------- AUTH --------------------

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    user = User(username=data['username'], password=data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username'], password=data['password']).first()
    if user:
        return jsonify({"message": "Login successful", "user_id": user.id})
    return jsonify({"message": "Invalid credentials"}), 401

# -------------------- HABIT MANAGEMENT --------------------

@app.route('/habit', methods=['POST'])
def create_habit():
    data = request.json
    habit = Habit(name=data['name'], user_id=data['user_id'])
    db.session.add(habit)
    db.session.commit()
    return jsonify({"message": "Habit created"})

@app.route('/habits/<int:user_id>', methods=['GET'])
def get_habits(user_id):
    habits = Habit.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": h.id, "name": h.name} for h in habits])

# -------------------- HABIT LOGGING --------------------

@app.route('/habit/log', methods=['POST'])
def log_habit():
    data = request.json
    log = HabitLog(
        habit_id=data['habit_id'],
        log_date=date.today(),
        status=data['status']
    )
    db.session.add(log)
    db.session.commit()
    return jsonify({"message": "Habit logged"})

# -------------------- STREAK CALCULATION --------------------

@app.route('/habit/streak/<int:habit_id>', methods=['GET'])
def habit_streak(habit_id):
    logs = HabitLog.query.filter_by(habit_id=habit_id, status=True).order_by(HabitLog.log_date.desc()).all()
    streak = 0
    prev_date = None

    for log in logs:
        if prev_date is None or (prev_date - log.log_date).days == 1:
            streak += 1
            prev_date = log.log_date
        else:
            break

    return jsonify({"streak": streak})

# -------------------- PROGRESS VISUAL DATA --------------------

@app.route('/habit/progress/<int:habit_id>', methods=['GET'])
def habit_progress(habit_id):
    logs = HabitLog.query.filter_by(habit_id=habit_id).all()
    return jsonify([
        {"date": str(log.log_date), "status": log.status}
        for log in logs
    ])

# -------------------- MOTIVATION MESSAGE --------------------

@app.route('/motivation', methods=['GET'])
def motivation():
    messages = [
        "Consistency beats motivation!",
        "One day at a time 💪",
        "Small habits make big changes",
        "Keep going, you're doing great!"
    ]
    return jsonify({"message": messages[date.today().day % len(messages)]})

# -------------------- RUN --------------------

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    