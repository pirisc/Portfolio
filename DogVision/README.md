**Dog Breed Classifier**


**Overview**

The Dog Breed Classifier is a deep learning model built with PyTorch that classifies dog breeds from a dataset containing over 10,000 labeled images across 120 different breeds. This project aims to demonstrate the application of convolutional neural networks (CNNs) in image classification tasks, specifically for identifying dog breeds.

The model is deployed via Gradio and hosted on Hugging Face, providing users with an interactive interface to classify dog breeds in real-time by simply uploading an image.

**Project Structure**

This repository contains the following components:

* `Dog_Vision.ipynb`: The primary Jupyter notebook that contains the entire process:

  * Data Preprocessing: Loading and preparing the Kaggle dataset.

  * Model Training: Building and training the convolutional neural network using PyTorch.

  * Evaluation: Testing the model’s performance on unseen images.

  * Gradio Deployment: Setting up the Gradio interface and deploying the model on Hugging Face for live interaction.

* `requirements.txt`: A file that lists all the required dependencies for running the notebook.

**Setup Instructions**

1. Clone the Repository
  Start by cloning the repository to your local machine:
```
  git clone https://github.com/pirisc/Portfolio/blob/main/DogVision/DogVision.ipynb
```
2. Install Dependencies
   Make sure all dependencies are installed:
```
    pip install -r requirements.txt
```
3. Set Up Kaggle API (For Dataset Access)
   
   To access the Kaggle dataset, you’ll need to set up your Kaggle API credentials. If you haven't done this yet:
     Sign in to Kaggle and go to your account settings.

     Create a new API token by clicking on Create New API Token and downloading the kaggle.json file.

     Place the kaggle.json file in the ~/.kaggle/ directory on your local machine.

     You can now download the dataset using the Kaggle API from within the notebook.
  

5. Run the Notebook
  Open the notebook Dog_Breed_Classifier.ipynb and follow the instructions within it to run the project.

**Live Demo**

For a live demonstration, visit the deployed Gradio app hosted on [Hugging Face](https://huggingface.co/spaces/Sairii/Dog_Breeds). Upload an image of a dog, and the model will predict the breed in real-time.

**Dataset**

The dataset used for training is from the Kaggle competition Dog Breed Identification. It contains over 10,000 images of dogs labeled with one of 120 breeds.

**Prerequisites**

To run this project locally, the following are required:

  * Python 3.x

  * PyTorch

  * Torchvision

  * Gradio

  * Kaggle API for dataset download (as detailed above)

  * Dependencies in `requirements.txt`

**License**
This project is licensed under the MIT License. See the LICENSE.md file for more information.

**Acknowledgments**
  * PyTorch: For providing the powerful tools for building deep learning models.
  
  * Gradio: For creating a simple way to deploy machine learning models.

  * Kaggle: For hosting the competition and providing the dataset.

**Contributing**
If you would like to contribute to this project, feel free to fork the repo and submit a pull request. All contributions are welcome, including improving model performance, adding more breeds, or improving documentation.

