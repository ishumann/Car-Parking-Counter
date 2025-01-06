import streamlit as st


def main():
    st.set_page_config(
        page_title="Car Parking Counter",
        page_icon="🤖",
        layout="centered",
        initial_sidebar_state="auto",
    )
    st.header("Counting Available Parking Slots")




    with st.sidebar:
        st.title("Upload:")
        uploaded_files = st.file_uploader(
    "Upload Image for configuring parking slots and a video for detecting empty parking slots:",
    type=["jpg", "jpeg", "mp4", "avi", 'png'],
    accept_multiple_files=True,
    )
        if uploaded_files:
            image_file = next((f for f in uploaded_files if f.type.startswith('image/')), None)
            video_file = next((f for f in uploaded_files if f.type.startswith('video/')), None)

        if uploaded_files:
            image_file = next(
                (f for f in uploaded_files if f.type.startswith("image/")), None
            )
            video_file = next(
                (f for f in uploaded_files if f.type.startswith("video/")), None
            )

            if image_file:
                
                # image = process_image(image_file)
                # draw_boxes = DrawBoxes(image)
                # st.image(
                #     draw_boxes.image,
                #     caption="Draw boxes on the image",
                #     use_column_width=True,
                # )
                pass

            if video_file:
                st.video(video_file)

        if st.button("Submit and Process"):
            with st.spinner("Processing..."):
                empty_slots_count = count_empty_slots(image, video_file)
                st.success(f"Processing Done. Empty Parking Slots: {empty_slots_count}")



if __name__ == "__main__":
    main()

