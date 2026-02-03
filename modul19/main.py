from modul18.app import total_books, unique_titles, average_rating, top_titles
from modul9.polymorphism.built import max_value
import...

book_df = pd.read_csv('bestsellers_with)categories_2022_03_27.csv')

st.title("Bestselling books analysis")
st.write("This is a streamlit app")


st.sidebar.header("Add new book data")
with (st.sidebar.form("book_form")):
    new_name = st.text_input("Book Name")
    new_author = st.text_input("Author")
    new_user_rating = st.slider("User rating" , 0.0 , 5.0 , 0.1)
    new_reviews = st.number_input("Reviews" , min_value=0 , step=1)
    new_price = st.number_input("Price" , min_value=2009 , max_value=2026)
    new_year = st.number_input("Year" , min_value=2009 , max_value=2026 )
    new_genre = st.selectbox("Genre" , books_df['Genre'].unique())
    submit_button = st.form_submit_button(label="Add Book")

    if submit_button:
        new_data = {
            'Name' : new_name,
            'Author' : new_author,
            'User Rating' : new_user_rating,
            'Reviews' : new_reviews,
            'Price' : new_price,
            'Year' : new_year,
            'Genre' : new_genre
        }


        books_df = pd.concat([pd.DataFrame(new_data , index=[0]), books_df], ignore_index=True)
        books_df.to_csv('bestsellers_with_categories_2022_03_27.csv', index=False)
        st.sidebar.success("New Book added")

st.sidebar.heeader("Filter Options")
selected_author = st.sidebar.selectbox("Select Author" , ["All"] + list(books_df['Author'].unique()))
selected_year = st.sidebar.selectbox("Select year" , ["All"] + list(books_df['Year'].unique()))
selected_genre = st.sidebar.selectbox("Select Genre", ["All"]+ list(books_df['Genre'].unique()))
min_rating = st.sidebar.slider("Maximum user rating" , 0.0 , 5.0 , 0.1)
max_price = st.sidebar.slider("Max Price ", 0 , books_df['Price'].max(), books_df['Price'].max())

if selected_author != "All":
    filtered_books_df = filtered_books_df[filtered_books_df['Author'] == selcted_author]
if selected_author != "All":
    filtered_books_df = filtered_books_df[filtered_books_df['Year'] == selected_year]
if selected_author != "All":
    filtered_books_df = filtered_books_df[filtered_books_df['Genre'] == selcted_genre]

filtered_books_df = filtered_books_df[
    (filtered_books_df['User Rating'] >= min_rating) & (filtered_books_df['Price'] <= max_price)
]


st.subheader("Summary Statistics")
total_books = filtered_books_df.shape[0]
unique_titles = filtered_books_df['Name'].nunique()
average_rating = filtered_books_df['User Rating'].mean()
average_price = filtered_books_df['Price'].mean()

col1, col2,col3,col4 = st.columns(4)
col1.metric("Total Books", total_books)
col2.metric("Unique titles", unique_titles)
col3.metric("Average Rating", average_rating)
col4.metric("Average Price", average_price)

st.subheader("Dataset Preview")
st.write(filtered_books_df.head())

col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 selling books")
    top_titles = filtered_books_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)
with col2:
    st.subheader("Top 10 Authors")
    top_titles = filtered_books_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)