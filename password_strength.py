from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def evaluate_password(password):
    score = 0
    feedback = []

    # Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password Should Be At Least 8 Characters Long.")

    # Uppercase
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add At Least One Uppercase Letter.")

    # Lowercase
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add At Least One Lowercase Letter.")

    # Digit
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add At Least One Number.")

    # Special character
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add At Least One Special Character (!@#$%^&*(),.?\":{}|<>).")

    return {"score": score, "feedback": feedback}

@app.route("/strength", methods=["POST"])
def strength():
    data = request.get_json()
    password = data.get("password", "")
    result = evaluate_password(password)
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=5001, debug=True)