# **Food Vision Classifier Big**

## **Overview**

The FoodVision Classifier is a deep learning model built with PyTorch that classifies 101 different food categories from a dataset containing 101,000 labeled images. For this project we used transfer learning to help us get the most accurate classification possible.

The model is deployed via Gradio and hosted on Hugging Face, providing users with an interactive interface to classify food categories in real-time by simply uploading an image.

This project is divided in two parts. The first part works with only 20% of the whole dataset and only with 3 food categories (pizza, sushi and steak) and the second part works with, also, the 20% of the dataset but with the 101 food categories.

## **Project Structure**

This repository contains the following components:
 * `Food_Vision.ipynb`: The primary Jupyter notebook that contains the entire process:

    * Data Preprocessing: Loading and preparing the dataset.

    * Model Training: In this case we are using transfer learning with two different models:
        * First model will be an EffNetB2
        * Second model will be an ViT
          
      In the case of our project, first we work with only 20% of the data and 3 different food categories(only with the pizza, steak and sushi categories). Later we will use what we learn from this data to the include the other food categories in the  dataset.

    * Evaluation: Testing the model’s performance on unseen images.

    * Gradio Deployment: Setting up the Gradio interface and deploying the model on Hugging Face for live interaction.

## **Live Demo**

For a live demonstration of this project, visit the deployed Gradio app hosted of [Hugging Face](https://huggingface.co/spaces/Sairii/FoodVision_Big). Upload an image of some type of food and the model will predict its category.

## **Dataset**

The dataset used is for training is from the [101 Food Dataset](https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/) and the dataset with only the 20% of the data is from the [Learning Pytorch Couse](https://www.learnpytorch.io/09_pytorch_model_deployment/#1-getting-data)

## **Prerequisites** 

To run this project locally, the following are required:
  * Torch
  * Torchvision
  * Gradio

## **Contributing**

If you would like to contribute to this project, feel free to fork the repo and submit a pull request. All contributions are welcome, including improving model performance, adding more breeds, or improving documentation.
