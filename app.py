from flask import Flask, render_template

app = Flask(__name__)

def analyze_logs():
    suspicious = []
    total_logs = 0

    with open("logs.txt","r") as file:
        logs = file.readlines()

    total_logs = len(logs)

    for log in logs:
        if "Failed login" in log or "Unauthorized" in log:
            suspicious.append(log.strip())

    return suspicious, total_logs


@app.route("/")
def index():

    alerts, total_logs = analyze_logs()
    alert_count = len(alerts)

    return render_template("index.html",
                           alerts=alerts,
                           total_logs=total_logs,
                           alert_count=alert_count)

if __name__ == "__main__":
    app.run(debug=True)