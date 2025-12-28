## 🐾 Pet Fun Score Predictor



A web-based AI application that analyzes animal images to estimate **playfulness / fun score**, visualize results with **emojis, leaderboards**, and an **annotated image highlighting the most playful animal** — all **without training a custom model**.





### 🚀 Features



📸 Upload an image of pets/animals



🧠 Uses a pretrained vision-language AI model (Gemini)



🐶 Detects animals and infers:

* Mood
* Posture
* Playfulness, energy, and cuteness



🎯 Computes a Fun Score (0–100) using rule-based logic



😄 Displays mood-based emojis



🏆 Maintains a live leaderboard



🌐 Clean, responsive frontend UI





### 🏗️ Tech Stack



#### 🔹Backend



* Python
* FastAPI
* Google Gemini Vision API
* python-multipart – image upload handling



#### 🔹Frontend



* HTML
* Google Fonts (Poppins)





### 📂 Project Structure



Pet Fun Score Predictor/

│

├── ai.py                 # AI vision inference

├── main.py               # Fun score logic

├── app.py                # FastAPI backend

├── uploads/              # Uploaded images

│

├── frontend/

│   └── index.html        # Web UI

│

├── README.md

└── requirements.txt





### ⚙️ Installation \& Setup



#### 1️⃣ Clone the Repository



git clone https://github.com/sourku0712/pet-fun-score-predictor.git

cd pet-fun-score-predictor



#### 2️⃣ Install Dependencies



pip install -r requirements.txt



#### 3️⃣ Set API Key



In ai.py:

GEM\_API\_KEY = "YOUR\_GEMINI\_API\_KEY"



### ▶️ Running the Application



#### 🔹 Start Backend (FastAPI)



 	uvicorn app:app --reload



 	Backend runs at:

 	http://127.0.0.1:8000



#### 🔹 Run Frontend



#####     Option 1 (Simple):



 	Open frontend/index.html directly in browser



#####     Option 2 (Recommended):



 	cd frontend

 	python -m http.server 5500



 	Open:

 	   http://localhost:5500





### 🧪 How It Works



* User uploads an image
* Image is sent to FastAPI backend
* AI model analyzes the image and returns structured attributes
* A rule-based engine computes fun scores
* Backend:
* Updates leaderboard
* Frontend displays:
* Scores + emojis
* Leaderboard





#### 🏆 Leaderboard Logic



* Each uploaded image is scored
* Leaderboard ranks images by highest fun score
* Top entries are displayed live on the UI





### 📌 Future Improvements



* True object detection bounding boxes
* Persistent leaderboard (database)
* User authentication
* Mobile-friendly UI
* Download annotated image button
