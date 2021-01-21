import requests
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    url = "http://thefirstcontainer:8765/"
    x = requests.get(url)
    return "This response is from the second container with a reply from the linked container: ----==== " + str(x.text) + " ====----"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)