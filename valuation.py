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

def policy_valuation(starting_age, gender, num_simulations, risk_factor, policy_size, annual_premium, max_age, death_probabilities, discount_factors):
    ages_of_death = []
    pv_values = []
    for _ in range(num_simulations):
        age = starting_age
        while True:
            death_probability = death_probabilities.get(age, 0)
            if np.random.rand() <= death_probability or age > max_age:
                ages_of_death.append(age)
                # assume we get the death benefit at the end of the year
                # if start_age=60, client die at 60, death_benefit will be paid at 60y year_end and discounted at 1/1+r
                pv_death_benefit = policy_size * discount_factors[age - starting_age]
                # assume we pay premium at the end of the year
                # if start_age=60, client die at 60, you dont pay premium, first pay at 61y year_begin and discounted at 1/1+r
                pv_premiums = annual_premium * np.sum(discount_factors[:age - starting_age])
                pv_values.append(pv_death_benefit - pv_premiums)
                break
            age += 1
    return ages_of_death, pv_values

# Use Streamlit to create sliders for the inputs
st.title("Life Settlement Valuation Service")
policy_size = 100  
st.text(f'Policy Size: {policy_size} USD, paid at the end of the event year')
gender = st.selectbox('Gender', options=['male', 'female'])
starting_age = st.slider('Age', min_value=0, max_value=110, value=80, step=1)
annual_premium = st.slider('Annual Premium, eg: +3 means you pay 3 USD every year, premium is fixed every year for whole life insurance, first payable at the beginning of the next year', min_value=-10.0, max_value=20.0, value=3.0, step=0.1)
annual_premium_increase = st.slider('Annual Premium Increase %, 5 means: you pay 3 usd this year, the next year you pay 3x(1+5%)=3.15 usd and so on', min_value=0.0, max_value=20.0, value=0.0, step=1.0) / 100
discount_rate = st.slider('Discount Rate %, 5.3 means 5.3%', min_value=0.0, max_value=20.0, value=5.3, step=0.1) / 100
risk_factor = st.slider('Risk Factor, eg: 1.1 means 10% more chance of dying each year comparing with average US person', min_value=0.5, max_value=1.5, value=1.0, step=0.1)
num_simulations = st.slider('Number of Simulations, small number will speed up the calculation', min_value=10000, max_value=500000, value=100000, step=5000)

max_age = max(data['age'])
death_probabilities = {age: prob * risk_factor for age, prob in zip(data['age'], data[gender])}
discount_factors = (1 + discount_rate) ** -np.arange(max_age - starting_age + 1)

# Run the function and store its outputs when the button is pressed
if st.button('Calculate!'):
    with st.spinner('Running the simulation...'):
        ages_of_death, pv_values = policy_valuation(starting_age, gender, num_simulations, risk_factor, policy_size, annual_premium, max_age, death_probabilities, discount_factors)
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

