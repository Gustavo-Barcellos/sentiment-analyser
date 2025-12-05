from flask import Flask, request, render_template

app = Flask(__name__)

positive_words = ["abundance", "achievement", "admire", "adventure", "amazing",
    "appreciation", "authentic", "balance", "beauty", "blessing",
    "brilliance", "calm", "celebrate", "clarity", "comfort",
    "commitment", "compassion", "confidence", "connection", "courage",
    "creative", "curiosity", "dedication", "delight", "determination",
    "dream", "empower", "energy", "enthusiasm", "excellence",
    "faith", "freedom", "growth", "grateful", "harmony",
    "hope", "inspire", "joy", "kindness", "leadership",
    "love", "mindful", "motivation", "optimism", "passion",
    "peace", "prosperity", "purpose", "resilience", "strength",
    "success", "trust", "victory", "wisdom", "positivity",
    "thriving", "radiance", "uplift", "brave", "healing"]
negative_words = ["anger", "anxiety", "apathy", "bad", "betrayal",
    "chaos", "conflict", "confusion", "corruption", "cry",
    "danger", "damage", "darkness", "depression", "despair",
    "distrust", "doubt", "failure", "fear", "frustration",
    "grief", "guilt", "harm", "hate", "helpless",
    "insecurity", "jealousy", "loss", "loneliness", "misery",
    "neglect", "pain", "panic", "poverty", "regret",
    "risk", "sadness", "shame", "stress", "struggle",
    "suffering", "toxic", "trauma", "uncertainty", "unfair",
    "unhappy", "violence", "weakness", "worry", "burden",
    "resentment", "hopeless", "fearful", "broken", "hostile"]

def analyze_phrase(phrase):


    
    total_positive = 0
    total_negative = 0

    for word in phrase.split():
        clean = word.lower().strip("!?.,:;")
        if clean in positive_words:
            total_positive += 1
        if clean in negative_words:
            total_negative += 1

    if total_positive > total_negative:
        feeling = "Positive"
    elif total_negative > total_positive:
        feeling = "Negative"
    else:
        feeling = "Neutral"

    return total_positive, total_negative, feeling

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        phrase = request.form.get("phrase")
        result = analyze_phrase(phrase)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
