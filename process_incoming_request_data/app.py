from flask import Flask, request
import pdb

app = Flask(__name__)

@app.route("/query")
def query_example():
    pdb.set_trace()
    request
    return 'TODO ...'

if __name__ == "__main__":
    app.run(debug=True, port=5000)
