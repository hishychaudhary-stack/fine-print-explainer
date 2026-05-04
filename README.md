# 📄 Explain the Fine Print

A web application that helps users understand complex Terms of Service and Privacy Policies by highlighting risky clauses and explaining them in plain English.

---

## 🚀 Features

- Paste any policy text
- Detects risky clauses like:
  - Data collection
  - Third-party sharing
  - Subscriptions
  - Arbitration
- Displays risk levels (HIGH / MEDIUM / LOW)
- Clean and simple UI

---

## 🛠️ Tech Stack

- Python (Flask)
- HTML / CSS
- Jinja2 Templates

---

## ▶️ How to Run Locally

```bash
git clone https://github.com/hishychaudhary-stack/fine-print-explainer.git
cd fine-print-explainer
python3 -m venv venv
source venv/bin/activate
pip install flask
python3 app.py

************ http://127.0.0.1:5000 ************


We collect your data and may share it with third party partners.
Subscriptions automatically renew monthly.
You agree to arbitration and waive your right to sue.



 Output
Data Collection → HIGH risk
Third-Party Sharing → HIGH risk
Subscription → MEDIUM risk
Arbitration → HIGH risk

Purpose

This project helps users understand what they are agreeing to before clicking “Accept” on legal agreements.

 Author

Hisham Chaudhary



