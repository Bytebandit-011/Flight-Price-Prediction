
# ✈️ Flight Fare Prediction Model: Flask Deployment

A machine learning web application that predicts flight fares based on various features like airline, route, departure time, and more. Built with Flask and deployed for easy access.

## 🚀 Live Demo Link
https://flight-price-prediction-hspw.onrender.com


## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Model Performance](#model-performance)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## 🎯 Overview

This project is a Flight Price Prediction Model designed to estimate flight fares based on various input features such as airline, departure and arrival times, flight duration, and more. The model is trained using machine learning algorithms and is deployed as a RESTful API using Flask, a lightweight Python web framework.

## ✨ Features

- **Interactive Web Interface**: Easy-to-use form for fare prediction
- **Machine learning model training**: (Random Forest, XGBoost, SVM , LR) for accurate price predictions.
- **Multiple Airlines Support**: Covers major airlines and routes
- **Responsive Design**: Works on desktop and mobile devices
- **Input Validation**: Ensures data quality and prevents errors

### Key Features:
- `Airline`: Carrier name (Air India, IndiGo, Jet Airways, etc.)
- `Date_of_Journey`: Travel date
- `Source`: Departure city
- `Destination`: Arrival city
- `Dep_Time`: Departure time
- `Arrival_Time`: Arrival time
- `Duration`: Flight duration
- `Total_Stops`: Number of stops (0-4)
- `Additional_Info`: Extra services information

## 📈 Model Performance

| Metric | Score |
|--------|-------|
| **Algorithm** | Random Forest Regressor |
| **R² Score** | 0.834 |
| **Mean Absolute Error** | ₹1,247 |
| **Root Mean Square Error** | ₹2,156 |
| **Cross-Validation Score** | 0.821 ± 0.023 |

## 🛠️ Installation

### Prerequisites
- Python 3.7+

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/flight-fare-prediction.git
cd flight-fare-prediction
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv flight_env

# Activate virtual environment
flight_env\Scripts\activate

```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```


## 🎮 Usage

### Web Interface

1. **Navigate** to the application URL
2. **Fill in the form** with your flight details:
   - Select airline
   - Choose source and destination
   - Pick travel date
   - Select departure time
   - Specify number of stops
3. **Click "Predict Fare"** to get the estimated price
4. **View results** with fare prediction and confidence interval

### API Usage

#### Predict Fare (POST)
```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "airline": "IndiGo",
    "source": "Delhi",
    "destination": "Mumbai",
    "date_of_journey": "2024-12-25",
    "dep_time": "Morning",
    "arrival_time": "Afternoon",
    "duration": "2h 20m",
    "total_stops": 0,
    "additional_info": "No info"
  }'
```

#### Response
```json
{
  "predicted_fare": 5847.32,
  "confidence_interval": [4892.15, 6802.49],
  "status": "success",
  "model_version": "v1.2"
}
```

## 🏗️ Project Structure

```
flight-fare-prediction/
├── app.py                    # Main Flask application
├── forms.py                  # WTForms for form handling
├── model.joblib              # Trained ML model (joblib format)
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── .gitignore               # Git ignore file
├── # %% [markdown].py       # Markdown cells export (development)
├── model-train.ipynb        # Jupyter notebook for model training
├── data/                    # Dataset folder
│   └── [your_dataset].csv   # Training data
└── templates/               # HTML templates
    ├── base.html            # Base template
    ├── index.html           # Home page
    ├── predict.html         # Prediction form
    └── result.html          # Results display
```



### Deployment
- 

## 📱 Screenshots

### Home Page
![image](https://github.com/user-attachments/assets/3f8b7aa5-0337-4403-b046-a96c3547a27c)


### Prediction Form
![image](https://github.com/user-attachments/assets/777f6d76-360e-4f8e-b207-e5f4663a6d5a)


## 🔮 Future Enhancements

- [ ] **Price Alerts**: Notify users when fares drop
- [ ] **Multiple Routes**: Compare prices across different routes
- [ ] **Mobile App**: Native mobile application
- [ ] **International Flights**: Expand to international routes


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## 🙏 Acknowledgments

- Dataset provided by [Source Name]
- Inspiration from flight booking platforms
- Flask documentation and community
- Scikit-learn contributors

---

⭐ **Star this repository if you found it helpful!**

## 📚 References

1. [Scikit-learn Documentation](https://scikit-learn.org/)
2. [Flask Documentation](https://flask.palletsprojects.com/)
3. [Flight Fare Prediction Research Papers](link-to-papers)

---

