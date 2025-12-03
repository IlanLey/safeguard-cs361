from flask import Flask, request, jsonify
import Levenshtein

app = Flask(__name__)

SIMILARITY_THRESHOLD = 0.7  # 70% similarity considered too similar

def password_similarity(new_password, old_password):
    if not new_password or not old_password:
        return {"error": "Both New and Old Passwords are Required."}

    similarity = Levenshtein.ratio(new_password, old_password)
    too_similar = similarity >= SIMILARITY_THRESHOLD

    feedback = "Password is Too Similar to Previous Password, Choose a More Unique One." if too_similar else "Password is Sufficiently Unique."
    return {"Similarity": similarity, "Too Similar": too_similar, "Feedback": feedback}

def username_password_similarity(username, password):
    if not username or not password:
        return {"error": "Both Username and Password are Required."}

    similarity = Levenshtein.ratio(username, password)
    too_similar = similarity >= SIMILARITY_THRESHOLD
    feedback = "Password is Too Similar to Username, Choose a Stronger Password." if too_similar else "Password is Sufficiently Different from Username."
    return {"Similarity": similarity, "Too Similar": too_similar, "Feedback": feedback}

@app.route("/check_password_similarity", methods=["POST"])
def check_password_similarity():
    data = request.get_json()
    new_password = data.get("new_password", "")
    old_password = data.get("old_password", "")
    result = password_similarity(new_password, old_password)
    return jsonify(result)

@app.route("/check_username_similarity", methods=["POST"])
def check_username_similarity():
    data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")
    result = username_password_similarity(username, password)
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=5002, debug=True)