from flask import Flask, render_template, request
import re

app = Flask(__name__)

RISK_RULES = [
    {
        "title": "Data Collection",
        "risk": "HIGH",
        "keywords": ["data", "personal information", "location", "browsing activity", "device information"],
        "plain": "The company may collect personal details about you.",
        "why": "This matters because collected data can be used for tracking, advertising, or profiling."
    },
    {
        "title": "Third-Party Sharing",
        "risk": "HIGH",
        "keywords": ["third party", "partners", "affiliates", "vendors", "advertising partners"],
        "plain": "Your information may be shared with outside companies.",
        "why": "Once your data is shared, you may have less control over who uses it."
    },
    {
        "title": "Auto-Renewal / Subscription",
        "risk": "MEDIUM",
        "keywords": ["subscription", "renew", "recurring", "billing cycle", "automatic renewal"],
        "plain": "You may be charged again automatically unless you cancel.",
        "why": "Users can forget to cancel and continue being billed."
    },
    {
        "title": "Arbitration",
        "risk": "HIGH",
        "keywords": ["arbitration", "class action", "waive", "lawsuit"],
        "plain": "You may be giving up your right to sue in court.",
        "why": "Disputes may have to be handled privately instead of through a normal court case."
    },
    {
        "title": "Cookies / Tracking",
        "risk": "LOW",
        "keywords": ["cookies", "tracking technologies", "analytics", "pixels"],
        "plain": "The website may track your activity.",
        "why": "This can be used to personalize content, measure behavior, or show ads."
    },
    {
        "title": "Account Termination",
        "risk": "MEDIUM",
        "keywords": ["terminate", "suspend", "disable your account", "remove access"],
        "plain": "The company may suspend or close your account.",
        "why": "You could lose access to your account or content if rules are violated."
    },
    {
        "title": "Limited Liability",
        "risk": "MEDIUM",
        "keywords": ["liability", "not responsible", "damages", "limitation of liability"],
        "plain": "The company limits how responsible it is if something goes wrong.",
        "why": "This may reduce your ability to recover losses."
    },
    {
        "title": "No Refunds",
        "risk": "MEDIUM",
        "keywords": ["no refund", "non-refundable", "refunds are not provided"],
        "plain": "You may not get your money back after paying.",
        "why": "This is important before purchasing or subscribing."
    }
]

def split_sentences(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s.strip() for s in sentences if s.strip()]

def analyze_text(text):
    text_lower = text.lower()
    sentences = split_sentences(text)

    results = []

    for rule in RISK_RULES:
        matched_keywords = [word for word in rule["keywords"] if word in text_lower]

        if matched_keywords:
            evidence = []
            for sentence in sentences:
                sentence_lower = sentence.lower()
                if any(word in sentence_lower for word in matched_keywords):
                    evidence.append(sentence)

            results.append({
                "title": rule["title"],
                "risk": rule["risk"],
                "plain": rule["plain"],
                "why": rule["why"],
                "keywords": matched_keywords,
                "evidence": evidence[:2]
            })

    if not results:
        results.append({
            "title": "No Major Risks Detected",
            "risk": "LOW",
            "plain": "This text did not trigger any major risk warnings.",
            "why": "The system only checks for common risky legal phrases.",
            "keywords": [],
            "evidence": []
        })

    score = 0
    for item in results:
        if item["risk"] == "HIGH":
            score += 3
        elif item["risk"] == "MEDIUM":
            score += 2
        else:
            score += 1

    if score >= 8:
        risk_level = "High Risk"
    elif score >= 4:
        risk_level = "Medium Risk"
    else:
        risk_level = "Low Risk"

    return results, score, risk_level

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("policy", "")
        results, score, risk_level = analyze_text(text)
        return render_template(
            "result.html",
            results=results,
            score=score,
            risk_level=risk_level,
            original_text=text
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
