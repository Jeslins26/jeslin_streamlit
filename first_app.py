import streamlit as st
st.title("Welcome, This is Jeslin S")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("CSV file uploaded successfully!")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error reading file: {e}")
data = {
    "Name": ["Jeslin", "Rahul", "Priya", "mosmi"],
    "Course": ["Python", "Java", "C++", "Web Dev"],
    "Score": [85, 90, 78, 92]
}

df = pd.DataFrame(data)
