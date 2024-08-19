# Chronic Kidney Disease Prediction

This project focuses on predicting chronic kidney disease (CKD) using machine learning models, with an emphasis on minimizing false negatives. The primary goal is to ensure that as few cases of CKD as possible go undetected.

## Project Overview

Chronic Kidney Disease (CKD) is a significant health issue that requires early detection for effective treatment. The project leverages various machine learning algorithms to build predictive models, focusing on reducing false negatives to ensure early detection and treatment.

## Dataset

The dataset used in this project includes various medical indicators related to kidney function and patient demographics. Key features include:

- Hemoglobin (`hemo`)
- Serum Creatinine (`sc`)
- Specific Gravity (`sg`)
- Albumin (`al`)
- Red Blood Cells (`rbc`)
- Hypertension (`htn`)
- Diabetes Mellitus (`dm`)
- Blood Urea (`bu`)
- Sodium (`sod`)
- Blood Glucose Random (`bgr`)

## Algorithms Used

The project explored multiple machine learning algorithms to identify the best model for CKD prediction:

1. **Logistic Regression**
2. **Random Forest Classifier**
3. **Support Vector Machine (SVM)**
4. **Gradient Boosting**
5. **AdaBoost**
6. **K-Nearest Neighbors (KNN)**
7. **Naive Bayes**
8. **Decision Tree Classifier**

After experimenting with these algorithms, Logistic Regression with specific hyperparameters was selected as the final model due to its balance between simplicity and performance.

### Best Logistic Regression Model

The best hyperparameters identified for the Logistic Regression model are:
- `C: 1`
- `Solver: liblinear`

### Evaluation Metrics

- **Training Accuracy**: 0.99
- **Test Accuracy**: 0.97
- **Emphasis on Minimizing False Negatives**: Special attention was given to optimizing the recall (sensitivity) metric to ensure that CKD cases are not missed.

## Methodology

### Data Preprocessing

- Data was cleaned and prepared, focusing on handling missing values, normalization, and feature selection.
- The top 10 most important features were selected using a Random Forest model.

### Model Building

The primary model used in this project is **Logistic Regression**, which was chosen after testing multiple algorithms.

## Conclusion

The project successfully built a predictive model that emphasizes minimizing false negatives, thereby reducing the likelihood of undetected CKD cases. This model can serve as a valuable tool in medical settings to assist in the early detection and treatment of CKD.

## How to Run the Project

1. Clone the repository.
2. Install the necessary dependencies: `pip install -r requirements.txt`.
3. Run the Flask application: `python main_file.py`.
4. Access the web interface at `http://127.0.0.1:5000/`.

## Future Work

- Incorporate additional data sources for improved accuracy.
- Experiment with more advanced machine learning algorithms such as XGBoost or Neural Networks.
- Implement a real-time monitoring system.

## Acknowledgments

- Thanks to the open-source community for providing tools like Scikit-learn and Flask.
- A special acknowledgment to the creators of the CKD dataset.
