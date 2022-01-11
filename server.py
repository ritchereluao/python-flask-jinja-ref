from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    # return "Hello World!"
    random_number = random.randint(1, 10)
    # current_year = datetime.date.today().strftime("%Y")
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route('/guess/<string:name>')
def guess_name(name):
    gender_response = requests.get(url=f"https://api.genderize.io/?name={name}")
    gender = gender_response.json()["gender"]

    age_response = requests.get(url=f"https://api.agify.io?name={name}")
    age = age_response.json()["age"]

    return render_template("guess.html", name=name, age=age, gender=gender)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_post = response.json()

    return render_template("blog.html", posts=all_post)


if __name__ == "__main__":
    # Run app in debug mode to auto-reload
    app.run(debug=True)
