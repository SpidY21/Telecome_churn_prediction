import streamlit as st
import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from xgboost import XGBClassifier
import pickle

import warnings

warnings.filterwarnings('ignore')

model = pickle.load((open("model.sav", 'rb')))
scaler = pickle.load((open("scaling.sav", 'rb')))
pca = pickle.load((open("pca.sav", 'rb')))


def yes_no(str1):
    if str1 == 'Yes':
        return 1
    return 0


def prediction(input_data):
    prediction1 = model.predict(input_data)
    if prediction1 == 0:
        return 'Customer will Not Churn'
    else:
        return 'Customer will Churn'


def main():
    st.title('Telecom Churn Prediction')
    area_code_option = ['area_code_408', 'area_code_415', 'area_code_510']
    # yes_no_option = ['Yes', 'No']
    state_option = ['CT', 'ME', 'MA', 'NH', 'RI', 'VT', 'NJ', 'NY', 'PA', 'IL', 'IN', 'MI', 'OH', 'WI', 'IA', 'KS',
                    'MN', 'MO', 'NE', 'ND', 'SD', 'DE', 'FL', 'GA', 'MD', 'NC', 'SC', 'VA', 'DC', 'WV', 'AL', 'KY',
                    'MS', 'TN', 'AR', 'LA', 'OK', 'TX', 'AZ', 'CO', 'ID', 'MT', 'NV', 'NM', 'UT', 'WY', 'AK', 'CA',
                    'HI', 'OR', 'WA']
    state_to_region = {
        'Northeast': ['CT', 'ME', 'MA', 'NH', 'RI', 'VT', 'NJ', 'NY', 'PA'],
        'Midwest': ['IL', 'IN', 'MI', 'OH', 'WI', 'IA', 'KS', 'MN', 'MO', 'NE', 'ND', 'SD'],
        'South': ['DE', 'FL', 'GA', 'MD', 'NC', 'SC', 'VA', 'DC', 'WV', 'AL', 'KY', 'MS', 'TN', 'AR', 'LA', 'OK', 'TX'],
        'West': ['AZ', 'CO', 'ID', 'MT', 'NV', 'NM', 'UT', 'WY', 'AK', 'CA', 'HI', 'OR', 'WA']
    }

    # State column
    region = ['Midwest', 'Northeast', 'South', 'West']
    state = st.selectbox('State:- ', state_option)
    state = list(map(lambda x: x[0] if state in x[1] else None, state_to_region.items()))
    state = list(filter(None, state))[0] if any(state) else None
    state = region.index(state)

    # Area Code
    area_code = st.radio('Area Code', range(len(area_code_option)), format_func=lambda x: area_code_option[x])

    # Account Length
    account_length = int(
        st.number_input('Account Length:- ', placeholder='Integer value only', value=0, step=1, min_value=0))

    # Voice Plan
    voice_plan = st.checkbox('Has Voice Plan')
    voice_plan = 1 if voice_plan else 0

    # Voice Message
    voice_message = int(
        st.number_input('Voice Message:- ', placeholder='Integer value only', value=0, step=1, min_value=0))

    # International Plan
    int_plan = st.checkbox('Has Internation Plan')
    int_plan = 1 if int_plan else 0

    # International Minutes
    int_mins = st.number_input('International Minutes:- ', min_value=0.0)

    # Internation Calls
    int_calls = int(
        st.number_input('International Calls:- ', placeholder='Integer value only', value=0, step=1, min_value=0))

    # International Charge
    int_charge = st.number_input('International Charges:- ', min_value=0.0)

    # Day Minutes
    day_min = st.number_input('Day Minutes:- ', min_value=0.0)

    # Day Calls
    day_calls = int(st.number_input('Day Calls:- ', placeholder='Integer value only', value=0, step=1, min_value=0))

    # Day Charges
    day_charges = st.number_input('Day Charges:- ', min_value=0.0)

    # Evening Minutes
    eve_mins = st.number_input('Evening Minutes:- ', min_value=0.0)

    # Evening Calls
    eve_calls = int(st.number_input('Evening Calls:- ', placeholder='Integer value only', value=0, step=1, min_value=0))

    # Evening Charges
    eve_charge = st.number_input('Evening Charges:- ', min_value=0.0)

    # Night Minutes
    night_mins = st.number_input('Night Minutes:- ', min_value=0.0)

    # Night Calls
    night_calls = int(st.number_input('Night Calls:- ', placeholder='Integer value only', value=0, step=1, min_value=0))

    # Night Charges
    night_charge = st.number_input('Night Charges:- ', min_value=0.0)

    # Customer Calls
    customer_calls = int(
        st.number_input('Customer Calls:- ', placeholder='Integer value only', value=0, step=1, min_value=0))

    #
    # Input Variable
    input_var = [state, account_length, area_code, voice_plan, voice_message, int_plan, int_mins, int_calls, int_charge,
                 day_calls,
                 day_min, day_charges, eve_mins, eve_calls, eve_charge, night_mins, night_calls, night_charge,
                 customer_calls]  # 19
    input_var = np.asarray(input_var)

    # Scaling the input data
    to_be_scaling = [account_length, voice_message, int_mins, int_calls, int_charge, day_min, day_calls, day_charges,
                     eve_mins, eve_calls, eve_charge, night_mins, night_calls, night_charge]
    to_be_scaling = np.asarray(to_be_scaling)
    to_be_scaling = to_be_scaling.reshape(1, -1)
    to_be_scaling = scaler.transform(to_be_scaling)
    final_input = np.append(to_be_scaling, [state, area_code, voice_plan, customer_calls, int_plan])
    final_input = final_input.reshape(1, -1)

    # PCA
    pc = pca.transform(final_input)
    x_new = pc[:, 0:14]

    message = 'Made By Group 1...'
    if st.button('Predict...'):
        message = prediction(x_new)
    st.success(message)


if __name__ == '__main__':
    main()
