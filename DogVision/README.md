# 🐾 Dog Breed Classifier

> *120 breeds. 10,000+ images. One model that knows dogs better than most dog owners.*

A deep learning image classifier built with **PyTorch** that identifies dog breeds in real-time. Upload a photo, get a prediction — simple as that. Powered by a convolutional neural network trained on the [Kaggle Dog Breed Identification dataset](https://www.kaggle.com/c/dog-breed-identification) and deployed live on Hugging Face Spaces.

---

## 🚀 Live Demo

**Try it now →** [Dog Breeds Classifier on Hugging Face](https://huggingface.co/spaces/Sairii/Dog_Breeds)

No setup needed. Just upload a dog photo and watch it work.

---

## 📌 What This Project Does

This project walks through the **full machine learning pipeline** — from raw data to a deployed, interactive web app:

| Stage | What happens |
|---|---|
| 📦 Data Preprocessing | Load and prepare labeled images from Kaggle |
| 🧠 Model Training | Train a CNN using PyTorch on 120 dog breeds |
| 📊 Evaluation | Test model accuracy on held-out images |
| 🌐 Deployment | Launch a Gradio interface hosted on Hugging Face |

---

## 📁 Project Structure

```
DogVision/
├── Dog_Vision.ipynb       # Full pipeline: preprocessing → training → evaluation → deployment
└── requirements.txt       # All dependencies
└── README.md
```

Everything lives in a single, well-documented notebook — clean, readable, and easy to follow.

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/pirisc/Portfolio.git
cd Portfolio/DogVision
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Kaggle API (for dataset access)

The dataset is hosted on Kaggle, so you'll need to authenticate:

1. Log in to [Kaggle](https://www.kaggle.com) and go to **Account Settings**
2. Click **Create New API Token** → this downloads a `kaggle.json` file
3. Move it to the right location:

```bash
mkdir -p ~/.kaggle
mv kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

The notebook will handle the dataset download from there.

### 4. Run the Notebook

Open `Dog_Vision.ipynb` in Jupyter and run the cells top to bottom.

---

## 🗂️ Dataset

**Source:** [Kaggle — Dog Breed Identification](https://www.kaggle.com/c/dog-breed-identification)

- 10,000+ labeled dog images
- 120 distinct breeds
- Provided as part of a Kaggle competition

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| [PyTorch](https://pytorch.org/) | Model architecture & training |
| [Torchvision](https://pytorch.org/vision/) | Image transforms & pretrained models |
| [Gradio](https://gradio.app/) | Interactive web UI |
| [Hugging Face Spaces](https://huggingface.co/spaces) | Model deployment & hosting |
| [Kaggle API](https://github.com/Kaggle/kaggle-api) | Dataset access |

**Requirements:** Python 3.x — see `requirements.txt` for full dependency list.

---

## 🤝 Contributing

Contributions are welcome! If you want to improve model accuracy, expand the breed list, or clean up the docs — fork the repo and open a PR. All improvements are appreciated.

---

## 📄 License

Licensed under the [MIT License](LICENSE.md) — use it, build on it, make it yours.
