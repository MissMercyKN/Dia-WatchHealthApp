## DiaWatch 🩺 – AI-Powered Diabetes Risk Detection App

DiaWatch is a user-friendly web application that uses machine learning to assess an individual's risk of developing diabetes. Built with Python and Streamlit, it empowers users with quick risk evaluations, lifestyle recommendations, and informative health tips — all based on input health parameters.It alos contain more information of the best practices to prevent diabetes

 ##🚀 Live Demo 
 https://dia-watchhealthapp-prrzzv7hdx5chsnpy4ps9i.streamlit.app/

## 📌 Features

- ✅ Predicts Low, Medium, or High diabetes risk
- 💡 Provides personalized **lifestyle recommendations**
- 📚 Includes educational content on diabetes prevention
- 🧠 Uses a trained **ML i** (`diabetes_model.pkl`)
- 🌐 Interactive **web interface** via Streamlit



## 🛠️ Tech Stack

- Python
- Scikit-learn (Model training)
- Streamlit (Web interf8ace)
- Pandas / NumPy (Data processing)
- Joblib (Model saving/loading)





## 📈 How It Works

1. User enters health metrics (e.g., BMI, Age, Glucose).
2. Input is passed to the `predict_diabetes()` function.
3. The ML model (trained on the Pima Indians dataset) predicts the diabetes risk.
4. The app displays:
   - Risk level
   - Recommendations
   - Educational information



## 🧪 Sample Inputs

You’ll be asked to enter the following:
- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age



## ⚙️ Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/MissMercyKN/Dia-WatchHealthApp/tree/main
   cd DiaWatch


