import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from config import DATABASE_URL

def set_background():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://wa-uploads.profitroom.com/castellsonclaret/2400x1080/17282996803046_castellsonclaretpoolv1.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .block-container {
            background-color: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background()

# Load database using config
engine = create_engine(DATABASE_URL)

st.title("Hotel Recommendation System")

city_list = pd.read_sql("SELECT DISTINCT City FROM hotels", engine)['City'].dropna().tolist()

# Sidebar filters
st.sidebar.header("Filter Options")
city = st.sidebar.selectbox("Choose a City", city_list)
rating_range = st.sidebar.slider("Rating Range", 0.0, 5.0, (3.0, 5.0), step=0.1)
search_name = st.sidebar.text_input("Search by Hotel Name (Optional)")

# Query execution
if st.sidebar.button("Find Hotels"):
    query = f"""
        SELECT Name, Rating, Address, "Map Link"
        FROM hotels
        WHERE City = '{city}'
        AND Rating BETWEEN {rating_range[0]} AND {rating_range[1]}
    """
    if search_name:
        query += f" AND Name LIKE '%{search_name}%'"
    query += " ORDER BY Rating DESC"

    df = pd.read_sql(query, engine)

    if df.empty:
        st.warning("No hotels found matching your criteria.")
    else:
        st.success(f"Found {len(df)} hotels in {city}")
        df['Google Maps'] = df['Map Link'].apply(lambda x: f'<a href="{x}" target="_blank">View Hotel</a>')
        df = df.drop(columns=["Map Link"])
        st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)

# Footer
st.markdown("""
    <hr>
    <center>
    <small>Developed by Abhishek P Unnithan | Powered by Google Places API & Streamlit</small>
    </center>
""", unsafe_allow_html=True)
