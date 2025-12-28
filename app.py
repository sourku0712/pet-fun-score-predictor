from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil, json, os

from ai import feature
from main import compute_fun_score

# ✅ Create app ONCE
app = FastAPI()

# ✅ Add CORS to the SAME app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS", "HEAD"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

leaderboard = []

# ✅ Health check (for UptimeRobot)
@app.api_route("/health", methods=["GET", "HEAD"])
def health_check():
    return {"status": "ok"}

# ✅ Analyze endpoint
@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    image_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    data = json.loads(feature(image_path))

    total_animals = data["total_animals"]
    interaction = data["interaction"]

    results = []
    scores = []
    image_score = 0

    for animal in data["animals"]:
        score = compute_fun_score(animal, total_animals, interaction)
        scores.append(score)
        image_score = max(image_score, score)

        results.append({
            "animal_type": animal["animal_type"],
            "mood": animal["mood"],
            "posture": animal["posture"],
            "fun_score": score
        })

    leaderboard.append({
        "image": file.filename,
        "score": image_score
    })
    leaderboard.sort(key=lambda x: x["score"], reverse=True)

    return {
        "total_animals": total_animals,
        "results": results,
        "leaderboard": leaderboard[:5]
    }