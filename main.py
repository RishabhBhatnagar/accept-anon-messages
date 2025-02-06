from flask import Flask, request

app = Flask(__name__)


@app.get("/echo")
def echo(): 
    content = request.args.get('q')
    if content is None:
        return dict(error="Param 'q' must be set")
    return dict(output=content)


if __name__ == "__main__":
    app.run(debug=True)
