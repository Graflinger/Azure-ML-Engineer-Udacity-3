# Prediction of Water Quality - Overview

In order to be able, if the quality of a specific water source is good enough for consumption, a ML model in Azure is used to predict the quality. Therefore a labeled dataset from kaggle, with quality metrics for 3276 different water bodies, is used to train ML models. These models are implemented using Azure ML Studio. AutoML as well as Hyperdrive are used, to find the best model. Afterwards this model is deployed as an endpoint, so its accessable through a REST API.   


## Dataset

### Overview
The dataset is provides by kaggle. (https://www.kaggle.com/adityakadiwal/water-potability)

Its content is about quality metrics for different water bodies. These are labeld with the information of Potability. 0 if it is not safe for consumption and 1 if it is safe.

### Task
The task is to predict wether a water bodie is safe for consumption or not.

### Access
The dataset got uploaded as a registered dataset.

## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
A Random forest was chosen as model, because it performs great on task like this and has a lot of hyperparameters, so you can take benefit of hyperdrive.

The 3 picked hyperparameters are: 
- n_estimator (defines how many desicion trees are being used)
- criterion (the function to measure the quality of a split) 
- max depth (defines the max depth of any given tree in the forest)

### Results
The best run resulted in a accuracy of: #### using n_estimator = , criterion = and max_depth = 
To improve the performance more runs and a greater set of predefined hyperparameters could be used.

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
