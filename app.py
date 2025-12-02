from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/rate", methods=["POST"])
def rate():
    data = request.get_json()
    rating = data.get("rating")
    # Here you could save to a database / file / logging system
    print(f"User submitted rating: {rating}")
    return jsonify({"success": True, "rating": rating})

if __name__ == "__main__":
    app.run(debug=True)
