# Guided Project: Mobile App for Lottery Addiction

# '''In this project, we are going to contribute to the development of a mobile app by writing a couple of functions that are mostly focused on calculating probabilities. The app is aimed to both prevent and treat lottery addiction by helping people better estimate their chances of winning.

# The app idea comes from a medical institute which is specialized in treating gambling addictions. The institute already has a team of engineers that will build the app, but they need us to create the logical core of the app and calculate probabilities. For the first version of the app, they want us to focus on the 6/49 lottery and build functions that can answer users the following questions:

# What is the probability of winning the big prize with a single ticket?
# What is the probability of winning the big prize if we play 40 different tickets (or any other number)?
# What is the probability of having at least five (or four, or three) winning numbers on a single ticket?

# The scenario we're following throughout this project is fictional — the main purpose is to practice applying probability and combinatorics (permutations and combinations) concepts in a setting that simulates a real-world scenario.

# ## Core Functions

# Below, we're going to write two functions that we'll be using frequently:

# - `factorial()` — a function that calculates factorials
# - `combinations()` — a function that calculates combinations
# '''

# READ ABOUT PROJECT in test.text

# import pandas as pd
# from collections import Counter
# from itertools import combinations
# import math

# # Load the lottery data
# lottery_canada = pd.read_csv('649.xls')

# # Function to extract winning numbers
# def extract_numbers(row):
#     """Extract winning numbers from a row."""
#     return set(row[4:10])  # Adjust this based on your data structure

# # Function to find most common pairs
# def common_number_pairs(data, top_n=10):
#     """
#     Function to find the most common pairs of numbers in lottery data.
    
#     Parameters:
#     data (pd.DataFrame): The DataFrame containing the lottery data.
#     top_n (int): The number of top pairs to return. Default is 10.
    
#     Returns:
#     List of tuples containing the most common pairs and their counts.
#     """
#     # Extract winning numbers
#     winning_numbers = data.apply(extract_numbers, axis=1)
    
#     # Initialize a Counter to count pairs
#     pair_counter = Counter()

#     # Count pairs of numbers that appear together
#     for numbers in winning_numbers:
#         pairs = combinations(sorted(numbers), 2)  # Get all pairs from the winning numbers
#         pair_counter.update(pairs)  # Update the count for each pair

#     # Find the most common pairs
#     most_common_pairs = pair_counter.most_common(top_n)  # Get top 'n' most common pairs
    
#     return most_common_pairs

# # Function to calculate one ticket probability

# def one_ticket_probability(user_numbers):
#     n_combinations = math.comb(49, 6)  # Use math.comb to calculate combinations
#     probability_one_ticket = 1 / n_combinations
#     percentage_form = probability_one_ticket * 100
    
#     formatted_percentage = f"{percentage_form:.7f}%"
#     print('Your chances to win the big prize with the numbers ' + str(user_numbers) + 
#           ' are ' + formatted_percentage + '. In other words, you have a 1 in ' + str(int(n_combinations)) + ' chances to win.')

# # Function to check historical occurrences of a combination
# def check_historical_occurrence(user_numbers, historical_numbers):   
#     user_numbers_set = set(user_numbers)
#     n_occurrences = historical_numbers.apply(lambda x: x == user_numbers_set).sum()
    
#     if n_occurrences == 0:
#         print(f"\nThe combination {user_numbers} has never occurred.")
#     else:
#         print(f"\nThe number of times combination {user_numbers} has occurred in the past is {n_occurrences}.")

# # Function to calculate multi-ticket probability
# def multi_ticket_probability(n_tickets):
#     n_combinations = math.comb(49, 6)
#     probability = n_tickets / n_combinations
#     percentage_form = probability * 100
#     print(f"\nYour chances to win the big prize with {n_tickets} tickets are {percentage_form:.6f}%.")

# # Main function to handle user choices
# def main():
#     while True:
#         choice = input('''\n
#                           ENTER 
#                           'mul' to check multiple tickets,
#                           'one' to check one ticket,
#                           'max_min' to find most or least frequent number,
#                           'common' to find common number pairs,
#                           'exit' to quit: 
#                           ENTER HERE ----> ''').lower()

#         if choice == 'exit':
#             print("Goodbye!")
#             break
        
#         elif choice == 'max_min':
#             flattened_numbers = [num for nums in lottery_canada.apply(extract_numbers, axis=1) for num in nums]
#             frequency_count = Counter(flattened_numbers)
#             most_frequent_number, highest_frequency = frequency_count.most_common(1)[0]
#             least_frequent_number, lowest_frequency = frequency_count.most_common()[-1]
#             print(f"\nThe most frequent number is {most_frequent_number} which appeared {highest_frequency} times.")
#             print(f"\nThe least frequent number is {least_frequent_number} which appeared {lowest_frequency} times.")
        
#         elif choice == 'common':
#             top_n = int(input("How many common pairs do you want to display? "))
#             most_common_pairs = common_number_pairs(lottery_canada, top_n)
#             print("\nMost common pairs of numbers that frequently appear together:")
#             for pair, count in most_common_pairs:
#                 print(f"Pair: {pair}, Count: {count}")

#         elif choice == 'mul':
#             try:
#                 n_tickets = int(input("Enter the number of tickets you want to purchase: "))
#                 multi_ticket_probability(n_tickets)
#             except ValueError:
#                 print("\nError: Please enter a valid number (int).")
        
#         elif choice == 'one':
#             while True:
#                 user_input = input("Enter 6 numbers separated by commas: ")
#                 try:
#                     user_numbers = list(map(int, user_input.split(',')))
#                     if len(user_numbers) == 6 and all(1 <= num <= 49 for num in user_numbers):
#                         one_ticket_probability(user_numbers)
#                         check_historical_occurrence(user_numbers, lottery_canada.apply(extract_numbers, axis=1))
#                         break
#                     else:
#                         print("\nError: You must enter exactly 6 numbers between 1 and 49.")
#                 except ValueError:
#                     print("\nError: Please enter valid numbers separated by commas.\n")
        
#         else:
#             print("\nInvalid input. Please try again.")

# # Run the program
# if __name__ == '__main__':
#     main()



# #check probability of multi ticket Enter -----> "mul"
# #check probability of single ticket Enter ----->"one"
# #check max and min frewuency of number Enter ---->"max_min"
# #check common number paires Enter -------> "common"
# #for exit Enter ------->"exit"



import pandas as pd
from collections import Counter
from itertools import combinations
import math
import streamlit as st

# Load the lottery data
lottery_canada = pd.read_csv('649.xls')

# Function to extract winning numbers
def extract_numbers(row):
    """Extract winning numbers from a row."""
    return set(row[4:10])  # Adjust this based on your data structure

# Function to find most common pairs
def common_number_pairs(data, top_n=10):
    winning_numbers = data.apply(extract_numbers, axis=1)
    pair_counter = Counter()
    for numbers in winning_numbers:
        pairs = combinations(sorted(numbers), 2)
        pair_counter.update(pairs)
    most_common_pairs = pair_counter.most_common(top_n)
    return most_common_pairs

# Function to calculate one ticket probability
def one_ticket_probability(user_numbers):
    n_combinations = math.comb(49, 6)
    probability_one_ticket = 1 / n_combinations
    percentage_form = probability_one_ticket * 100
    return f"{percentage_form:.7f}%"

# Function to check historical occurrences of a combination
def check_historical_occurrence(user_numbers, historical_numbers):
    user_numbers_set = set(user_numbers)
    n_occurrences = historical_numbers.apply(lambda x: x == user_numbers_set).sum()
    return n_occurrences

# Function to calculate multi-ticket probability
def multi_ticket_probability(n_tickets):
    n_combinations = math.comb(49, 6)
    probability = n_tickets / n_combinations
    percentage_form = probability * 100
    return f"{percentage_form:.6f}%"

# Main app function using Streamlit
def main():
    st.title("Lottery Number Analysis")

    menu = ['One Ticket Probability', 'Multi Ticket Probability', 'Max/Min Frequent Numbers', 'Common Number Pairs']
    choice = st.sidebar.selectbox("Choose an option", menu)

    if choice == 'One Ticket Probability':
        user_input = st.text_input("Enter 6 numbers separated by commas", "")
        if user_input:
            try:
                user_numbers = list(map(int, user_input.split(',')))
                if len(user_numbers) == 6 and all(1 <= num <= 49 for num in user_numbers):
                    probability = one_ticket_probability(user_numbers)
                    historical_occurrences = check_historical_occurrence(user_numbers, lottery_canada.apply(extract_numbers, axis=1))
                    st.write(f"Your chances to win with {user_numbers} are {probability}.")
                    st.write(f"This combination has occurred {historical_occurrences} times in the past.")
                else:
                    st.error("Please enter exactly 6 numbers between 1 and 49.")
            except ValueError:
                st.error("Invalid input! Please enter numbers separated by commas.")
    
    elif choice == 'Multi Ticket Probability':
        n_tickets = st.number_input("Enter the number of tickets", min_value=1, step=1)
        if n_tickets:
            probability = multi_ticket_probability(n_tickets)
            st.write(f"Your chances to win with {n_tickets} tickets are {probability}.")

    elif choice == 'Max/Min Frequent Numbers':
        flattened_numbers = [num for nums in lottery_canada.apply(extract_numbers, axis=1) for num in nums]
        frequency_count = Counter(flattened_numbers)
        most_frequent_number, highest_frequency = frequency_count.most_common(1)[0]
        least_frequent_number, lowest_frequency = frequency_count.most_common()[-1]
        st.write(f"The most frequent number is {most_frequent_number} which appeared {highest_frequency} times.")
        st.write(f"The least frequent number is {least_frequent_number} which appeared {lowest_frequency} times.")

    elif choice == 'Common Number Pairs':
        top_n = st.number_input("How many common pairs do you want to display?", min_value=1, step=1)
        if top_n:
            most_common_pairs = common_number_pairs(lottery_canada, top_n)
            st.write("Most common pairs of numbers that frequently appear together:")
            for pair, count in most_common_pairs:
                st.write(f"Pair: {pair}, Count: {count}")

# Run the app
if __name__ == '__main__':
    main()
