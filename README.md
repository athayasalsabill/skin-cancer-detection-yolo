# Skin Cancer Detection
This repository contains the implementation of a YOLO-based skin lesion classification project, from dataset preparation to model deployment. Here's how I developed the project:

### Dataset Preparation
Initially, I obtained a skin lesions dataset from Roboflow. Roboflow offers a variety of labeled datasets, including an 8-class skin lesions dataset uploaded by a user named *Cardinal*. After watching a YOLO tutorial, I applied the knowledge using this dataset, successfully building an 8-class skin lesions classification model.

Later, I decided to create my own dataset—well, more like assembling one. I downloaded skin lesion images for 10 classes from the ISIC website. The dataset preparation involved:

- Preprocessing: Cleaning, resizing, augmenting, and annotating the images.
- Annotation Automation: For annotations, I utilized the previously trained 8-class model. I wrote a program to automatically infer the new dataset using the 8-class model and generate the label files. You can find the detailed code for this process in the file [anotassi.ipynb](anotassi.ipynb).
The [preprocessing tools](preprocessing tools) folder contains all the scripts used for preprocessing tasks.

### Deployment
For deployment, I built a Flask app to serve as the UI for skin cancer detection. The deployment code is located in the [deploy](deploy) folder. To use it:

1. Create a virtual environment.
2. Install all dependencies listed in [requirements.txt](requirements.txt).
3. Run the app.py.

### Dataset Availability
Unfortunately, I cannot upload the dataset I created due to size constraints. If you'd like access to it, feel free to contact me at athayasalsabil2002@gmail.com.
