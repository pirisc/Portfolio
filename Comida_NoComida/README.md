**Comida / NoComida**

##📌 **Project Overview**
**Comida/NoComida** is a binary text classification model trained to label short phrases as either:

  * `comida` — the phrase refers to food, eating, drinks, recipes, or anything food-adjacent
  * `no_comida` — everything else

The dataset was built from scratch, containing ~1,000 labeled text samples. The final model is deployed as an interactive Gradio app on Hugging Face Spaces, where you can type any phrase and get an instant prediction.


## 📊 **Dataset**
The dataset was created and labeled by hand, consisting of ~1,000 short phrases in Spanish, each annotated with one of two labels:
 
| Label      | Description                          | Example                     |
|------------|--------------------------------------|-----------------------------|
| `comida`   | Food-related phrase                  | *"una pizza con champiñones"*|
| `no_comida`| Non-food phrase                      | *"el partido de fútbol"*    |

You can find and download the dataset [here](https://huggingface.co/datasets/Sairii/comida_no_comida)


## 🧠 Model
 
The classifier was built using HuggingFace:
  - For the tokenizer: we used `distilbert-base-uncased`
  - And for the model: we also used `distilbert-base-uncased`


## 🚀 Live Demo
 
The model is deployed as a **Gradio app on Hugging Face Spaces**. Just type a phrase and see the prediction in real time.
 
👉 Try it here: [Comida/NoComida on Hugging Face](https://huggingface.co/spaces/Sairii/learn_hf_food_not_food_text_classifier_demo)

