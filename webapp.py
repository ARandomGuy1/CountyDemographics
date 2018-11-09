from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) 

@app.route("/")
def render_main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    #print(get_state_options(counties))
    return render_template('Home.html', states = get_state_options(counties))
    
@app.route("/response")
def render_response():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    state = request.args["states"]
    states = {}
    for x in range(0, len(counties)):
        if counties[x]["State"] in states:
            states[counties[x]["State"]] += 1
        else:
            states[counties[x]['State']] = 1
    fact = 0
    for x in states:
        if x == state:
            fact = states[x]
    return render_template("response.html", response = fact)
            
            
    
    
def get_state_options(counties):
    state = ""
    listOfStates = []
    for x in range(0, len(counties)):
        state = counties[x]['State']
        if state not in listOfStates:
            listOfStates.append(counties[x]["State"])
    options = ""
    for x in listOfStates:
        options += Markup("<option value=\"" + x + "\">" + x + "</option>")
    return options


    


















if __name__=="__main__":
    app.run(debug=False, port=54321)