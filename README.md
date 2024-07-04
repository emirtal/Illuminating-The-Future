# Illuminating-The-Future

# Power Outage Prediction Project

## Overview
This project aims to develop analytical models that can accurately predict power outages in the United States. The goal is to assist power utilities and commercial companies in proactive decision-making, efficient resource allocation, and comprehensive contingency planning to minimize the financial impact and ensure a reliable supply of electricity.

## Background
In recent years, the United States has experienced an increase in power outages, primarily due to climate change and the limitations of the outdated power grid. Severe weather events such as hurricanes, storms, wildfires, and heatwaves have intensified, posing a significant threat to the power infrastructure. The outdated grid struggles to handle the growing electrical loads, exacerbating the problem.

Grid operators are focusing on accurate forecasting and effective load management to ensure proper grid operation. This involves analyzing historical data, weather patterns, and other relevant factors to predict electricity demand accurately and allocate resources efficiently.

## Objective
The project aims to propose a set of analytical models to predict power outages, benefiting power utilities and commercial companies by enabling proactive decision-making, efficient resource allocation, and comprehensive contingency planning.

## Approach
1. **Data Consolidation and Cleaning**:
   - Consolidated weather data from NOAA and outage data for CA and NY.
   - Processed and cleaned data using Python and R to ensure quality and compatibility for modeling.

2. **Exploratory Modeling**:
   - Explored initial models using Linear and Logistic Regression.
   - Due to the lack of load data, focused on weather and calendar features.

3. **Model Selection**:
   - Evaluated Logistic Regression, Decision Tree, Random Forest, SVM, KNN, and Boosted Tree algorithms.
   - Used SMOTE oversampling to balance the dataset.
   - Selected CatBoost model with SMOTE for final predictions.

## Data Processing
1. **Weather Data**:
   - Downloaded daily weather data from NOAA for the past 10 years.
   - Cleaned and merged weather data for NY and CA.

2. **Outage Data**:
   - Processed timestamp and location data.
   - Cleaned Megawatt and customer data.
   - Merged weather and outage data on state and event date.

3. **Feature Engineering**:
   - Added calendar features (Season, Month, Day of Week, Weekend).
   - Transformed weather condition codes to binary values.

## Results
The final CatBoost model with SMOTE oversampling showed better performance than random predictions but still requires improvement. Key findings include:
1. **Extreme Precipitation**: Significant indicator of blackouts, with Ice Fog being the most predictive variable.
2. **Temperature Deviations**: Maximum Temperature was statistically significant but had a smaller effect.
3. **Calendar Variables**: Winter months significantly increased the probability of a blackout.

## Future Work
1. **Enhanced Weather Data**:
   - Incorporate more weather samples from different stations.
   - Include weather predictions for future dates.

2. **Additional Data Sources**:
   - Include daily electrical consumption trends.

3. **Brownout Data**:
   - Expand the dataset to include brownouts.

## Technical Details
- **Programming Languages**: Python, R
- **Libraries**: Pandas, Scikit-learn, CatBoost, SMOTE
- **Cloud Services**: AWS, Azure, GCP

## How to Use
1. **Clone the Repository**:
   ```bash
   git clone [repository_url]
