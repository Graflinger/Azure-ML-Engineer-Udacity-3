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
AutoML run configuration
![AutoML Config](https://github.com/Graflinger/Azure-ML-Engineer-Udacity-3/blob/bc4e283e67a3f0c7aa84c6ce48e8e08a6d959d66/pictures/automlconfig.PNG)

### Results
The auto ml run resulted in a Voting Ensebmle as the best model. Its parameters are shown in the screenshots below. 
How to improve even further: The automl run could have benefited from a longer running duration or better performing compute clusters.

Run details of the auto ml run
![Run Details](https://github.com/Graflinger/Azure-ML-Engineer-Udacity-3/blob/bc4e283e67a3f0c7aa84c6ce48e8e08a6d959d66/pictures/RunDetailsAutobestmodel.PNG)

Parameters of the best model
![Registered Datasets](https://github.com/Graflinger/Azure-ML-Engineer-Udacity-3/blob/bc4e283e67a3f0c7aa84c6ce48e8e08a6d959d66/pictures/votingensebmleparameters.PNG)

## Hyperparameter Tuning
A Random forest was chosen as model, because it performs great on task like this and has a lot of hyperparameters, so you can take benefit of hyperdrive.

The 3 picked hyperparameters are: 
- n_estimator (defines how many desicion trees are being used)
- criterion (the function to measure the quality of a split) 
- max depth (defines the max depth of any given tree in the forest)

### Results
The best run resulted in a accuracy of: 0.84615385 using n_estimator = 64 , criterion = "gini" and max_depth = 16
To improve the performance more runs and a greater set of predefined hyperparameters could be used.

Run Detail of Hyperparameter run
![Registered Datasets](https://github.com/Graflinger/Azure-ML-Engineer-Udacity-3/blob/bc4e283e67a3f0c7aa84c6ce48e8e08a6d959d66/pictures/RunDetailsHyper.PNG)

Best model with its hyperparameters
![Registered Datasets](https://github.com/Graflinger/Azure-ML-Engineer-Udacity-3/blob/bc4e283e67a3f0c7aa84c6ce48e8e08a6d959d66/pictures/hyperdriverundetails2.PNG)

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
To Query a the endpoint you can use the same code as in this screenshot:
![Registered Datasets](https://github.com/Graflinger/Azure-ML-Engineer-Udacity-3/blob/bc4e283e67a3f0c7aa84c6ce48e8e08a6d959d66/pictures/Calling%20Endpoint.PNG)

Just provide a array with all the information needed. (10 variables in the same order like the in the dataset)
## Screen Recording
link for the screencast

https://youtu.be/t4dWBNhtDqw
