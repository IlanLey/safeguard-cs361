from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Good Rotational Password Time Period
PASSWORD_MAX_AGE_DAYS = 90

@app.route("/check_password_age", methods=["POST"])
def check_password_age():
    data = request.get_json()
    last_changed = data.get("last_changed") if data else None

    if not last_changed:
        return jsonify({"days_old": None, "status": "Error", "message": "Missing 'last_changed' Date (YYYY-MM-DD)"})

    try:
        last_changed_date = datetime.strptime(last_changed, "%Y-%m-%d")
    except ValueError:
        return jsonify({"days_old": None, "status": "Error", "message": "Invalid Date Format, Expected YYYY-MM-DD"})

    # Checks the Days Old
    days_old = (datetime.now() - last_changed_date).days

    # Check 90 Day Threshold
    if days_old >= PASSWORD_MAX_AGE_DAYS:
        status, message = "Expired", "Your Password is Expired. You Should Update It."
    elif days_old >= PASSWORD_MAX_AGE_DAYS * 0.75:
        status, message = "Expiring Soon", "Your Password is Getting Old. Consider Updating Soon."
    else:
        status, message = "Safe", "Your Password Age is Safe."
    return jsonify({"days_old": days_old, "status": status, "message": message})

if __name__ == "__main__":
    app.run(port=5003)