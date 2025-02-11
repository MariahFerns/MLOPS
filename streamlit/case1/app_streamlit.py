
import streamlit as st

st.write('# Streamlit Basic Calculator')

# input 2 numbers
number1 = st.number_input('Enter first number', value=0)
number2 = st.number_input('Enter second number', value=0)

# initialize variables
add=None
sub=None
mul=None
div=None

# perform the calculations
if number1 is not None and number2 is not None:
  add = number1 + number2
  sub = number1 - number2
  mul = number1 * number2
  # handle division by 0
  if number2 == 0:
    div = 'undefined (cannot divide by zero)'
  else:
    div = number1 / number2

# Display my results
st.write(f'The addition of {number1} and {number2} is {add}')
st.write(f'The subtraction of {number1} and {number2} is {sub}')
st.write(f'The multiplication of {number1} and {number2} is {mul}')
st.write(f'The division of {number1} and {number2} is {div}')
