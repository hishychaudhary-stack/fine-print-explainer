from flask import Flask, render_template, request

app = Flask(__name__)

def analyze_text(text):
    results = []
    text_lower = text.lower()

    if "data" in text_lower or "personal information" in text_lower:
        results.append(("Data Collection", "This policy may collect your personal data or information.", "HIGH"))

    if "third party" in text_lower or "partners" in text_lower:
        results.append(("Third-Party Sharing", "Your information may be shared with outside companies or partners.", "HIGH"))

    if "subscription" in text_lower or "renew" in text_lower or "recurring" in text_lower:
        results.append(("Subscription / Auto-Renewal", "This may involve recurring payments or automatic renewal.", "MEDIUM"))

    if "arbitration" in text_lower:
        results.append(("Arbitration", "You may be giving up your right to sue in court.", "HIGH"))

    if "cookies" in text_lower:
        results.append(("Cookies", "The website may track your activity using cookies.", "LOW"))

    if "terminate" in text_lower or "suspend" in text_lower:
        results.append(("Account Termination", "The company may be able to suspend or terminate your account.", "MEDIUM"))

    if "liability" in text_lower:
        results.append(("Limited Liability", "The company may limit how responsible it is if something goes wrong.", "MEDIUM"))

    if not results:
        results.append(("General", "No major risky clauses were detected.", "LOW"))

    return results

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("policy", "")
        results = analyze_text(text)
        return render_template("result.html", results=results)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
