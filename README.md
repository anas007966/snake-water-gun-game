# 🐍 Snake Water Gun Game 🎮

Hello! 👋  
This is a fun and simple Python project I made as a beginner. It's a game called **Snake Water Gun**, just like Rock Paper Scissors — but with a twist!

---

## 📌 Game Rules

- You will get **10 chances** to play.
- Each round, you type:
  - `s` for Snake
  - `w` for Water
  - `g` for Gun
- The computer randomly picks one too.
- The winner of each round is decided based on these rules:

| Your Choice | Computer's Choice | Result             |
|-------------|-------------------|--------------------|
| Snake (s)   | Water (w)         | You Win 🥳         |
| Water (w)   | Gun (g)           | You Win 🥳         |
| Gun (g)     | Snake (s)         | You Win 🥳         |
| Same choice | Same choice       | Tie 🤝             |
| Other cases |                   | You Lose 😢        |

---

## 📁 Requirements

- Python 3 installed (I used **Python 3.11**)
- `playsound` module installed to play audio

### Install playsound
```bash
pip install playsound==1.2.2
