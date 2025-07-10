
from flask import Flask, request, jsonify
from flask_cors import CORS
from .validators import pan, aadhar

app = Flask(__name__)
CORS(app)

@app.route("/api/validate/pan", methods=["POST"])
def validate_pan():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400
    pan_number = pan.extract_pan_number(file.read())
    return jsonify({"pan_number": pan_number})

@app.route("/api/validate/aadhar", methods=["POST"])
def validate_aadhar():
    file = request.files.get("file")
    print("[debug] request.files keys:", list(request.files.keys()))

    if not file:
        return jsonify({"error": "No file uploaded"}), 400
    aadhar_number = aadhar.extract_aadhar_number(file.read())
    return jsonify({"aadhar_number": aadhar_number})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
