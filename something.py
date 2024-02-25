# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 16:20:04 2023

@author: heman
"""

import numpy as np
import rasterio
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
# Function to read an image
def read_image(image_path):
    with rasterio.open(image_path) as src:
        image = src.read()
        metadata = src.profile
    return image, metadata
# Function to preprocess the image
def preprocess_image(image):
 
 preprocessed_image = np.copy(image)
 # ... preprocessing steps here ...
 return preprocessed_image
# Function to calculate NDVI
def calculate_ndvi(image):
    nir = image[4] # Assuming 5th band is near-infrared
    red = image[3] # Assuming 4th band is red
    ndvi = (nir.astype(float) - red) / (nir + red)
    return ndvi
# Function to create a feature matrix from our images
def create_feature_matrix(ndvi1, ndvi2):
    # Flatten the NDVI images to create a 2D array where each row is a pixel and each column is a feature
    features1 = ndvi1.flatten().reshape(-1, 1)
    features2 = ndvi2.flatten().reshape(-1, 1)
    # Create a feature matrix by taking the difference of NDVI values
    feature_matrix = features2 - features1
    return feature_matrix
# Function to create labels for training (you would replace this with your actual method)
def create_labels(feature_matrix):
 # This is a placeholder function. In reality, you would have a method of labeling
 # which could be manual or based on some heuristic or existing data
 # For example, thresholding NDVI difference might be a simple method
    labels = np.where(abs(feature_matrix[:,0]) > 0.1, 1, 0) # Change threshold is 0.1 for example

    return labels
# Read in the images
image1, metadata1 = read_image("C:/Users/heman/Downloads/stackedtif_00.tif")
image2, metadata2 = read_image("C:/Users/heman/Downloads/stackedtif_13.tif")
# Preprocess the images
preprocessed_image1 = preprocess_image(image1)
preprocessed_image2 = preprocess_image(image2)
# Calculate NDVI for both images
ndvi1 = calculate_ndvi(preprocessed_image1)
ndvi2 = calculate_ndvi(preprocessed_image2)
# Create feature matrix
feature_matrix = create_feature_matrix(ndvi1, ndvi2)
# Create labels
labels = create_labels(feature_matrix)
# Split the dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(feature_matrix, labels, test_size=0.3, random_state=42)
# Initialize the Random Forest model
rf = RandomForestClassifier(n_estimators=100, random_state=42)
# Train the model
rf.fit(X_train, y_train)
# Predict on the test set
y_pred = rf.predict(X_test)
# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
# Show confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print(conf_matrix)
# Visualize the change detection result
predicted_labels = rf.predict(feature_matrix).reshape(ndvi1.shape)
plt.imshow(predicted_labels, cmap='viridis')
plt.colorbar(label='Change Detection')
plt.show()