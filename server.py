from datetime import datetime

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    print("new web request")
    return f"hello so fast so fast so fastfast so fastfast so fastfast so fast!!! the datetime is {datetime.now()}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
