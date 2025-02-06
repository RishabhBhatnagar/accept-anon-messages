from flask import Flask, request, redirect, url_for

app = Flask(__name__)


@app.get("/echo")
def echo(): 
    content = request.args.get('q')
    if content is None:
        return dict(error="Param 'q' must be set")
    return dict(output=content)


@app.get('/')
def default():
    return redirect(url_for("echo", **request.args))


if __name__ == "__main__":
    app.run(debug=True)
