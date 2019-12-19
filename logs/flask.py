from  flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "ojbk"

if __name__ == '__main__':
    # __call__
    app.run()
