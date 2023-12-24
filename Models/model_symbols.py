import os
import cv2
import numpy as np
from skimage.feature import hog
from skimage import exposure
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import joblib
import random
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn import svm

target_img_size = (32, 32)
random_seed = 42
random.seed(random_seed)
np.random.seed(random_seed)

# Function to extract HOG features from an image
def extract_hog_features(img):
    img = cv2.resize(img, dsize=target_img_size)
    win_size = (32, 32)
    cell_size = (4, 4)
    block_size_in_cells = (2, 2)

    block_size = (block_size_in_cells[1] * cell_size[1], block_size_in_cells[0] * cell_size[0])
    block_stride = (cell_size[1], cell_size[0])
    nbins = 9  # Number of orientation bins
    hog = cv2.HOGDescriptor(win_size, block_size, block_stride, cell_size, nbins)
    h = hog.compute(img)
    h = h.flatten()
    return h.flatten()

# Function to load images and labels from the dataset
def load_dataset_symbols(root_folder):
    features = []
    labels = []
    label_names = []  # To store the label names corresponding to each label

    label_index = 0
    for label_name in os.listdir(root_folder):
        label_folder = os.path.join(root_folder, label_name)
        if os.path.isdir(label_folder):
            for filename in os.listdir(label_folder):
                if filename.endswith(".jpg"):
                    img_path = os.path.join(label_folder, filename)
                    img = cv2.imread(img_path, 0)
                    features.append(extract_hog_features(img))
                    labels.append(label_index)
                    label_names.append(label_name)
            label_index += 1

    return np.array(features), np.array(labels), label_names

classifiers = {
    'SVM': svm.LinearSVC(random_state=random_seed),
    'KNN': KNeighborsClassifier(n_neighbors=7),
    'NN': MLPClassifier(solver='sgd', random_state=random_seed, hidden_layer_sizes=(500,), max_iter=20, verbose=1)
}

dataset_root_symbols = "Models/dataset/symbols"

def run_experiment():
    features, labels, label_names = load_dataset_symbols(dataset_root_symbols)
    
    train_features, test_features, train_labels, test_labels = train_test_split(
        features, label_names, test_size=0.2, random_state=random_seed)
    
    for model_name, model in classifiers.items():
        print('############## Training', model_name, "##############")
        # Train the model only on the training features
        model.fit(train_features, train_labels)
        
        # Test the model on images it hasn't seen before
        accuracy = model.score(test_features, test_labels)
        
        print(model_name, 'accuracy:', accuracy*100, '%')
        
        # Save the SVM model
        if model_name == 'SVM':
            model_filename = "svm_model_symbols.joblib"
            joblib.dump(model, model_filename)
            print("Saved SVM model to:", model_filename)

run_experiment()
