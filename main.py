from distutils.command.config import config
from models.utils import HousePrice
from flask import Flask,render_template,request
import config

app= Flask(__name__)

@app.route("/")
def hello_flak():

    return render_template("index.html")

@app.route("/price",methods=["POST","GET"])
def house_price():
    if request.method=="POST":

        CRIM=float(request.form.get("CRIM"))
        ZN=float(request.form.get("ZN"))
        INDUS=float(request.form.get("INDUS"))
        CHAS=float(request.form.get("CHAS"))
        NOX=float(request.form.get("NOX"))
        RM=float(request.form.get("RM"))
        AGE=float(request.form.get("AGE"))
        DIS=float(request.form.get("DIS"))
        RAD=float(request.form.get("RAD"))
        TAX=float(request.form.get("TAX"))
        PTRATIO=float(request.form.get("PTRATIO"))
        B=float(request.form.get("B"))
        LSTAT=float(request.form.get("LSTAT"))


        price_pred=HousePrice(CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT)
        price_of_house=price_pred.Price_prediction()

        return render_template("index.html",prediction=price_of_house)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER,debug=True)