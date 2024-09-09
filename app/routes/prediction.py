from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
import pandas as pd
import pickle

router = APIRouter()

# Assuming you have your label encoders loaded
with open("app/le_soil.pkl", "rb") as f:
    le_soil = pickle.load(f)

with open("app/le_crop.pkl", "rb") as f:
    le_crop = pickle.load(f)

# Assuming your model is loaded
with open("app/fertilizer_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("app/crop_model.pkl", "rb") as f:
    crop_model = pickle.load(f)

class InputData(BaseModel):
    Temperature: List[float]
    Humidity: List[float]
    Moisture: List[float]
    Soil_Type: List[str]
    Crop_Type: List[str]
    Nitrogen: List[int]
    Potassium: List[int]
    Phosphorous: List[int]

class CropInputData(BaseModel):
    N: List[int]
    P: List[int]
    K: List[int]
    Temperature: List[float]
    Humidity: List[float]
    PH: List[float]
    Rainfall: List[float]


@router.post("/predict-fertilizer")
async def predict(data: InputData):
    # Convert the input data to a DataFrame
    new_data = pd.DataFrame({
        'Temperature': data.Temperature,
        'Humidity': data.Humidity,
        'Moisture': data.Moisture,
        'Soil Type': [le_soil.transform([soil])[0] for soil in data.Soil_Type],
        'Crop Type': [le_crop.transform([crop])[0] for crop in data.Crop_Type],
        'Nitrogen': data.Nitrogen,
        'Potassium': data.Potassium,
        'Phosphorous': data.Phosphorous
    })

    # Ensure the DataFrame columns are in the right order
    new_data = new_data[['Temperature', 'Humidity', 'Moisture', 'Soil Type', 'Crop Type', 'Nitrogen', 'Potassium', 'Phosphorous']]
    
    # Make predictions using your model
    predictions = model.predict(new_data)

    # Return predictions as a response
    return {"predictions": predictions.tolist()}

@router.post("/predict-crop")
async def predict_crop(data: CropInputData):
    try:
        # Convert input data to DataFrame
        new_data = pd.DataFrame({
            'N': data.N,
            'P': data.P,
            'K': data.K,
            'temperature': data.Temperature,
            'humidity': data.Humidity,
            'ph': data.PH,
            'rainfall': data.Rainfall
        })

        # Make predictions
        predictions = crop_model.predict(new_data)

        return {"predictions": predictions.tolist()}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
