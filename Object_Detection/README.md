# 🚮 Trashify — Object Detection for Waste Management
 
A computer vision web application that detects trash, bins, and hands in images using a fine-tuned object detection model, deployed as an interactive Gradio interface on Hugging Face Spaces.
 
---

## 📌 Overview
 
Trashify is an object detection application built around **RT-DETRv2** (Real-Time Detection Transformer v2), a state-of-the-art transformer-based architecture for real-time object detection. The model was fine-tuned on the [Trashify dataset](https://huggingface.co/datasets/mrdbourke/trashify_manual_labelled_images) to detect seven object classes relevant to waste management scenarios.
 
The application rewards users with **+1 point** when all three target items — trash, bin, and hand — are detected simultaneously in a single image, encouraging active participation in cleaning up local areas.
 
---

## 🧠 Model & Architecture
 
| Property | Detail |
|---|---|
| **Base Architecture** | RT-DETRv2 (Real-Time Detection Transformer v2) |
| **Task** | Object Detection |
| **Input Size** | 640 × 640 px |
| **Base Model** | `mrdbourke/rt_detrv2_finetuned_trashify_box_detector_v1` |
| **Framework** | PyTorch + Hugging Face Transformers |

## 🏷️ Detected Classes
 
The model detects the following seven classes:
 
| Class | Bounding Box Color | Description |
|---|---|---|
| `trash` | 🔵 Blue | Target item |
| `bin` | 🟢 Green | Target item |
| `hand` | 🟣 Purple | Target item |
| `trash_arm` | 🟡 Yellow | Arm holding trash |
| `not_trash` | 🔴 Red | Incorrectly classified as trash |
| `not_bin` | 🔴 Red | Incorrectly classified as bin |
| `not_hand` | 🔴 Red | Incorrectly classified as hand |
 
---

## 🔄 Inference Pipeline
 
The prediction pipeline follows these steps:
 
```
Input Image (PIL)
      │
      ▼
AutoImageProcessor         ← Resizes to 640×640, normalizes pixel values,
                              converts to PyTorch tensors
      │
      ▼
RT-DETRv2 Model            ← Forward pass, produces raw logits + bounding box deltas
      │
      ▼
post_process_object_detection  ← Applies confidence threshold, rescales boxes
                                  back to original image dimensions
      │
      ▼
Draw bounding boxes (PIL ImageDraw)
      │
      ▼
Logic layer                ← Checks which target classes were detected,
                              returns appropriate message
      │
      ▼
Output: Annotated Image + Text Message
```

---

## 📚 Context & Learning
 
This project was built as part of a structured course on [fine-tuning and deploying computer vision models with Hugging Face](https://www.learnhuggingface.com/notebooks/hugging_face_object_detection_tutorial). It covers the full ML deployment cycle: loading a pre-trained fine-tuned model, building an inference pipeline, handling model outputs (post-processing bounding boxes back to image space), and wrapping everything in a usable web interface.
 
Key concepts practiced:
- Object detection inference with transformer-based models
- Image preprocessing pipelines for vision models
- Bounding box post-processing and coordinate rescaling
- Gradio interface design and example caching behavior
- Debugging ML deployment errors in production-like environments

This model is not perfect but it is the start of working with Object Detection and everything related with it. 




