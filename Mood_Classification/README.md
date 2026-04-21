# 🧠 Mood Classifier — From Model to Product

> *An end-to-end NLP project: fine-tuning a text emotion classifier and turning it into a real, human-centered application.*

---

## 💡 Project Overview

This repository documents the full lifecycle of an NLP project — from raw dataset to deployed product — across two distinct phases:

**Phase 1** is the ML engineering work: loading a dataset, encoding labels, tokenizing text, fine-tuning a pre-trained transformer model, evaluating it, and saving it to HuggingFace Hub.

**Phase 2** is the product work: taking that trained model and wrapping it in an experience that a real human would actually want to use — with curated playlists, memes, quotes, self-care tips, and affirmations matched to whatever emotion the model detects.

Together, these two phases answer a question that a lot of ML projects never bother to ask: *okay, the model works — but now what?*

---

## 🗂️ Repository Structure

```
mood-classifier/
│
├── README.md                        ← You are here
│
├── 01_training_pipeline/
│   ├── mood_classification_app.ipynb   ← Full training notebook
│   └── README.md                       ← Deep dive into the ML pipeline
│
└── 02_vibe_app/
    ├── app.py                          ← Gradio application
    ├── requirements.txt                
    └── README.md                       ← Deep dive into the app architecture
```

---

## 📖 The Two Chapters

### Chapter 1 — Training Pipeline [`01_training_pipeline/`](./01_training_pipeline/)

This is where the model gets built. Starting from the [`Sairii/mood_dataset`](https://huggingface.co/datasets/Sairii/mood_dataset) (6,561 labeled text samples across 8 emotions), the notebook walks through the full supervised fine-tuning pipeline:

- Exploratory data analysis and label distribution
- Label encoding with `sklearn`'s `LabelEncoder`
- Tokenization using DistilBERT's fast tokenizer
- Fine-tuning `distilbert-base-uncased` using HuggingFace's `Trainer` API
- Evaluation on a held-out test set with accuracy metrics
- Saving and pushing the model to HuggingFace Hub

**The output of this phase** is a fine-tuned model hosted publicly at `Sairii/mood_classifier_distilbert` — which becomes the engine that powers Phase 2.

👉 [Read the full training pipeline README](./01_training_pipeline/README.md)

---

### Chapter 2 — Vibe App [`02_vibe_app/`](./02_vibe_app/)

This is where the model becomes a product. The trained classifier is loaded via HuggingFace's `pipeline` API and wrapped in a Gradio interface that does more than just output a label — it hands the user a curated emotional support package.

Each of the 8 detectable emotions maps to a hand-crafted `vibe_map` containing Spotify playlists, memes, inspirational images, quotes, self-care tips, and affirmations. The user selects which categories they want via a checkbox interface — because sometimes you need all the support, and sometimes you just need a playlist and to be left alone.

**The output of this phase** is a live Gradio app deployed on HuggingFace Spaces.

👉 [Read the full vibe app README](./02_vibe_app/README.md)

---

## 🛠️ Tech Stack

| Layer | Tools |
|---|---|
| Data | HuggingFace `datasets`, Pandas |
| Modeling | `transformers`, `distilbert-base-uncased`, HuggingFace `Trainer` |
| Evaluation | `evaluate`, `sklearn` |
| Inference | HuggingFace `pipeline` |
| UI | `Gradio` |
| Deployment | HuggingFace Spaces |
| Runtime | PyTorch (CUDA / CPU) |

---

## 🎯 Detected Emotions

| Label | Description |
|---|---|
| 😢 Sad | Grief, loss, low mood |
| 😡 Angry | Frustration, rage, injustice |
| 😰 Anxious | Worry, overthinking, fear |
| 😊 Joy | Happiness, excitement, gratitude |
| 😴 Tired | Exhaustion, burnout, low energy |
| 😶 Numb | Emotional flatness, dissociation |
| 💪 Confident | Self-assurance, empowerment |
| 🌱 Hopeful | Optimism, anticipation, possibility |

---

## 🚀 Try It Live

The deployed app is available on HuggingFace Spaces:

👉 [Sairii/VibeMoodClassification](https://huggingface.co/spaces/Sairii/VibeMoodClassification)

The fine-tuned model is available on HuggingFace Hub:

👉 [Sairii/mood_classifier_distilbert](https://huggingface.co/Sairii/mood_classifier_distilbert)

---


## 🙋 Author

Built end-to-end with Python, HuggingFace, and the conviction that good technology should make people feel understood — not just processed.

---

## 📄 License

Apache 2.0
