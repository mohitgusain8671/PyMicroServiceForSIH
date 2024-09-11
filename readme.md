# FastAPI Microservice for Fertilizer and Crop Prediction

This FastAPI microservice provides endpoints for predicting fertilizer requirements and crop suitability based on various environmental and soil factors. The models are trained using machine learning techniques, and predictions are made using pre-trained models stored in `.pkl` files.


### Files

- **main.py**: The entry point for the FastAPI application.
- **routes/prediction.py**: Contains the API routes for fertilizer and crop prediction.
- **crop_model.pkl**: Pickle file containing the pre-trained crop prediction model.
- **fertilizer_model.pkl**: Pickle file containing the pre-trained fertilizer prediction model.
- **le_crop.pkl**: Pickle file for label encoding crop types.
- **le_soil.pkl**: Pickle file for label encoding soil types.

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd FastApiMicroservice

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
4. **Run the FastAPI application:**

    ```bash
    uvicorn app.main:app --reload
    ```
The application will start at http://127.0.0.1:8000.

# API Endpoints

## 1. `/predict-fertilizer`

- **Method**: `POST`
- **Description**: Predicts fertilizer requirements based on environmental and soil data.

### Request Body
```json
{
    "Temperature": [float],
    "Humidity": [float],
    "Moisture": [float],
    "Soil_Type": [string],
    "Crop_Type": [string],
    "Nitrogen": [int],
    "Potassium": [int],
    "Phosphorous": [int]
}
```
### Response Body
```json
{
    "predictions": [int]
}
```

## 2. `/predict-crop`

- **Method**: `POST`
- **Description**: Predicts suitable crops based on soil, environmental data, and nutrient values.

### Request Body
```json
{
    "N": [int],
    "P": [int],
    "K": [int],
    "Temperature": [float],
    "Humidity": [float],
    "PH": [float],
    "Rainfall": [float]
}
```
### Response Body
```json
{
    "predictions": [int]
}
```
