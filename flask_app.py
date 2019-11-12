
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
import sass
import json

app = Flask(__name__)

sass.compile(dirname=('./static/sass/', './static/css'))

tripSettings = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
regionPlace = "placeholder"
countries = ['', '', '', '', '']

jsonFile =  open('setup.json')
jsonString = jsonFile.read()
jsonDate = json.loads(jsonString)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/setup', methods=['get', 'post'])
def setup():
    # Step 1, display lower limit form
    if "step" not in request.form:
        return render_template("setup.html", background="none", step="chooseCountry", name="Choose your region!")
    elif request.form["step"] == "tripType":
        jsonDate['UnRegion'] = (request.form["region"])
        tripSettings[0] = (request.form["region"])
        return render_template("setup.html", background="none", step="tripType", name="Who are you travelling with?")

  # Step 2, accept lower limit from form, display upper limit
    elif request.form["step"] == "occasion":
        jsonDate['travellingWith'] = (request.form["1"])
        tripSettings[1] = (request.form['1'])
        return render_template("setup.html", background="none", step="occasion", name="What's the occasion?", number=tripSettings[1])

  # Step 3, accept lower+upper limits from form, display random number
    elif request.form["step"] == "dietaryRestrictions":
        # lower = request.form['1']
        jsonDate['ocassion'] = (request.form["2"])
        tripSettings[2] = (request.form['2'])
        # n = lower + ' ' + upper
        return render_template("setup.html", background="none", step="dietaryRestrictions", name="Are there any dietary restrictions?")
    elif request.form["step"] == "numPeople" and tripSettings[1] not in ['Solo', 'Couple']:
        jsonDate['dietRestrictions'] = (request.form["3"])
        tripSettings[3] = (request.form['3'])


        return render_template("setup.html", background="none", step="numPeople", name="How many people are you travelling with?", check=tripSettings[0])
    elif (request.form["step"] == "numPeople" and tripSettings[1] in ['Solo', 'Couple']):
        jsonDate['dietRestrictions'] = (request.form["3"])
        tripSettings[3] = (request.form['3'])

        if tripSettings[1] == 'Solo':
            jsonDate['numPeople']["adults"] = 1
            tripSettings[4] = '1'
        else:
            jsonDate['numPeople']["adults"] = 2
            tripSettings[4] = '2'
        jsonDate['numPeople']["children"] = 0
        tripSettings[5] = '0'
        # return "hello"
        return render_template("setup.html", background="none", step="ifDates", number=tripSettings, name="Do you have dates for your trip?")
    elif request.form["step"] == "ifDates":
        jsonDate['numPeople']["adults"] = (request.form['adultQuantity'])
        jsonDate['numPeople']["children"] = (request.form['childQuantity'])
        tripSettings[4] = (request.form['adultQuantity'])
        tripSettings[5] = (request.form['childQuantity'])
        return render_template("setup.html", background="none", step="ifDates", number=tripSettings, name="Do you have dates for your trip?")
    elif request.form["step"] == "dates":
        jsonDate['ifDates'] = (request.form["6"])
        tripSettings[6] = (request.form['6'])
        if tripSettings[6] == 'Yes':
            return render_template("setup.html", background="none", step="dates", number=tripSettings[6], name="When are you travelling?", description="We need the dates to offer real-time prices. You can change them after this setup")
        elif tripSettings[6] == 'No':
            return render_template("setup.html", background="none", step="dates", number=tripSettings[6], name="When would you like to go?")
    elif request.form["step"] == "results":
        if tripSettings[6] == 'Yes':
            jsonDate['plannedDates']["start"] = (request.form['trip-start'])
            jsonDate['plannedDates']["end"] = (request.form['trip-end'])
            tripSettings[7] = (request.form['trip-start'])
            tripSettings[8] = (request.form['trip-end'])
        elif tripSettings[6] == 'No':
            jsonDate['unplannedDates']["month"] = (request.form['months'])
            jsonDate['unplannedDates']["days"] = (request.form['days'])
            tripSettings[7] = (request.form['months'])
            tripSettings[8] = (request.form['days'])
        # tripSettings[7] = (request.form['7'])
        # tripSettings[2] = (request.form['3'])

        # return "hello"
        return render_template("setup.html", background="none", step="results", number=tripSettings, name="Itinerary", json=jsonDate)


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
