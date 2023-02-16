import pandas as pd 
import numpy as np 
import tensorflow as tf 
import json
import os

class HousePrice():
    def __init__(self,CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT):
        self.CRIM=CRIM
        self.ZN=ZN
        self.INDUS=INDUS
        self.CHAS=CHAS
        self.NOX=NOX
        self.RM=RM
        self.AGE=AGE
        self.DIS=DIS
        self.RAD= RAD
        self.TAX=TAX
        self.PTRATIO=PTRATIO
        self.B=B
        self.LSTAT=LSTAT

    def Load_model(self):
        self.loaded_model=tf.keras.models.load_model(os.path.join("models/MODEL","deep_model.tf"))

        with open("models/project_data_deep.json","r")as f:
            self.project_data=json.load(f)

    def Price_prediction(self):
        self.Load_model()
        array=np.zeros(len(self.project_data["columns"]))
        array[0]=self.CRIM
        array[1]=self.ZN
        array[2]=self.INDUS
        array[3]=self.CHAS
        array[4]=self.NOX
        array[5]=self.RM
        array[6]=self.AGE
        array[7]=self.DIS
        array[8]=self.RAD
        array[9]=self.TAX
        array[10]=self.PTRATIO
        array[11]=self.B
        array[12]=self.LSTAT
        array1=array.reshape(1,13)

        prediction=self.loaded_model.predict([array1])[0][0]
        print("price of house is in thaousand $",prediction)

        return prediction

if __name__=="__main__":
    CRIM=0.000462
    ZN=0.000000
    INDUS=0.420455
    CHAS=0.000000
    NOX=0.386831
    RM=0.473079
    AGE=0.802266
    DIS=0.125072
    RAD=0.000000
    TAX=0.164122
    PTRATIO=0.893617
    B=1.000000
    LSTAT=0.169702

    price_pred=HousePrice(CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT)
    price_of_house=price_pred.Price_prediction()

    print("price of bouston house is in thousand $ ",price_of_house)

