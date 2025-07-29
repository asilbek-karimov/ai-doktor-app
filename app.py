from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    diagnosis = None
    if request.method == 'POST':
        symptoms = request.form['symptoms']
        diagnosis = ai_diagnose(symptoms)  # o'zingiz yozgan tahlil funksiyasi

    return render_template('index.html', diagnosis=diagnosis)