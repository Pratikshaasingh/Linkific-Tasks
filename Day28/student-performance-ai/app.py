"""
AI-Powered Student Performance Prediction System - Refactored Flask Backend API
Framework: Flask, Scikit-learn, Pandas, NumPy, Joblib
"""
import os
import logging
import joblib
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='static', template_folder='templates')

MODEL_PATH = "model.pkl"

def get_or_train_model() -> RandomForestRegressor:
    """Load pre-trained model or train a new instance using synthetic academic data."""
    if os.path.exists(MODEL_PATH):
        logger.info("Loading existing model from %s", MODEL_PATH)
        return joblib.load(MODEL_PATH)
    
    logger.info("Training new RandomForestRegressor model on synthetic dataset...")
    np.random.seed(42)
    n_samples = 500
    prev_marks = np.random.uniform(40, 100, n_samples)
    attendance = np.random.uniform(50, 100, n_samples)
    assignment_score = np.random.uniform(40, 100, n_samples)
    study_hours = np.random.uniform(1, 10, n_samples)
    participation = np.random.uniform(1, 10, n_samples)

    final_marks = (
        0.35 * prev_marks + 
        0.25 * attendance + 
        0.20 * assignment_score + 
        0.10 * (study_hours * 10) + 
        0.10 * (participation * 10) + 
        np.random.normal(0, 3, n_samples)
    )
    final_marks = np.clip(final_marks, 0, 100)

    df = pd.DataFrame({
        'prev_marks': prev_marks,
        'attendance': attendance,
        'assignment_score': assignment_score,
        'study_hours': study_hours,
        'participation': participation,
        'final_marks': final_marks
    })

    X = df[['prev_marks', 'attendance', 'assignment_score', 'study_hours', 'participation']]
    y = df['final_marks']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    joblib.dump(model, MODEL_PATH)
    logger.info("Model successfully trained and saved to %s", MODEL_PATH)
    return model

model = get_or_train_model()
PREDICTION_RECORDS = []

@app.route('/')
def home():
    """Render the main web dashboard portal."""
    return render_template('index.html')

@app.route('/api/v1/health', methods=['GET'])
def health_check():
    """Verify API health status and model readiness."""
    return jsonify({
        "status": "healthy",
        "service": "AI-Powered Student Performance Prediction System",
        "model_loaded": model is not None
    }), 200

@app.route('/api/v1/predict', methods=['POST'])
def predict():
    """Accept academic parameters, evaluate model inference, and output prediction metrics."""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid or missing JSON payload."}), 400

        required_fields = ['student_name', 'prev_marks', 'attendance', 'assignment_score', 'study_hours', 'participation']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        student_name = str(data['student_name']).strip()
        prev_marks = float(data['prev_marks'])
        attendance = float(data['attendance'])
        assignment_score = float(data['assignment_score'])
        study_hours = float(data['study_hours'])
        participation = float(data['participation'])

        features = np.array([[prev_marks, attendance, assignment_score, study_hours, participation]])
        predicted_score = float(model.predict(features)[0])
        predicted_score = round(np.clip(predicted_score, 0, 100), 2)

        if predicted_score >= 75:
            risk_level = "Low Risk (High Performing)"
            need_support = False
            recommendation = "Maintain current study routine and join advanced peer study groups."
        elif predicted_score >= 50:
            risk_level = "Medium Risk (Moderate)"
            need_support = True
            recommendation = "Focus on weak subject areas and increase weekly study hours."
        else:
            risk_level = "High Risk (Requires Academic Intervention)"
            need_support = True
            recommendation = "Immediate faculty counseling and mandatory remedial classes required."

        record = {
            "id": len(PREDICTION_RECORDS) + 1,
            "student_name": student_name,
            "prev_marks": prev_marks,
            "attendance": attendance,
            "assignment_score": assignment_score,
            "study_hours": study_hours,
            "participation": participation,
            "predicted_score": predicted_score,
            "risk_level": risk_level,
            "need_support": need_support,
            "recommendation": recommendation
        }

        PREDICTION_RECORDS.append(record)
        return jsonify({"status": "success", "data": record}), 200

    except ValueError:
        return jsonify({"error": "Invalid data format. Please check numeric inputs."}), 400
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

@app.route('/api/v1/records', methods=['GET'])
def get_records():
    """Retrieve historical prediction records."""
    return jsonify({
        "status": "success",
        "total_records": len(PREDICTION_RECORDS),
        "records": PREDICTION_RECORDS
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)