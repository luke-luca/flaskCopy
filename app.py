from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

title = "Easy Message"
flavours = ['Cytryna-Limonka',
            'Wanilia',
            'Czekolada',
            'Śmietanka z Ciastkiem',
            'Truskawka',
            'Guma Balonowa',
            'Wata Cukrowa',
            'Mango',
            'Pianki',
            'Jagoda',
            'Banan Split',
            'Mieta-Czekolada']

cap_colors = ['Czerwone',
              'Niebieskie',
              'Zielone',
              'Różowe',
              'Czarne',
              'Żółte',
              'Fioletowe',
              'Pomaranczowe']


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html', title=title, flavours=flavours, cap_colors=cap_colors)


@app.route('/result', methods=["GET", "POST"])
def my_form_post():
    # Smaki
    climonka = request.form['Cytryna-Limonka']
    wanilia = request.form['Wanilia']
    czekolada = request.form['Czekolada']
    szciastkiem = request.form['Śmietanka z Ciastkiem']
    truskawka = request.form['Truskawka']
    gbalonowa = request.form['Guma Balonowa']
    wcukrowa = request.form['Wata Cukrowa']
    mango = request.form['Mango']
    pianki = request.form['Pianki']
    jagoda = request.form['Jagoda']
    bsplit = request.form['Banan Split']
    mczekolada = request.form['Mieta-Czekolada']

    v = [climonka, wanilia, czekolada, szciastkiem, truskawka,
         gbalonowa, wcukrowa, mango, pianki, jagoda, bsplit, mczekolada]
    # Czapki
    czerwone = request.form['Czerwone']
    niebieskie = request.form['Niebieskie']
    zielone = request.form['Zielone']
    rozowe = request.form['Różowe']
    czarne = request.form['Czarne']
    zolte = request.form['Żółte']
    fioletowe = request.form['Fioletowe']
    pomaranczowe = request.form['Pomaranczowe']

    c = [czerwone, niebieskie, zielone, rozowe,
         czarne, zolte, fioletowe, pomaranczowe]
    kubki = request.form['kubki']
    spoons = request.form['spoons']
    return render_template('result.html', c=c, v=v, flavours=flavours, cap_colors=cap_colors, kubki=kubki, spoons=spoons)


if __name__ == '__main__':
    app.run(debug=True)
