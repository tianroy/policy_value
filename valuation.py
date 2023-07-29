#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 21:55:40 2023

@author: roy
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('life_expect.csv')

# Define your function here
def policy_valuation(data, starting_age, gender, num_simulations, risk_factor, policy_size, annual_premium, discount_rate):
    ages_of_death = []
    pv_values = []
    for _ in range(num_simulations):
        age = starting_age
        while True:
            death_probability = data.loc[data['age'] == age, gender].values[0] * risk_factor
            if np.random.rand() <= death_probability:
                ages_of_death.append(age)
                pv_death_benefit = policy_size / ((1 + discount_rate) ** (age - starting_age))
                pv_premiums = sum([annual_premium *((1 + annual_premium_increase) ** i) / ((1 + discount_rate) ** i) for i in range(age - starting_age)])
                pv_values.append(pv_death_benefit - pv_premiums)
                break
            age += 1
            if age > max(data['age']):
                ages_of_death.append(age)
                pv_values.append(-sum([annual_premium / ((1 + discount_rate) ** i) for i in range(age - starting_age)]))
                break
    return ages_of_death, pv_values

# Use Streamlit to create sliders for the inputs
st.title("Life Settlement Valuation Service")
policy_size = 100  
st.text(f'Policy Size: {policy_size} USD')
gender = st.selectbox('Gender', options=['male', 'female'])
starting_age = st.slider('Age', min_value=0, max_value=110, value=80, step=1)
annual_premium = st.slider('Annual Premium, eg: +2 means you pay 2 USD to policy owner per year', min_value=-10.0, max_value=20.0, value=1.8, step=0.1)
annual_premium_increase = st.slider('Annual Premium Increase %, 12 means today you pay 2 usd the next year you pay 2.24 and so on', min_value=0.0, max_value=30.0, value=12.0, step=1.0) / 100
discount_rate = st.slider('Discount Rate %, 5.3 means 5.3%', min_value=0.0, max_value=20.0, value=5.3, step=0.1) / 100
risk_factor = st.slider('Risk Factor, eg: 1.1 means 10% more chance of dying each year comparing with average US person', min_value=0.5, max_value=1.5, value=1.0, step=0.1)
num_simulations = st.slider('Number of Simulations, small number will speed up the calculation', min_value=1000, max_value=10000, value=4000, step=500)

# Run the function and store its outputs when the button is pressed
if st.button('Calculate!'):
    with st.spinner('Running the simulation...'):
        ages_of_death, pv_values = policy_valuation(data, starting_age, gender, num_simulations, risk_factor, policy_size, annual_premium, discount_rate)
    st.success('Calculation completed!')
    st.write(f"Expected life till: {np.mean(ages_of_death):.1f}")
    st.write(f"Policy valuation: {np.mean(pv_values):.1f}")
    # Plot the results
    fig, ax = plt.subplots()
    ax.hist(ages_of_death, bins=range(starting_age, max(ages_of_death)+1), alpha=0.7, edgecolor='black')
    ax.set_title('Distribution of Age of Death')
    ax.set_xlabel('Age of Death')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)
    fig, ax = plt.subplots()
    ax.hist(pv_values, bins=100, alpha=0.7, edgecolor='black')
    ax.set_title('Distribution of Policy Valuation')
    ax.set_xlabel('Policy Valuation')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)
    
st.markdown('© Olivia & Co. 2023')

