from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def pocetna():
    # Ovo traži index.html unutar 'templates' foldera
    return render_template('index.html')

@app.route('/moj-video')
def video_stranica():
    # Ovo traži video.html unutar 'templates' foldera
    return render_template('video.html')

if __name__ == "__main__":
    app.run(debug=True)