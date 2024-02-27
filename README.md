# TUBERCULOSIS-DETECTION-USING-CHEST-X-RAY-IMAGE


## Overview

This project focuses on the detection of Tuberculosis using Chest X-ray images. Various image processing techniques, including image enhancement, histogram equalization, image restoration, segmentation, and filters, are employed to improve the accuracy of detection.

## Table of Contents

- [Introduction](#introduction)
- [Image Processing Techniques](#image-processing-techniques)
- [Building a CNN Model](#CNN-Model)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)

## Introduction

Tuberculosis (TB) is a chronic lung disease that occurs due to bacterial infection and is one of the top 10 leading causes of death. It is transmitted by aerosol inhalation of the bacterium Mycobacterium tuberculosis (Mtb) from an infected individual. During the course of infection, a wide variety of pulmonary disease lesion presentations may concurrently present within the same host. Accurate and early detection of TB is very important, otherwise, it could be life-threatening. The latest World Health Organization(WHO) study on 2018 is showing that about 1.5 million people died and around 10 million people are infected with tuberculosis (TB) each year. Moreover, more than 4,000 people die every day from TB. A number of those deaths could have been stopped if the disease was identified sooner. In this work, we have detected TB reliably from the chest X-ray images using image pre-processing, data augmentation, image segmentation, and deep-learning classification techniques. We also used a visualization technique to confirm that CNN learns dominantly from the segmented lung regions that resulted in higher detection accuracy.

## Dataset
Our data set contains 3500 normal and 700 affected (Tuberculosis) images. They are saved in two different folders namely “Nor mal” and “Tuberculosis
Link to our dataset: (https://www.kaggle.com/datasets/tawsifurrahman/tuberculosis-tb-chest-xray-dataset)

## Work Flow Diagram
![image](https://github.com/SAICHARAN0204/TUBERCULOSIS-DETECTION-USING-CHEST-X-RAY-IMAGES/assets/82882226/314cabb1-d176-47aa-84dc-0641a5d80ac7)

## Image Processing Techniques

1. **Image Enhancement**:
     Techniques to improve the visual quality of Chest X-ray images, ensuring better feature representation.
     ![image](https://github.com/SAICHARAN0204/TUBERCULOSIS-DETECTION-USING-CHEST-X-RAY-IMAGES/assets/82882226/4c1310a2-df5c-42c1-93a3-c9cfd9495066)


3. **Histogram Equalization**:
       This method usually increases the global contrast of many images, especially when the image is represented by a narrow range of intensity values. Through this adjustment, the intensities can be better distributed on the histogram utilizing the full range of intensities evenly. This allows for areas of lower local contrast to gain a higher contrast. Histogram equalization accomplishes this by effectively spreading out the highly populated intensity values which degrade image contrast.
     ![image](https://github.com/SAICHARAN0204/TUBERCULOSIS-DETECTION-USING-CHEST-X-RAY-IMAGES/assets/82882226/7dd9de4c-2d39-409c-88c9-f13f420a94c1)


5. **Image Restoration**:
     Image restoration is the operation of taking a corrupt/noisy image and estimating the clean, original image. Corruption may come in many forms such as motion blur, noise and camera 
mis-focus.
  ![image](https://github.com/SAICHARAN0204/TUBERCULOSIS-DETECTION-USING-CHEST-X-RAY-IMAGES/assets/82882226/8bd9b2ad-6e12-4e7f-96a5-59bea0d88f53)

6. **Filters**: '
     The Sobel filter is used for edge detection. It works by calculating the gradient of image intensity at each pixel within the image. It finds the direction of the largest increase from light to dark and the rate of change in that direction.
     ![image](https://github.com/SAICHARAN0204/TUBERCULOSIS-DETECTION-USING-CHEST-X-RAY-IMAGES/assets/82882226/6374c810-4eda-4422-b0b9-ced2ff266467)
 
7. **Segmentation**:
     Image segmentation is a method in which a digital image is broken down into various subgroups called Image segments which helps in reducing the complexity of the image to make further processing or analysis of the image simpler. Segmentation in easy words is assigning labels to pixels.
     ![image](https://github.com/SAICHARAN0204/TUBERCULOSIS-DETECTION-USING-CHEST-X-RAY-IMAGES/assets/82882226/d5de2f3d-0f9f-4223-832f-8a9fe0bbf477)
   
8. **FEATUR EXTRACTION:- WAVELET**
     The wavelet analysis method is a time-frequency analysis method which selects the appropriate frequency band adaptively based on the characteristics of the signal. Then the frequency band matches the spectrum which improves the time-frequency resolution.The basic method of the wavelet transform is selecting a function whose integral is zero in time-domain as the basic wavelet. By the expansion and  of the basic wavelet, we can get a family function which may constitute a framework for the function space. We decompose the signal by projecting the analysis signals on the framework. The signal in original timedomain can get a time-scale expression by several scaling in the wavelet transform domain. Then we are able to achieve the most effective signal processing purpose transform domain.The essence of wavelet de-noising is searching for the best mapping of signals from of the actual space to wavelet function space in order to get the best restoration of the original signal. From the view of the signal processing, the wavelet de-noising is a signal filtering. The wavelet de-noising is able to retain the characteristics of the image successfully. Actually, it is comprehensive with feature extraction and low-pass filtering
   ![image](https://github.com/SAICHARAN0204/TUBERCULOSIS-DETECTION-USING-CHEST-X-RAY-IMAGES/assets/82882226/c8262972-5947-4fd2-add6-ba69dc2e7297)
   ![image](https://github.com/SAICHARAN0204/TUBERCULOSIS-DETECTION-USING-CHEST-X-RAY-IMAGES/assets/82882226/f437882a-3c09-4f25-83b1-ed74b2a8007f)
   ![image](https://github.com/SAICHARAN0204/TUBERCULOSIS-DETECTION-USING-CHEST-X-RAY-IMAGES/assets/82882226/3ed65ebf-e77e-481a-b92e-793daae12213)
   ![image](https://github.com/SAICHARAN0204/TUBERCULOSIS-DETECTION-USING-CHEST-X-RAY-IMAGES/assets/82882226/ead53260-a13a-4196-95aa-8bdf2aefb785)
   ![image](https://github.com/SAICHARAN0204/TUBERCULOSIS-DETECTION-USING-CHEST-X-RAY-IMAGES/assets/82882226/a2cbf490-be8b-4a2b-ac05-fc1b75998b30)


## CNN-Model
The input image is fed to the neural network. The Convnet then performs convolutions over the input image. Each convolution filter will result in its own output feature map. As we can look at the image, multiple convolutional filters are applied over the input image, as a result, we have transformed a single image into multiple output feature maps.Each feature map will hold specific information about the image. The number of these layers is called the depth of the channels.Next, comes the pooling stage. In pooling, we downsize the input feature map, while retaining the most useful information. So, each value in the feature map after maxpooling will represent a larger patch of the input feature map. Max pooling helps convnets to detect more complex patterns with less computing power.Multiple convolutional layers and max-pooling layers can be arranged successively to form the deep neural network. The number of layers and the depth of each convolutional layer are provided by us, there are no strict guidelines for these hyperparameters and we can experiment on our own to find the combination that works best for our model.Finally, these convolutional layers are connected to a Dense layer(Fully connected), or a regular neural network. We arefree to add multiple layers in this dense layer as well. The final output layer of this neural network will have two nodes, one for each class

1.**Process followed**
    Step 1: Choose a Dataset
    Step 2: Prepare Dataset for Training
    Step 3: Create Training Data.
    Step 4: Shuffle the Dataset.
    Step 5: Assigning Labels and Features.
    Step 6: CREATING A DIRECTORY STRUCTURE
    Step 7: copying trained images to aug_dir
    Step 8: Model architecture
    Step 9: Training and evaluating the model
    Step 10: plot the graph (accuracy, loss)
    Step 11: confusion matrix
    Step 12: Final report



  
## Project Structure

- **`/data`**: Contains the dataset of Chest X-ray images for training and testing.
- **`/src`**: Implementation of image processing techniques and Tuberculosis detection algorithms.
- **`/results`**: Stores the results and evaluation metrics.
- **`/docs`**: Documentation for the project.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/saicharan0204/tuberculosis-detection.git
    cd tuberculosis-detection
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Navigate to the `/src` directory:

    ```bash
    cd src
    ```

2. Run the image processing and detection scripts:

    ```bash
    python image_enhancement.py
    python histogram_equalization.py
    python image_restoration.py
    python segmentation.py
    python filter_application.py
    python tuberculosis_detection.py
    ```

3. View the results in the `/results` directory.

## Results

Include performance metrics, confusion matrices, and visualizations showcasing the effectiveness of the image processing techniques and Tuberculosis detection.

|                | Support  | Precision | Recall | F1 Score |
|----------------|----------|-----------|--------|----------|
| Normal         | 61       | 0.77      | 0.89   | 0.82     |
| Tuberculosis   | 59       | 0.86      | 0.73   | 0.79     |
| avg/total      | 120      | 0.81      | 0.81   | 0.81     |

Achieved precision: 81%
Achieved recall: 81%
F1-score :81%
Support :120

The dataset is quite small but by using a CNN and data augmentation The F1 score is greater than 80%. From the confusion matrix we see that our model has a tendency to classify TB images as Normal, more so than to classify Normal images as TB.

