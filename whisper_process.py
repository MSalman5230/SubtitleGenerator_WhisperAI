import stable_whisper as whisper
from helper import get_subtitle_path, read_file, get_filename_from_path,delete_file,save_uploaded_file



def get_subtitles(uploaded_file):
    import stable_whisper as whisper
    file_path = save_uploaded_file(uploaded_file)
    # import torch
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    subtitle_path = get_subtitle_path(file_path)
    result.to_srt_vtt(subtitle_path, word_level=False)
    print("Finished processing", subtitle_path)
    delete_file(file_path)
    # import gc; gc.collect(); torch.cuda.empty_cache(); del model
    return get_filename_from_path(subtitle_path), read_file(subtitle_path)
    # return "test.srt"
