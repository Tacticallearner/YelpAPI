import requests
import streamlit as st

def fetch_yacht_details():
    try:
        url = 'https://api.yourapp.com/yachts'
        headers = {
            'Content-Type': 'application/json',
            # Include API key if required
            # 'Authorization': 'Bearer YOUR_API_KEY'
        }
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            # Handle response errors
            st.error(f'Error fetching data: {response.status_code}')
            return None

        return response.json()
    except Exception as e:
        st.error(f'An error occurred: {e}')
        return None

# Using the function in a Streamlit app
yacht_data = fetch_yacht_details()
if yacht_data:
    for yacht in yacht_data:
        st.write(f"Name: {yacht['name']}")
        # Display other yacht details
else:
    st.write("No yacht data available.")
