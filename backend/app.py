from fastapi import FastAPI,HTTPException,Path
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal
from fastapi.responses import JSONResponse
import pandas as pd
import pickle
from fastapi.middleware.cors import CORSMiddleware
with open('model.pkl','rb') as f:
    model=pickle.load(f)
tier1_cities=['Chennai','Mumbai','Hyderabad', 'Delhi','Kolkata','Bangalore']
tier2_cities=['Jaipur' ,'Indore','Kota','Lucknow','Gaya','Jalandhar','Mysore']
class Insurance(BaseModel):
    age:Annotated[int,Field(...,gt=0,lt=120,description='age of the user')]
    weight:Annotated[float,Field(...,gt=0,description='Weight of the user')]
    height:Annotated[float,Field(...,gt=0,description='Height of the user')]
    income_lpa:Annotated[float,Field(...,description='Annual Income of the user')]
    smoker:Annotated[bool,Field(...,description='Is the person a smoker')]
    city:Annotated[str,Field(...,description='City user belongs to')]
    occupation:Annotated[str,Field(...,description='Occupation of the user')]

    @computed_field
    @property
    def bmi(self)->float:
        return round(self.weight/(self.height**2),2)
    @computed_field
    @property
    def age_group(self)->str:
        if self.age >0 and self.age<30:
            return 'Young'
        elif self.age <60:
             return 'middle_aged'
        else:
            return 'Senior Citizen'
    @computed_field
    @property
    def lifestyle_risk(self)->str:
        if self.smoker and self.bmi>30:
            return 'high'
        elif self.smoker and self.bmi>27:
            return 'medium'
        else:
            return 'low'

    @computed_field
    @property
    def city_tier(self)->int:
        if self.city in tier1_cities:
            return 1
        elif self.city in tier2_cities:
            return 2
        else:
            return 3
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post('/predict')
def predict(data:Insurance):
    input_df=pd.DataFrame([{
        'bmi':data.bmi,
        'age_group':data.age_group,
        'city_tier':data.city_tier,
        'lifestyle_risk':data.lifestyle_risk,
        'income_lpa':data.income_lpa,
        'occupation':data.occupation
    }])
    prediction=model.predict(input_df)[0]
    return JSONResponse(status_code=200,content={'prediction': str(prediction)})