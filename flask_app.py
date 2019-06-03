
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
import sass

app = Flask(__name__)

sass.compile(dirname=('./static/sass/', './static/css'))

tripSettings = [0, 0, 0, 0, 0, 0, 0, 0, 0]
regionPlace = "placeholder"
countries = ['', '', '', '', '']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/setup', methods=['get', 'post'])
def setup():
    # Step 1, display lower limit form
    if "step" not in request.form:
        return render_template("setup.html", background="none", step="chooseCountry", name="Choose your region!")
    elif request.form["step"] == "tripType":
        tripSettings[0] = (request.form["region"])
        return render_template("setup.html", background="none", step="tripType", name="Who are you travelling with?")

  # Step 2, accept lower limit from form, display upper limit
    elif request.form["step"] == "occasion":
        tripSettings[1] = (request.form['1'])
        return render_template("setup.html", background="none", step="occasion", name="What's the occasion?", number=tripSettings[1])

  # Step 3, accept lower+upper limits from form, display random number
    elif request.form["step"] == "dietaryRestrictions":
        # lower = request.form['1']
        tripSettings[2] = (request.form['2'])
        # n = lower + ' ' + upper
        return render_template("setup.html", background="none", step="dietaryRestrictions", name="Are there any dietary restrictions?")
    elif request.form["step"] == "numPeople" and tripSettings[1] not in ['Solo', 'Couple']:
        tripSettings[3] = (request.form['3'])


        return render_template("setup.html", background="none", step="numPeople", name="How many people are you travelling with?", check=tripSettings[0])
    elif (request.form["step"] == "numPeople" and tripSettings[1] in ['Solo', 'Couple']):

        tripSettings[3] = (request.form['3'])
        if tripSettings[1] == 'Solo':
            tripSettings[4] = '1'
        else:
            tripSettings[4] = '2'
        tripSettings[5] = '0'
        # return "hello"
        return render_template("setup.html", background="none", step="results", number=tripSettings, name="Total")
    elif request.form["step"] == "results":

        # tripSettings[2] = (request.form['3'])
        tripSettings[4] = (request.form['adultQuantity'])
        tripSettings[5] = (request.form['childQuantity'])
        # return "hello"
        return render_template("setup.html", background="none", step="results", number=tripSettings, name="Total")


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r



if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000,debug=True)
