# Creating a frozenset from a list
my_frozenset = frozenset([1, 2, 3, 4, 5])
print(my_frozenset)

# Creating a frozenset from a tuple
fs = frozenset((1, 2, 3, 4, 5))
print(fs)

a = frozenset([1, 2, 3, 4])
b = frozenset([3, 4, 5, 6])

# Union
print(a | b)  # frozenset({1, 2, 3, 4, 5, 6})

# Intersection
print(a & b)  # frozenset({3, 4})

# Difference
print(a - b)  # frozenset({1, 2})

# Symmetric Difference
print(a ^ b)  # frozenset({1, 2, 5, 6})

'''
Problem Statement
You are managing a system that tracks different investment portfolios for clients. 
Each portfolio is a combination of different stocks, and once a portfolio is defined, it should not change. 
This helps in ensuring the consistency and integrity of the portfolios over time.
'''

# Define some portfolios using frozenset
portfolio1 = frozenset({"AAPL", "GOOGL", "TSLA"})
portfolio2 = frozenset({"MSFT", "AMZN", "NFLX"})
portfolio3 = frozenset({"AAPL", "MSFT", "GOOGL"})

# Dictionary to store the performance of each portfolio
portfolio_performance = {
    portfolio1: {"Q1": 5.0, "Q2": 7.5, "Q3": 6.0, "Q4": 8.2},
    portfolio2: {"Q1": 3.2, "Q2": 4.1, "Q3": 5.3, "Q4": 6.7},
    portfolio3: {"Q1": 4.5, "Q2": 5.9, "Q3": 6.8, "Q4": 7.4}
}

# Function to add a new portfolio performance (immutable portfolios)
def add_portfolio_performance(portfolio, performance):
    if portfolio in portfolio_performance:
        print("Portfolio already exists. Cannot modify existing portfolio.")
    else:
        portfolio_performance[portfolio] = performance

# Attempt to add a new portfolio
new_portfolio = frozenset({"TSLA", "NVDA", "AMD"})
new_performance = {"Q1": 6.5, "Q2": 7.0, "Q3": 8.1, "Q4": 9.3}

add_portfolio_performance(new_portfolio, new_performance)

# Print all portfolio performances
for portfolio, performance in portfolio_performance.items():
    print(f"Portfolio: {portfolio}")
    for quarter, value in performance.items():
        print(f"  {quarter}: {value}%")

# Attempt to modify an existing portfolio (should not allow modification)
add_portfolio_performance(portfolio1, {"Q1": 6.0, "Q2": 8.0, "Q3": 7.0, "Q4": 9.0})
