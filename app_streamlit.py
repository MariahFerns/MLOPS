
import streamlit as st

st.write('# Streamlit Basic Calculator')

# input 2 numbers
number1 = st.number_input('Enter first number')
number2 = st.number_input('Enter second number')

# perform the calculations
add = number1 + number2
sub = number1 - number2
mul = number1 * number2
# div = number1 / number2

# Display my results
st.write(f'The addition of {number1} and {number2} is {add}')
st.write(f'The subtraction of {number1} and {number2} is {sub}')
st.write(f'The multiplication of {number1} and {number2} is {mul}')
# st.write(f'The division of {number1} and {number2} is {div}')
