import streamlit as st
import google.generativeai as genai
import os

# 🔐 Use environment variable for safety
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

st.title("🌱 Smart Farming Assistant")
st.write("Get region-specific, multilingual farming advice powered by Gemini")

# User inputs
location = st.text_input("Enter your location (e.g., Tamil Nadu, India)")
crop_stage = st.selectbox("Select crop stage", ["Planting", "Growing", "Harvesting"])
constraints = st.text_input("Constraints (e.g., organic-only, low water availability)")
query = st.text_area("Ask your farming question")

# 🇮🇳 All 22 Official Indian Languages
language = st.selectbox(
    "Select response language",
    [
        "English",
        "Hindi",
        "Bengali",
        "Telugu",
        "Marathi",
        "Tamil",
        "Urdu",
        "Gujarati",
        "Kannada",
        "Odia",
        "Malayalam",
        "Punjabi",
        "Assamese",
        "Maithili",
        "Santali",
        "Kashmiri",
        "Nepali",
        "Konkani",
        "Sindhi",
        "Dogri",
        "Manipuri (Meitei)",
        "Bodo",
        "Sanskrit"
    ]
)

if st.button("Get Advice"):
    if query.strip():
        model = genai.GenerativeModel("models/gemini-2.5-flash")

        prompt = (
            f"Location: {location}\n"
            f"Crop Stage: {crop_stage}\n"
            f"Constraints: {constraints}\n"
            f"Question: {query}\n\n"
            f"Respond ONLY in {language}.\n"
            "Give 3-5 short bullet points. Use simple language suitable for farmers."
        )

        response = model.generate_content(contents=prompt)

        st.subheader("Farming Advice")

        for line in response.text.split("\n"):
            line = line.strip()
            if line:
                st.markdown(f"- {line}")
    else:
        st.warning("Please enter a farming question.")
