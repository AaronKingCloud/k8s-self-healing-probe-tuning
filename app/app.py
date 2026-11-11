### Aaron King ####

from flask import Flask, jsonify
import os
import socket
import time

# Flask application instance
app = Flask(__name__)

# Global variable to track wedged state
wedged = False

# Read environment variables for configuration
startup_delay = int(
    os.getenv("STARTUP_DELAY_SECONDS", "0")
)

health_latency = int(
    os.getenv("HEALTHZ_LATENCY_MS", "0")
)

student_id = os.getenv(
    "STUDENT_ID",
    "STUDENT_ID"
)

# Print startup message and delay application start
print(
    f"Starting application with "
    f"{startup_delay}s startup delay"
)

time.sleep(startup_delay)


# Define Flask routes
@app.route("/")
def home():
    hostname = socket.gethostname()

    return (
        f"hello from {student_id} "
        f"pod={hostname}\n"
    )


@app.route("/healthz")
def healthz():
    global wedged

    # Simulate health check latency
    time.sleep(
        health_latency / 1000
    )

    # Return 500 if wedged, otherwise return 200
    if wedged:
        return (
            f"wedged {student_id}\n",
            500
        )

    # Return 200 OK if not wedged
    return (
        f"ok {student_id}\n",
        200
    )


@app.route(
    "/wedge",
    methods=["GET", "POST"]
)
def wedge():
    global wedged

    wedged = True

    return jsonify(
        {
            "status": "wedged"
        }
    )


if __name__ == "__main__":
    # Run the Flask application
    app.run(
        host="0.0.0.0",
        port=8080
    )