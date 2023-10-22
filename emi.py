import streamlit as st

# Define a function to calculate emi
def calculate_emi(p, n, r):

	# Apply the formula
	emi = p * (r/100) * (1 + r/100)**n / ((1+r/100)**n -1)

	# Print the calculted EMI on screen
	st.write("EMI Calculated: ", round(emi,3))

# Define the Outstanding Loan Balance calculation function
def calculate_outstanding_balance(p, n, r, m):

	# Apply the formula
	balance = (p * ((1+r/100)**n - (1+r/100)**m) )/ ((1+r/100)**n - 1)

	# Print the calculated Outstanding Loan Balance on screen
	st.write("Outstanding Loan Balance Calculated: ", round(balance,3))

# Add the title to the app
st.title("EMI Calculator")

# Take the inputs from user
principal = st.slider("Loan Amount", 1000.0, 100000.0)
tenure = st.slider("Tenure in years", 1, 30)
roi = st.slider("Interest Rate (% P.A.)", 1, 15)
period = st.slider("Period after to check Outstanding Loan Balance in months", 1, tenure * 12)

# Calculate the 'n' and 'r' values
n = tenure * 12
r = roi / 12

# Create the buttons
emi_button = st.button("Calculate EMI")
balance_button = st.button("Calculate Outstanding Loan Balance")

# Call the functions based on the button is clicked.
if emi_button:
	calculate_emi(principal, n, r)

elif balance_button:
	calculate_outstanding_balance(principal, n, r, period)