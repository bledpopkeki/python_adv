import pandas as pd
import streamlit as st
import plotly.express as px

st.header('display in frames')

df = pd.DataFrame({
    'Name': ['bledbabatm','yllaimbontaparta','neverbuissnes'],
    'Age': [59,74,67],
    'City':['Prishtine','Gjakove','Peje']
})

st.write(df)

st.title("Best selling Book Analysis")
st.write("This app analyzes the Amazon top selling books from 2009 to 2023.")

books_df = pd.read_csv('Module18/bestsellers_with_categories_2022_03_27.csv')

st,subheader("Summary statistics")
total_books = books_df.shape[0]
unique_titles = books_df['Name'].nunique()
average_rating = books_df['User Rating'].mean()
average_price = books_df['price'].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total books", total_books)
col2.metric("Unique Titles", unique_titles)
col3.metric("Average rating", f"{average_rating:.2f}")
col4.metric("Average price", f"{average_price:.2f}")

st.subheader("dataset preview")
st.write(books_df.head())

col1, col2 = st.columns(2)

with col1:
    st.subheader("top 10 book titles")
    top_titles = books_df['Name'].value_counts.head(10)
    st.bar_chart(top_titles)

with col2:
    st.subheader("top 10 Authors")
    top_authors = books_df['author'].value_ccounts().head(10)
    st.bar_chart(top_authors)


st.subheader("Number of fiction vs nonfiction books over the years")
size = books_df.groupby(['year', 'genre']).size().reset_index(name='counts')
fig = px.bar(size, x='Year', y='Counts', color='Genre',title="Number of fiction books",
             color_discrete_sequence=px.sequential.Plasma, barmode='group')

st.plotly_chart(fig)