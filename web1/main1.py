from flask import Flask
import dataSource

app = Flask(__name__)

@app.route("/")
def index():
    print(dataSource.get_countries())
    return "<H1>Hello world</H1>"

if __name__ == "__main__":
    app.run(debug=True)