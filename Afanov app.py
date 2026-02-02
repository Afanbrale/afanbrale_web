from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Koristimo <h1> tag za velika, podebljana slova
    return "<h1>Afanbrale napravio web stranicu :O</h1>"

if __name__ == "__main__":
    app.run(debug=True)