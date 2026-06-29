# Chromatic Object Segmentation Engine

A Python-based computer vision tool designed to explore color space transformations and isolate specific target objects from image frames using color masking strategies.

This project implements image filtering routines to cleanly separate yellow objects of interest from background noise without relying on heavy deep-learning frameworks.

## 🚀 Key Features
* **Color Space Conversion:** Translates standard BGR image streams into HSV channels to evaluate optimal target isolation zones.
* **Dynamic Chromatic Masking:** Builds custom threshold boundaries (`inRange`) to isolate objects based on highly specific color profiles.
* **Bitwise Logical Operations:** Isolates targets cleanly by applying pixel masks to original image matrices.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Libraries:** OpenCV (`cv2`), NumPy

## 💻 How to Run Locally

1. Clone this repository to your machine:
   ```bash
   git clone [https://github.com/AbdelrahmanMohamed7/Chromatic-Object-Segmentation.git](https://github.com/AbdelrahmanMohamed7/Chromatic-Object-Segmentation.git)
