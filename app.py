from flask import Flask, request, render_template
from pprint import pprint
import wbdata as w

app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/carbon', methods =["GET", "POST"])
def carbon():
    if request.method == "POST":
       country_code = request.form.get("ccheck")
       emission_per_capita = w.get_data("EN.ATM.CO2E.EG.ZS", country=country_code.upper())
       for i in emission_per_capita:
            if i['value'] != None:
               value = i['value']
               value = str(value)
       return "Your Country's Carbon Dioxide Density(kg per kg of oil equivalent use): " + value
    return render_template("form.html")

if __name__=='__main__':
    app.run()