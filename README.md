# Telecom Churn Prediction Dataset

## Overview

This dataset contains information on customers of a telecom company. The primary goal of this dataset is to predict customer churn—whether a customer will leave the telecom provider (churn) or continue using the service. Predicting churn allows the company to retain customers by taking proactive steps to improve their satisfaction and engagement.

## Dataset Description

The dataset includes 20 features, which capture various attributes related to customer demographics, account details, and usage patterns. The key target variable is `churn`, indicating whether a customer has left the service or not. Here’s a description of each column:

| Column           | Description                                                                                     |
|------------------|-------------------------------------------------------------------------------------------------|
| `state`          | The U.S. state where the customer is located.                                                   |
| `area.code`      | The area code of the customer.                                                                  |
| `account.length` | Duration (in days) the account has been active.                                                 |
| `voice.plan`     | Whether the customer is subscribed to a voice plan (yes or no).                                 |
| `voice.messages` | Number of voice messages received (if voice plan is active).                                    |
| `intl.plan`      | Whether the customer has an international plan (yes or no).                                     |
| `intl.mins`      | Minutes used in international calls.                                                            |
| `intl.calls`     | Number of international calls made.                                                             |
| `intl.charge`    | Charges incurred for international calls.                                                       |
| `day.mins`       | Minutes used during the day.                                                                    |
| `day.calls`      | Number of calls made during the day.                                                            |
| `day.charge`     | Charges incurred for calls made during the day.                                                 |
| `eve.mins`       | Minutes used during the evening.                                                                |
| `eve.calls`      | Number of calls made during the evening.                                                        |
| `eve.charge`     | Charges incurred for evening calls.                                                             |
| `night.mins`     | Minutes used during the night.                                                                  |
| `night.calls`    | Number of calls made during the night.                                                          |
| `night.charge`   | Charges incurred for night calls.                                                               |
| `customer.calls` | Number of calls made to customer support by the user.                                           |
| `churn`          | Target variable indicating if the customer churned (yes) or not (no).                          |

## Objective

The objective of this dataset is to build a predictive model that can accurately classify customers into two groups: those likely to churn and those likely to stay. This can help telecom companies retain customers by identifying at-risk customers and addressing their concerns before they leave.

## Churn Prediction

Churn prediction is an essential area in customer relationship management (CRM) and is widely used in industries like telecom, banking, and insurance. In this dataset, "churn" is defined as a customer leaving the service. By analyzing the factors that contribute to churn, companies can develop targeted marketing campaigns, improve service quality, or make necessary adjustments to their pricing and support strategies.

### Key Steps in Churn Prediction

1. **Data Preprocessing**: Clean the data by handling missing values, normalizing numerical features, and encoding categorical variables.
2. **Feature Engineering**: Create new features or adjust existing features to improve the predictive power of the model.
3. **Modeling**: Use classification algorithms like logistic regression, decision trees, or ensemble methods to build a predictive model.
4. **Evaluation**: Evaluate model performance using metrics like accuracy, precision, recall, and F1 score. Fine-tune the model based on these metrics.
5. **Deployment**: Integrate the predictive model into a production environment to enable real-time or batch processing of churn predictions.

By using this dataset, you can experiment with various machine learning algorithms and techniques to gain insights into customer behavior and the factors leading to churn. This can ultimately help improve customer retention and increase business revenue.


Link to the deployed App:- https://telecomechurnprediction-7prokjhha4796ddws2pcxj.streamlit.app/
