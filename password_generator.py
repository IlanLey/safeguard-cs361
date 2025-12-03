from flask import Flask, request, jsonify
import random, string
import pyperclip

app = Flask(__name__)

@app.route("/generate", methods = ["GET"])
def generatePassword():
    
    # Get All Random Uppercase, Lowercase and Punctuations
    chars = string.ascii_letters + string.digits + string.punctuation
    
    # Get the Length Parameter (Default is 10)
    length = int(request.args.get("length", 10))

    # Best Security Practices (Cannot Go Below Password Length of 8)
    if length < 8:
        length = 8

    # Generate Random Password
    password = ''.join(random.choice(chars) for _ in range(length))

    # Copy to clipboard
    pyperclip.copy(password)

    # Return JSON Randomly Generated Password
    return jsonify({
        "password": password,
        "length": length,
    })

if __name__ == "__main__":
    app.run(port=5004)