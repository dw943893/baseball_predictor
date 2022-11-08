from operator import mod
import pandas as pd
import streamlit as st
import pickle

def load_model():
  with open('logreg_home.pkl', 'rb') as f:
    the_model = pickle.load(f)
  return the_model

model = load_model()

st.title('Will the Home Team Win?')
st.subheader("Regular Season Games")
a = st.number_input('Home team batters hit by pitch', min_value = 0)
# when user pressed enter, need to store the input

b = st.number_input('Home team hits', min_value = 0)
c = st.number_input('Home team walks', min_value = 0)
d = st.number_input('Home team double plays', min_value = 0)
e = st.number_input('Home team errors', min_value = 0)
f = st.number_input('Home team left on base', min_value = 0)
g = st.number_input('Home team caught stealing', min_value = 0)
h = st.number_input('Visiting team left on base', min_value = 0)
i = st.number_input('Visiting team caught stealing', min_value = 0)
j = st.number_input('Visiting team errors', min_value = 0)
k = st.number_input('Visiting team double plays', min_value = 0)
l = st.number_input('Visiting team batters hit-by-pitch', min_value = 0)
m = st.number_input('Visiting team walks', min_value = 0)
n = st.number_input('Visiting team hits', min_value = 0)

if st.button('Submit'):
    data = {
    '58 home hit-by-pitch':[a],
    '51 home hits':[b],
    '59 home walks':[c],
    '38 visiting left on base':[h],
    '35 visiting caught stealing':[i],
    '76 home double plays':[d],
    '46 visiting errors':[j],
    '74 home errors':[e],
    '63 home caught stealing':[g],
    '48 visiting double plays':[k],
    '30 visiting hit-by-pitch':[l],
    '31 visiting walks':[m],
    '66 home left on base':[f],
    '23 visiting hits':[n]
    }
    test = pd.DataFrame(data)

    pred = model.predict(test)[0]
    if pred == "L":
        result = "Loss"
    else:
        result = "Win"
    probs = list(model.predict_proba(test)[0])
    prob = probs[0] if pred == 'L' else probs[1]
    st.write('Predicted Result: ', result)
    st.metric('Probability', f'{100 * round(prob, 2)}%')
