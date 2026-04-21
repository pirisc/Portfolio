# 🧠 Vibe Mood Classifier

> *Journal your heart out. Choose how you want to be loved today: playlists, memes, inspirational images, self-care tips, or quotes.*

A fine-tuned NLP application that reads the emotional tone of your text and responds with a fully personalized vibe package — because your feelings deserve more than a label. They deserve a whole experience.

---

## 🌟 What It Does

You write something — a journal entry, a rant, a sentence, a single word — and the model detects the emotion living in those words. Then, instead of just telling you what you're feeling, it hands you a curated toolkit for *that specific emotion*: music to match your mood, a meme to make you feel less alone, an inspirational image, a quote that hits different, a self-care nudge, and an affirmation to ground you.

The best part? **You choose what you need.** Checkboxes let you select only the support that serves you in that moment. Sometimes you need all of it. Sometimes you just need a playlist and to be left alone. This app respects that.

---

## 🎯 Supported Emotions

| Emotion | Vibe |
|---|---|
| 😢 Sad | Soft playlists, permission to feel it, gentle nudges |
| 😡 Angry | Hard music, boundaries, poetic pop-offs |
| 😰 Anxious | Calming sounds, grounding tips, reality checks |
| 😊 Joy | Upbeat bangers, celebration, main character energy |
| 😴 Tired | Chill playlists, rest permission, couch justification |
| 😶 Numb | Ambient sounds, patience, "frozen doesn't mean gone" |
| 💪 Confident | Hype music, power quotes, "whole damn meal" energy |
| 🌱 Hopeful | Uplifting anthems, manifesting reminders, bloom quotes |

---

## ✨ Features

### 🎛️ Personalized Vibe Packages
Each of the 8 detected emotions maps to a curated `vibe_map` containing:

- **🎵 Playlist** — A Spotify playlist matched to the emotional energy
- **😂 Meme** — Because humor is a coping mechanism and nobody should gatekeep that
- **🖼️ Inspirational Image** — Visual emotional support
- **✨ Quote** — Carefully selected words from people who've been there
- **💡 Self-Care Tip** — A concrete, doable action for right now
- **💬 Affirmation** — Words that remind you who you actually are

### ☑️ User-Controlled Output
A checkbox interface lets users select exactly what they want to see. No information overload. No unsolicited advice. Just the support you asked for.

### 🧠 Emotion Detection with Confidence Score
The classifier returns the detected emotion AND a confidence percentage, so you can see how clearly your words mapped to a mood.

---

## 🏗️ Project Architecture

```
VibeMoodClassification/
│
├── app.py                  # Full Gradio application with vibe_map + classifier
├── requirements.txt        # Dependencies
└── README.md               # This file (HuggingFace Spaces config + docs)
```

---

## 🛠️ Tech Stack

| Component | Tool |
|---|---|
| Base Model | `distilbert/distilbert-base-uncased` |
| Fine-tuned Model | `Sairii/mood_classifier_distilbert` |
| Inference | HuggingFace `pipeline` (text-classification) |
| UI Framework | `Gradio` |
| Deployment | HuggingFace Spaces |
| Runtime | PyTorch (CUDA / CPU auto-detection) |

---

## 🚀 How to Run Locally

### 1. Clone the repo

```bash
git clone https://huggingface.co/spaces/Sairii/VibeMoodClassification
cd VibeMoodClassification
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> **requirements.txt:**
> ```
> gradio
> torch
> transformers
> ```

### 3. Launch the app

```bash
python app.py
```

The app will be live at `http://localhost:7860` 🎉

---

## 🔬 How It Works

### Step 1 — Text Input
The user types a journal entry, a sentence, or any free-form text into the input box.

### Step 2 — Emotion Classification
The text is passed through the fine-tuned DistilBERT model via a HuggingFace inference pipeline. The model returns the top predicted emotion label and its confidence score.

```python
classifier = pipeline(
    task="text-classification",
    model="Sairii/mood_classifier_distilbert",
    device="cuda" if torch.cuda.is_available() else "cpu",
    top_k=2,
    batch_size=32
)
```

### Step 3 — Vibe Mapping
The predicted emotion label is used to look up a curated pool of resources from `vibe_map` — a hand-crafted dictionary of playlists, memes, images, quotes, self-care tips, and affirmations for each emotion. One item per category is randomly sampled at inference time, ensuring variety across sessions.

```python
vibe = vibe_map.get(label, {})
playlist = random.choice(vibe.get("playlists", ["No playlist found"]))
affirmation = random.choice(vibe.get("affirmations", ["No affirmation found"]))
# ... and so on for each category
```

### Step 4 — Selective Output Rendering
The Gradio interface renders only the categories the user selected via the checkbox group. Unselected outputs return `None` and are hidden from view.

```python
meme_url = result["meme"] if "Meme" in selections else None
image_url = result["image"] if "Inspirational Image" in selections else None
```

---

## 🗂️ Vibe Map Structure

The `vibe_map` is the heart of the application — a nested dictionary that stores all curated content organized by emotion and category:

```python
vibe_map = {
    "emotion_label": {
        "playlists":   [...],   # Spotify playlist URLs
        "memes":       [...],   # Image URLs
        "images":      [...],   # Inspirational image URLs
        "quotes":      [...],   # Text quotes with attribution
        "self_care":   [...],   # Actionable self-care tips
        "affirmations":[...]    # Personalized affirmations
    },
    # ... repeated for all 8 emotions
}
```

Each pool contains between 5–13 items per category, randomly sampled at runtime to keep the experience fresh across repeated uses.

---

## 🎨 Gradio Interface

The app uses a multi-output Gradio interface with:

- **Input 1:** `gr.Textbox` — free-form text entry
- **Input 2:** `gr.CheckboxGroup` — user selects which content types to display
- **Output 1:** `gr.Textbox` — emotion label, confidence score, and selected text content
- **Output 2:** `gr.HTML` — clickable Spotify playlist link
- **Output 3:** `gr.Image` — meme (if selected)
- **Output 4:** `gr.Image` — inspirational image (if selected)

---

## 📊 Model Details

| Property | Value |
|---|---|
| Base architecture | DistilBERT (distilbert-base-uncased) |
| Task | Multi-class sequence classification |
| Number of labels | 8 |
| Dataset | Sairii/mood_dataset (6,561 samples) |
| Training split | 80/20 train/test |
| Optimizer | AdamW (lr=1e-4) |
| Epochs | 5 |
| Batch size | 32 |

---


## 🤗 Live Demo

Try it live on HuggingFace Spaces:
👉 [Sairii/VibeMoodClassification](https://huggingface.co/spaces/Sairii/VibeMoodClassification)

---

## 📄 License

Apache 2.0 — use it, fork it, feel your feelings with it.
