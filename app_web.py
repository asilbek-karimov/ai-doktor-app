from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/javob', methods=['POST'])
def javob():
    simptom = request.form['simptom']
    if 'isitma' in simptom and 'yo‘tal' in simptom:
        natija = "Sizda COVID-19 bo‘lishi mumkin. Iltimos, test topshiring."
    elif 'bosh og‘riq' in simptom:
        natija = "Siz charchagandirsiz, dam oling. Davom etsa, shifokorga murojaat qiling."
    else:
        natija = "Iltimos, aniqroq alomatlar kiriting."
    return render_template('javob.html', natija=natija)

if __name__ == '__main__':
    app.run(debug=True)