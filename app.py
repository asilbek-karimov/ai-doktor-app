from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    javob = ""
    if request.method == "POST":
        simptom = request.form["simptom"]
        javob = f"Siz kiritgan alomat: {simptom}. Bu haqida tez orada tahlil beriladi."
    return render_template_string("""
        <h1>AI Doktor Assistent</h1>
        <form method="post">
            <label>Alomatingizni kiriting:</label><br>
            <input type="text" name="simptom" required><br><br>
            <input type="submit" value="Yuborish">
        </form>
        <p>{{ javob }}</p>
    """, javob=javob)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000) # Bu yer test uchun ozgina o'zgartirish kiritildi