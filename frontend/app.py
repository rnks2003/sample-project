import streamlit as st

def initialise():
    st.set_page_config(
        page_title="Medical Image Diagnosis",
        page_icon=":material/clinical_notes:",
        layout="wide",
        initial_sidebar_state="auto"
    )

def run_image_processing(image):
    import time
    time.sleep(2)  # Simulate processing time
    return "Diagnosis: No abnormalities detected."

def render_image_processing():
    image = st.file_uploader("Upload a medical image for diagnosis", type=["png", "jpg", "jpeg"])
    if image:
        with st.spinner('Processing image...'):
            result = run_image_processing(image)
        st.success(result)


if __name__ == "__main__":
    initialise()
    render_image_processing()
