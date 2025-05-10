# SoundRoute 🎧🗺️

**Travel-based playlist generator that matches your destination and mood with music.**

---

## 📌 Features
- Choose a destination city and a mood
- Receive a tailored playlist recommendation
- Lightweight Flask web app with static frontend

---

## 🚀 How It Works
- Input city and mood (e.g., "Paris" and "romantic")
- Backend reads `city_moods.json` and returns matching songs
- If no exact match, a random default playlist is shown

---

## 📁 Project Structure
```
soundroute/
├── app.py               # Main Flask app
├── recommender.py       # Logic for matching playlists
├── data/
│   └── city_moods.json  # Data file for cities/moods
├── templates/
│   └── index.html       # Frontend page
├── static/
│   └── style.css        # Basic styling
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

---

## 🛠 Technologies
- Python
- Flask
- HTML/CSS
- JSON for simple data storage

---

## 🧠 Example Cities & Moods
| City   | Mood     | Sample Tracks                                  |
|--------|----------|------------------------------------------------|
| Paris  | Romantic | La Vie en Rose, Ne Me Quitte Pas               |
| Berlin | Party    | Midnight City, On Hold                         |
| Tokyo  | Chill    | Night Owl, Cold Little Heart                   |

---

## 📦 Installation

```
git clone https://github.com/soulstream-voyager/soundroute.git
cd soundroute
pip install -r requirements.txt
python app.py
```

---

## 🗣️ Contact
Made with 🎶 by [@soulstream-voyager](https://github.com/soulstream-voyager)  
📫 sofiiahusyak@gmail.com | [@sofiia_hus](https://t.me/sofiia_hus) on Telegram

---

> “Every place has a rhythm. Every moment deserves a soundtrack.”

---
