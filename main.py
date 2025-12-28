def compute_fun_score(animal, total_animals, interaction):
    score = 0

    # Posture
    posture_score = {
        "jumping": 25,
        "standing": 20,
        "sitting": 15,
        "lying": 5
    }
    score += posture_score.get(animal["posture"], 10)

    # Mood
    mood_score = {
        "playful": 25,
        "happy": 20,
        "alert": 15,
        "calm": 10,
        "sleepy": 5,
        "aggressive": 0
    }
    score += mood_score.get(animal["mood"], 10)

    # Playfulness Level
    score += animal["playfulness_level"]

    # Energy Level
    score += animal["energy_level"]

    # Cuteness Level
    score += animal["cuteness_level"]

    # Interaction
    if (interaction == "playing"):
        score += 15

    # Multiple animals bonus
    if total_animals>1:
        score += min(total_animals * 3, 15)

    return min(score, 100)