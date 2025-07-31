import streamlit as st
import pandas as pd

st.title("Hello, Streamlit!")
st.header("Welcome to my Streamlit app!")
st.subheader("This is a subheader")
st.write("This is a simple Streamlit application to demonstrate basic functionality.")
st.markdown("""
### my favourite programming languages
- Python
- sql
""")
st.code("""
def hello_world():
    print("Hello, World!")
""")

st.latex(r"""x^2 + y^2 = z^2""")

# Demo DataFrame
import numpy as np
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Score': np.random.randint(60, 100, 4)
}
df = pd.DataFrame(data)
st.write("## Demo DataFrame")
st.dataframe(df)

# Streamlit metric example
st.write("## Key Metric Example")
st.metric(label="Average Score", value=int(df['Score'].mean()), delta="+5")

# Streamlit JSON example
st.write("## Data as JSON")
st.json(data)

st.image("demo.webp")

st.sidebar.title("This is a sidebar where you can add additional information or controls.")


col1, col2 = st.columns(2)
with col1:
    st.write("This is the first column.")
    st.button("Click me!")
with col2:
    st.write("This is the second column.")
    st.checkbox("Check me!")

email = st.text_input("Enter email:")
number = st.number_input("Enter a number")
date = st.date_input("Select a date")

st.selectbox("Select a programming language",
             options=["Python", "JavaScript", "Java", "C++", "Ruby"])

# File upload and CSV reader
st.write("## Upload and Display a CSV File")
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
if uploaded_file is not None:
    df_uploaded = pd.read_csv(uploaded_file)
    st.write("### Uploaded CSV Data")
    st.dataframe(df_uploaded)
 
