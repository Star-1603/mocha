import streamlit as st
import os
import google.generativeai as genai
os.environ['GOOGLE_API_KEY']="AIzaSyAB7zjcm2GpAH1vJLu1ePHjYmi_MYfIx1U"
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
# function to load Gemini Pro model
model = genai.GenerativeModel('gemini-pro')

def main():
    # page configuration
    st.set_page_config(page_title="Museum Info", layout="wide")
    # formatting for the header
    st.title("MOCHA: your own Museum ticket booking assistant")
    # sidebar formatting
    st.sidebar.subheader("Museum and Type")
    platform_options = {
        "North India": ["National Museum, Delhi","Sanskriti Kendra Museum", "National Science centre", "Virasat E Khalsa"],
        "Western India": ["Rajiv Gandhi Regional Museum of Natural History", "Jaisalmer War Museum", "Sardar Vallabh bhai patel National Memorial"],
        "Southern India": ["Government Museum, Chennai", "Salar Jung Museum, Hyderabad", "Telugu Samskritha Niketanam", "Railway Museum, Mysore"],
        "Eastern India": ["Victoria Memorial", "Ashutosh Museum Of Indian Art", "Fort William", "Odisha State Museum","Jawahar Lal Museum, Itanagar"],
        "Central India": ["Indore Museum", "Bharat Bhavan", "Nehru Science Centre, Mumbai","Chhatrapati Shivaji Maharaj Vastu Sangrahalaya"]
    }
    selected_platform = st.sidebar.selectbox("Select Region", list(platform_options.keys()))
    selected_option = st.sidebar.radio("Select Museum", platform_options[selected_platform])

    # get input
    st.subheader("Learn More about the Museum You wish to visit")
    content = selected_option.lower()

    st.subheader(f"Generated information for this Museum: {selected_option.title()}")

    if st.button("Show Information"):
        try:
         
            # Generate the content using the model (placeholder for actual model call)
            response = model.generate_content(f"Generate a detailed explaination for {content}, the history and significance of the museum")

            # Extract the generated text (assuming response.text is the output format)
            generated_text = response.text

            if response.parts:
                    titles = [part.text.strip() for part in response.parts]
                    for i, title in enumerate(titles, start=1):
                        st.write(f"{i}. {title}")
            else:
                st.write("No content generated.")
        except Exception as e:
            st.error(f"Error: {str(e)}")
main()
# Button for Content Generation
