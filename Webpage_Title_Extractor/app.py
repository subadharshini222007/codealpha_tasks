import streamlit as st
from main import extract_webpage_title
import requests

st.set_page_config(
    page_title="Webpage Title Extractor",
    page_icon="🌐",
    layout="centered"
)

st.title("🌐 Automated Webpage Title Extractor")

st.write(
    "Enter any public webpage URL to automatically "
    "extract its title and save the result."
)

url = st.text_input(
    "Enter Webpage URL",
    placeholder="https://example.com"
)

if st.button("Extract Webpage Title"):

    if not url.strip():
        st.warning("Please enter a webpage URL.")

    else:
        try:
            title = extract_webpage_title(url)

            if title:
                result = (
                    f"Webpage URL: {url.strip()}\n"
                    f"Webpage Title: {title}\n"
                )

                with open("output.txt", "w", encoding="utf-8") as file:
                    file.write(result)

                st.success("Webpage title extracted successfully!")

                st.subheader("Extracted Title")
                st.write(title)

                st.download_button(
                    label="Download Result",
                    data=result,
                    file_name="output.txt",
                    mime="text/plain"
                )

            else:
                st.warning("No title found on this webpage.")

        except ValueError as error:
            st.error(str(error))

        except requests.exceptions.RequestException:
            st.error(
                "Unable to access this webpage. "
                "Please check the URL and try again."
            )

        except Exception as error:
            st.error(f"An unexpected error occurred: {error}")