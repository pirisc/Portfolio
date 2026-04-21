# WELCOME

Welcome to my portfolio!! My name is Iris and I'm an aspiring Machine Learning Engineer focused on building practical AI systems and data-driven applications.

I'm learning by myself following different online courses, so it's taking its time, but I'm eager to learn and put things in practice.

---

## 👩🏻‍💻​ ​Projects 
### 🖼️ Computer vision 

#### 🐕​ DogVision - Dog Breed Classifier
> PyTorch · CNN · Transfer Learning · Gradio · Hugging Face Spaces

Deep learning classifier that identifies **120 dog breeds** from images, trained on the Kaggle Dog Breed Identification dataset (~10,000 labeled images). Built with PyTorch, deployed as an interactive Gradio app on Hugging Face Spaces.

120-class image classification using convolutional neural networks
End-to-end pipeline: data preprocessing → training → evaluation → deployment
Live demo: users upload any dog photo and get an instant breed prediction

🔗 [Live Demo](https://huggingface.co/spaces/Sairii/Dog_Breeds)

#### 🍕​🍔​🍣​ FoodVision Big — 101 Food Category Classifier
> PyTorch · EfficientNetB2 · Vision Transformer (ViT) · Transfer Learning · Gradio · Hugging Face Spaces

Transfer learning pipeline classifying **101 food categories** from the Food-101 dataset (101,000 images). The project is structured in two phases: a focused 3-class prototype (pizza, steak, sushi) scaled up to all 101 categories using EffNetB2 and ViT architectures.

Dual-model comparison: EfficientNetB2 vs. Vision Transformer
Transfer learning with fine-tuning on 20% of Food-101 dataset
Gradio interface deployed on Hugging Face for real-time food image classification

🔗 [Live Demo](https://huggingface.co/spaces/Sairii/FoodVision_Big)

#### 🗑️​Trashify — Object Detection for Waste Management

> PyTorch · RT-DETRv2 · Hugging Face Transformers · Gradio · Hugging Face Spaces

Computer vision application built on **RT-DETRv2** (Real-Time Detection Transformer v2), fine-tuned to detect 7 object classes in waste management scenarios: trash, bins, hands, and their negative counterparts. The app awards users +1 point when all three target items are detected simultaneously — making recycling interactive.

- Transformer-based object detection with no NMS (bipartite matching + learned object queries)
- Full inference pipeline: image preprocessing → forward pass → bounding box post-processing → annotated output
- Covers the complete ML deployment cycle: fine-tuned model → Gradio interface → HF Spaces production deployment

🔗 [Live Demo](https://huggingface.co/spaces/Sairii/trashify_demo_v1)

#### CIFAR-10 Image Classifier

> PyTorch · CNN · Image Classification

Image classification on the **CIFAR-10 benchmark** — 60,000 32×32 colour images across 10 classes (50,000 train / 10,000 test). Built from scratch as a foundational exploration of convolutional architectures and training dynamics in PyTorch.

- 10-class classification on a standard computer vision benchmark
- Custom CNN architecture trained end-to-end in PyTorch

#### FashionMNIST Classifier

> PyTorch · CNN · Image Classification

Clothing item classifier trained on the **FashionMNIST dataset** — 70,000 grayscale images across 10 fashion categories (28×28 pixels). A step up from digit recognition, introducing real-world texture and shape variation.

- 60,000 training / 10,000 test examples across 10 apparel classes
- Exploration of neural network architecture decisions in a controlled benchmark setting

#### MNIST Digit Classifier

> PyTorch · Neural Networks · Image Classification

The classic entry point to computer vision. Handwritten digit recognition on the **MNIST dataset** — the "hello world" of deep learning, used here to establish solid fundamentals in PyTorch model building, training loops, and evaluation.

---
### 📖​ Natural Language Processing
#### Comida/NoComida - Binary Text Classifier
> Hugging Face Transformers · DistilBERT · Spanish NLP · Gradio · Hugging Face Spaces

Binary text classification model trained on a custom hand-labeled dataset of **~1,000 Spanish phrases**, distinguishing food-related text (`comida`) from everything else (`no_comida`). Dataset built from scratch, model fine-tuned on distilbert-base-uncased, deployed as a live Gradio app.

- Custom dataset creation and labeling pipeline (Spanish language)
- Fine-tuning DistilBERT for domain-specific binary classification
- Dataset and model published on Hugging Face Hub

🔗 [Live Demo](https://huggingface.co/spaces/Sairii/learn_hf_food_not_food_text_classifier_demo) · [Dataset](https://huggingface.co/datasets/Sairii/comida_no_comida)

#### 🎥​ Movie Review Sentiment Classifier

> PyTorch · NLP · Binary Sentiment Classification

Sentiment analysis model trained on the **IMDb Large Movie Review Dataset** — 25,000 training and 25,000 test highly polar reviews, classified as positive or negative. A deep dive into text preprocessing, embedding strategies, and sequence modeling fundamentals.

- Binary sentiment classification on a standard NLP benchmark
- 50,000 labeled reviews (pos/neg) from the IMDb dataset


#### 😍​😀​😶‍🌫️​😭​ VibeMood — Text Mood Classifier

> Python · NLP · Text Classification

Text classification model that goes beyond binary sentiment to capture mood and emotional tone from short-form text. Built to explore multi-class emotional classification and the nuances of subjective language.

---

### 📊 Classical Machine Learning
#### Kaggle Competition Notebooks
> scikit-learn · XGBoost · LightGBM · Pandas · Feature Engineering · EDA

A collection of competition notebooks focused on tabular data, featuring rigorous EDA, feature engineering, and ensemble methods.

| Competition | Task | Best Score | Metric | 
|---|---|---|---|
|[Spaceship Titanic](https://www.kaggle.com/competitions/spaceship-titanic) | Binary Classification | 0.80430 | Accuracy |
| [Titanic - ML from disaster](https://www.kaggle.com/competitions/titanic) | Binary Classification | 0.66507 | Accuracy | 

---

## 💻 Tech Stack 

| Category | Tools |
|---|---|
| Deep Learning | PyTorch, Torchvision |
| Transformers & NLP | Hugging Face Transformers, Datasets, DistilBERT, ViT, RT-DETRv2 |
| Classical ML | scikit-learn, XGBoost, LightGBM |
| Data | NumPy, Pandas |
| Deployment | Gradio, Hugging Face Spaces|
| Visualization | Matplotlib, Seaborn |




