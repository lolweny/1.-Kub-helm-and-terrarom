from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# ✅ Explicitly bind metrics to /metrics
metrics = PrometheusMetrics(app, path="/metrics")

@app.route("/")
def hello():
    return "👋 Hello from Lance AKS! - v8"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

