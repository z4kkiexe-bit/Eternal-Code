from flask import Flask, render_template, request, jsonify
import google.genai as genai
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    pesan = request.json["pesan"]
    respon = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=pesan
    )
    return jsonify({"balasan": respon.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True) 