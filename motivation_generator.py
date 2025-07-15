# motivation_generator.py

import random
import json

def load_keywords():
    with open("config.json") as f:
        config = json.load(f)
    return config["keywords"], config["language_mix"]

def generate_motivation():
    keywords, language_mix = load_keywords()
    topic = random.choice(keywords)
    hashtags = random.sample([k for k in keywords if k.startswith("#")], k=2) if "#" in "".join(keywords) else []

    lang = random.choices(
        ["english", "pidgin"],
        weights=[language_mix.get("english", 0.8), language_mix.get("pidgin", 0.2)]
    )[0]

    emojis = ["💪", "🔥", "💯", "🚀", "🎯", "😤", "😎", "🌟", "📈", "🙏", "🧠", "💼"]

    if lang == "english":
        body_templates = [
            f"Discipline around {topic} builds quiet strength.\nStay consistent even when no one is clapping.\nBig rewards come with silent work.",
            f"{topic.capitalize()} doesn’t happen overnight.\nPut your head down and put in the reps.\nSuccess is waiting at the end of the routine.",
            f"Your {topic} mindset determines your {topic} outcome.\nKeep showing up. Keep improving.\nThe world will adjust eventually.",
            f"Everyone wants results, but only few love the grind.\nThat’s your advantage.\n{topic.capitalize()} is for the focused ones."
        ]
    else:
        body_templates = [
            f"No be who shout pass dey win.\nSteady hustle on top {topic} na him dey last.\nJust dey push — e go click one day.",
            f"Make nobody run your race for you.\n{topic.capitalize()} na personal journey.\nDey consistent and dey learn.",
            f"Dem fit laugh now, but your time go come.\nJust focus on {topic}, do your part.\nNa God dey do timing, no be man."
        ]

    body = random.choice(body_templates)
    hash_text = " ".join(hashtags) if hashtags else ""
    emoji = random.choice(emojis)
    return f"{body}\n\n{hash_text} {emoji}".strip()

if __name__ == "__main__":
    print("💬 Sample tweet:")
    print(generate_motivation())
