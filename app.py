from flask import Flask, render_template, request
from script import predict_price
import pandas as pd

df=pd.read_csv("bhp.csv")
app = Flask(__name__)

@app.route('/')
def home():
    lo=sorted(df["location"].unique())
    return render_template('index1.html',lo=lo)
    # return render_template('index1.html')

@app.route('/form', methods=["GET","POST"])

def form():
    if request.method == "POST":
        loc = request.form.get("location")
        sqft = request.form.get("sqft")
        bath = request.form.get("bath")
        bhk = request.form.get("bhk")
        x = predict_price(loc, int(sqft), int(bath), int(bhk))
        x=list(str(x))
        s=x[:5]
        r="".join(s)
        return render_template('index1.html', ans=r)

app.run(debug=True)