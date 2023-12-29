import streamlit as st
from whisper_process import get_subtitles  # Replace with your actual function
from helper import save_uploaded_file


@st.cache_data(show_spinner=False)
def process_get_subtitles(file_path):
    return get_subtitles(file_path)


def clear_old_subtitle_state():
    if "sub_filename" in st.session_state:
        del st.session_state["sub_filename"]
    if "file_contents" in st.session_state:
        del st.session_state["file_contents"]


st.title("Subtitle Generator - WisperAI")


def main():
    uploaded_file = st.file_uploader(
        "Choose a video file",
        type=["mp4", "mkv", "avi", "wav", "mp3"],
        on_change=clear_old_subtitle_state,
    )

    if uploaded_file is not None:
        file_details = {
            "Filename": uploaded_file.name,
            "FileType": uploaded_file.type,
            "FileSize": uploaded_file.size / (1024 * 1024),
        }
        st.success("File Uploaded")

        # if st.button("Process"):
        with st.spinner("Processing..."):
            sub_filename, file_contents = process_get_subtitles(uploaded_file)
            st.session_state["sub_filename"] = sub_filename
            st.session_state["file_contents"] = file_contents
            st.success("Processing complete!")
            st.write(st.session_state["sub_filename"])

    if "sub_filename" in st.session_state and "file_contents" in st.session_state:
        st.download_button(
            label="Download subtile (.srt)",
            file_name=st.session_state["sub_filename"],
            data=st.session_state["file_contents"],
            #key="srt-file",
            help="Save this file and upload it to your video player.",
        )


if __name__ == "__main__":
    main()
