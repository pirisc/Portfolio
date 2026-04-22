# 🧠 Mood Classifier with Affirmations

> *Journal your heart out. Choose how you want to be loved today: soft hugs or sassy truth bombs.*

A fine-tuned NLP application that classifies the emotional tone of text and responds with personalized affirmations — because machines can have emotional intelligence too.

---

## 🌟 What It Does

You write something — a journal entry, a sentence, a vibe — and this model tells you exactly what emotion is living in those words. Then, because knowing your mood isn't enough, it hits you with an affirmation tailored to that emotion. And the best part? You get to choose your delivery style:

- **Soft** — gentle, validating, warm. For when you need a hug.
- **Sassy** — direct, empowering, zero-nonsense. For when you need a reality check.

---

## 🎯 Supported Emotions

| Emotion | Example text |
|---|---|
| 😢 Sad | *"I feel like nothing is going right"* |
| 😡 Angry | *"I can't believe they did that to me"* |
| 😰 Anxious | *"I keep overthinking everything"* |
| 😊 Joy | *"I'm having the best day ever"* |
| 😴 Tired | *"I just want to sleep forever"* |
| 😶 Numb | *"I don't feel anything at all"* |
| 💪 Confident | *"I crushed that presentation today"* |
| 🌱 Hopeful | *"I think things are finally turning around"* |

---

## 🛠️ Tech Stack

| Component | Tool |
|---|---|
| Base Model | `distilbert/distilbert-base-uncased` |
| Fine-tuning | HuggingFace `Trainer` API |
| Dataset | [`Sairii/mood_dataset`](https://huggingface.co/datasets/Sairii/mood_dataset) (6,561 samples) |
| Evaluation | `evaluate` (accuracy metric) |
| Label Encoding | `sklearn.preprocessing.LabelEncoder` |
| Demo UI | `Gradio` |
| Deployment | HuggingFace Spaces |

---

## 🔬 Model Training Pipeline

The full training pipeline lives in `mood_classification_app.ipynb`. Here's a high-level walkthrough of what happens:

### Step 1 — Data Loading & Exploration
The dataset is loaded from HuggingFace Hub using `datasets.load_dataset("Sairii/mood_dataset")`. This dataset is also created by me.  We explore the distribution of emotion labels and convert the dataset to a Pandas DataFrame for inspection.

### Step 2 — Label Encoding
Emotion labels are normalized (lowercased, stripped) and converted to integer IDs using `sklearn`'s `LabelEncoder`. We build `id2label` and `label2id` dictionaries for the model.

### Step 3 — Tokenization
We use DistilBERT's fast tokenizer with padding and truncation. A `tokenize_text` function is mapped across the dataset in batches of 1,000 for efficiency.

### Step 4 — Model Setup
`AutoModelForSequenceClassification` is loaded from `distilbert/distilbert-base-uncased` with the number of output labels and our custom `id2label`/`label2id` mappings.

### Step 5 — Training
Training is configured with:
- **Batch size:** 32
- **Learning rate:** 1e-4
- **Epochs:** 5
- **Evaluation:** per epoch
- **Best model checkpoint:** auto-loaded at end

```python
training_args = TrainingArguments(
    output_dir=model_save_dir,
    learning_rate=0.0001,
    num_train_epochs=5,
    eval_strategy="epoch",
    load_best_model_at_end=True,
    ...
)
```

### Step 6 — Evaluation
After training, predictions are run on the test set. We compute softmax probabilities, argmax labels, and compare against ground truth using `accuracy_score`. Low-confidence predictions are also inspected.

### Step 7 — Inference Pipeline
The trained model is wrapped in a HuggingFace `pipeline` for easy text classification:

```python
mood_classifier = pipeline(
    task="text-classification",
    model="models/mood_classifier_distilbert",
    device=device,
    top_k=1,
    batch_size=32
)
```

### Step 8 — Gradio Demo & Deployment
A Gradio interface wraps the classifier and affirmation logic, then the entire demo folder is uploaded to HuggingFace Spaces via `upload_folder`. [Here](https://huggingface.co/spaces/Sairii/mood_text_classifier) you can find the live version of this proyect. 

---

## 💬 Using the Classifier in Python

```python
from transformers import pipeline
import torch

model_path = "Sairii/mood_classifier_distilbert"
device = "cuda" if torch.cuda.is_available() else "cpu"

classifier = pipeline(
    task="text-classification",
    model=model_path,
    device=device,
    top_k=1
)

result = classifier("I'm so exhausted and can't keep going like this")
print(result)
# [{'label': 'tired', 'score': 0.94}]
```

---

## 🎨 Affirmation System

The affirmation engine maps each of the 8 emotions to two tonal pools — **soft** and **sassy** — each containing 13 unique affirmations that are randomly sampled at inference time. This gives the app a human-feeling, non-repetitive quality.

```python
def mood_text_classifier(text: str, tone: str = "soft") -> dict:
    outputs = classifier(text)[0]
    label = outputs[0]["label"].lower()
    score = outputs[0]["score"]
    affirmation = random.choice(affirmations[label][tone])
    
    return {
        "emotion": label,
        "confidence": round(score, 3),
        "affirmation": affirmation
    }
```

**Example output:**
```json
{
  "emotion": "anxious",
  "confidence": 0.912,
  "affirmation": "Your brain is lying to you again—don't fall for it."
}
```

---

## 📊 Dataset

- **Source:** [`Sairii/mood_dataset`](https://huggingface.co/datasets/Sairii/mood_dataset)
- **Size:** 6,561 samples
- **Split:** 80% train / 20% test (stratified, seed=42)
- **Labels:** 8 emotion classes

---

## 🤗 Model on HuggingFace Hub

The fine-tuned model is hosted publicly at:
```
Sairii/mood_classifier_distilbert
```

---

## 📁 HuggingFace Spaces Config

The `README.md` in the `demos/mood_text_classifier/` folder contains the Spaces YAML header required for deployment:

```yaml
---
title: Mood Text Classifier
emoji: ❤️🤬😪😴
colorFrom: blue
colorTo: yellow
sdk: gradio
app_file: app.py
pinned: false
license: apache-2.0
---
```

---

## 📄 License

Apache 2.0 — use it, fork it, build on it.
