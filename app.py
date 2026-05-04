from flask import Flask, render_template, request

app = Flask(__name__)

def analyze_text(text):
    results = []

    if "data" in text.lower():
        results.append(("Data Collection", "This policy mentions collecting your data.", "HIGH"))

    if "third party" in text.lower():
        results.append(("Third-Party Sharing", "Your data may be shared.", "HIGH"))

    if "subscription" in text.lower():
        results.append(("Subscription", "May include recurring payments.", "MEDIUM"))

    if "arbitration" in text.lower():
        results.append(("Arbitration", "You may give up your right to sue.", "HIGH"))

    if not results:
        results.append(("General", "No major risks found.", "LOW"))

    return results

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["policy"]
        results = analyze_text(text)
        return render_template("result.html", results=results)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
