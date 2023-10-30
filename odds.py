#Define a function to calculate the odds
def calculate_odds(probability): # add a colon for functions
    # The formula for odds is: odds = probability / (1 - probability)
    return probability / (1 - probability) #probability formula
# Get the probability of the event from the user
probability = float(input("Enter the probability of the event (between 0 and 1): "))
# Calculate the odds
odds = calculate_odds(probability)
# Print the results
print(f"The odds of the event happening are: {odds: .2f} to 1")