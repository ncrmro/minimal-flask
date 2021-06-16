from src import app

print('HELLO WORLD')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
