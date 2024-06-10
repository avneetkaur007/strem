import streamlit as st
st.title('Loan approval app')
st.write('Check your eligibilty')
c=st.number_input('Enter your credit score')
s=st.number_input('Enter your salary')

if s>=50000 and c>=500:
    st.write('Congratulations')
    st.balloons()
else:
    st.write('Sorry')
