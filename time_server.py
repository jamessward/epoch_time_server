from flask import Flask
import os
import time

app = Flask(__name__)


@app.route('/')
def get_time():
    # Returns epoch time
    return str(time.time())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
