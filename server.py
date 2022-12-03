from flask import Flask, render_template
import random
from datetime import datetime
import requests

NAME = "Thulani Mbatha"

app = Flask(__name__)

@app.route('/')
def home():
    rand_num = random.randint(0, 50)
    year = datetime.now().year
    return render_template("index.html", num=rand_num, current_year=year, my_name=NAME)  # num is the variable name, rand_num is the value

@app.route('/guess/<name>')
def age_name_guess(name):

    parameter = {
        "name" : name,
    }

    gender_response = requests.get("https://api.genderize.io", params=parameter)
    age_response = requests.get("https://api.agify.io", params=parameter)

    # get the gender
    gen_data = gender_response.json()
    gender = gen_data["gender"]

    # get the age
    age_data = age_response.json()
    age = age_data["age"]

    return render_template("guess.html", guess_name=name, guess_gender=gender, guess_age=age)

if __name__ == "__main__":
    app.run(debug=True)
