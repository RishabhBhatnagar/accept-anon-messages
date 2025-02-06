from flask import Flask, request, redirect, url_for
from datetime import datetime
from typing import List, Dict


app = Flask(__name__)
past_successful_requests: List[Dict] = []


@app.get("/requests")
def return_past_requests():
    return past_successful_requests


@app.get("/echo")
def echo(): 
    content = request.args.get('q')
    if content is None:
        return dict(error="Param 'q' must be set")
    past_successful_requests.append({
        "time": datetime.now(),
        "query": content
    })
    return dict(output=content)


@app.get('/')
def default():
    return redirect(url_for("echo", **request.args))


if __name__ == "__main__":
    app.run(debug=True)

