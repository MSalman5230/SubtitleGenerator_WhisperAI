# SubtitleGenerator_WhisperAI
 Generate accurate subtitles for videos with timestamp using WhisperAI\
 It uses OpenAI's WhisperAI for transcribing video/audio to English subtitles\
 And Streamlit for Web UI




# Setup
1. FFMPEG is required [https://www.ffmpeg.org/download.html]
2. Install Pytorch Stable [https://pytorch.org/get-started/locally/]
3. Install Stabilizing Timestamps for Whisper and streamlit

```bash
pip install -U stable-ts streamlit
```

# RUN
```bash
streamlit run app.py
```
