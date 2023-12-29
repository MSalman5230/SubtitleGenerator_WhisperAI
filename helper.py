import os

upload_dir = "files"


def save_uploaded_file(uploaded_file):
    save_path = os.path.join(upload_dir, uploaded_file.name)
    with open(save_path, "wb") as f:
        if uploaded_file.size != f.write(uploaded_file.getbuffer()):
            return False
            # st.error("Upload Failed try again")
        else:
            return save_path
            # st.success("File has been successfully uploaded")


def read_file(file_path):
    # Read the contents of the file
    with open(file_path, "r", encoding="utf8") as file:
        file_contents = file.read()
        return file_contents

    # Display the file contents
    # st.text_area("File Contents:", file_contents)


def get_subtitle_path(file_name):
    base_name, ext = file_name.rsplit(".", 1)
    return base_name + ".srt"


def get_filename_from_path(file_path):
    return os.path.basename(file_path)

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' successfully deleted.")
    except OSError as e:
        print(f"Error deleting file '{file_path}': {e}")
