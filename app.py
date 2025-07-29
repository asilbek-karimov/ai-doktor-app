# app.py

from flask import Flask, request, render_template

app = Flask(__name__)

# Bu yerda kasalliklar bazasi bor — oddiy lug‘at (dictionary) ko‘rinishida
kasallik_bazasi = {
    "yo'tal": "Sizda nafas yo‘llari infeksiyasi bo‘lishi mumkin. Ko‘proq suv iching va agar yo'tal 3 kundan ortsa, shifokorga murojaat qiling.",
    "isitma": "Isitma infeksiya belgisi bo‘lishi mumkin. Vrachga boring va tana haroratingizni nazorat qiling.",
    "bosh og‘rig‘i": "Bosh og‘rig‘i stress, uyqusizlik yoki suvsizlanishdan bo‘lishi mumkin. Agar kuchli bo‘lsa, nevropatologga murojaat qiling."
}

@app.route("/", methods=["GET", "POST"])
def index():
    javob = ""
    if request.method == "POST":
        alomat = request.form["alomat"].lower()
        if alomat in kasallik_bazasi:
            javob = kasallik_bazasi[alomat]
        else:
            javob = "Bu alomat bo‘yicha ma'lumot topilmadi. Iltimos, boshqa so‘z kiriting."

    return render_template("index.html", javob=javob)

if __name__ == "__main__":
    app.run(debug=True)