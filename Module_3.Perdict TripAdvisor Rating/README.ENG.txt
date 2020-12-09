Work on the Project 3. Perdict TripAdvisor Rating

Created the first model using machine learning algorithms.

1. Let's say we are DS for TripAdvisor. One of the company's problems is dishonest restaurants that wind up their ratings.
One way to find such restaurants is to build a model that predicts the restaurant rating.
If the predictions of the model are very different from the actual result, then the restaurant may not be playing fair and should be tested.

The task is to create such a model.

We will work with a dataset containing information about 40,000 restaurants in Europe, and the model that we will train will have to predict the restaurant rating
according to TripAdvisor based on the data.

The code for creating the model is provided, the model works on the basis one of the powerful machine learning algorithms - RandomForestRegression.
but for the model to work, we need to load the correct data into it. Bringing the data into the required form will be our task.

For correct operation, all data in the dataframe that we will use when training the model must be in int or float formats.

2. Stages of work on the project, the main steps:

Initial data inspection;
Checking the number of unique values;
Checking data for empty values;
Handling None values;
Displaying data suitable for further model building;
Analysis of nominative variables and elimination of those that do not affect the operation of the model;
Generation \ creation of new features (Feature Engineering) (adding new columns to the dataframe) based on the information already contained in the data;
Translating categorical features into numeric ones, in machine learning we use the concept of dummy variables;
We use additional sources of information about cities and countries;
Conclusions.

3. Splitting the dataframe
First of all, to create a model, you need to divide the dataframe into a dataset that we will use to train the model (X), and into a target variable,
those. the value we will predict (y).

Further, we divide each of the obtained sets into training (train, used to train the model) and test (test, used to assess the accuracy of the model).
This division is carried out using a special method included in the Scikit-Learn library (sklearn).
In the parameters of the method, we indicate which part of the original dataframe should be left for testing the model. In our code, this part is 25% or 0.25.

4. Training and testing the model


5. Tasks with kaggle

Competition conditions:

All participants must use the same algorithm with the default parameters.
Allowed to use external data.
The solutions will be checked by teachers for their adequacy and reproducibility.
Baseline is available in the Notebooks tab of this competition

Notebook template with model options
Baseline contains settings for the model
(RandomForestRegression) == model = RandomForestRegressor (n_estimators = 100, verbose = 1, n_jobs = -1, random_state = RANDOM_SEED)

6. Submission

7. Result
score - 0.20
