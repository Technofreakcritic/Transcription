import streamlit as st
from faster_whisper import WhisperModel
import os
import io

def format_timestamp(seconds):
    """Formats seconds into MM:SS or S.ss format."""
    if seconds < 60:
        return f"{seconds:.2f}s"
    else:
        minutes = int(seconds // 60)
        remaining_seconds = int(seconds % 60)
        return f"{minutes:02d}:{remaining_seconds:02d}"

# App title
st.title("Audio Transcription App")

@st.cache_resource
def load_model(size):
    """Loads and caches the Whisper model."""
    # or run on GPU with PyTorch
    # model = WhisperModel(size, device="cuda", compute_type="float16")
    model = WhisperModel(size, device="cpu", compute_type="int8")
    return model

@st.cache_data
def transcribe_audio(_model, audio_bytes):
    """Transcribes the audio bytes and caches the result."""
    segments, _ = _model.transcribe(io.BytesIO(audio_bytes), beam_size=5)
    return list(segments)  # Convert generator to list to cache results

# Model selection
model_size = "tiny"  # or "base", "small", "medium", "large"
model = load_model(model_size)

# File uploader
audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

if audio_file is not None:
    st.audio(audio_file, format='audio/wav')

    # Process audio in-memory
    audio_data = audio_file.getvalue()
    
    with st.spinner("Transcribing... Please wait."):
        segments = transcribe_audio(model, audio_data)
    
    # Display transcription and prepare for download
    transcript_text = ""
    for segment in segments:
        start_time = format_timestamp(segment.start)
        end_time = format_timestamp(segment.end)
        segment_text = f"[{start_time} -> {end_time}] {segment.text}"
        st.write(segment_text)
        transcript_text += segment_text + "\n"

    st.header("Download Transcript")
    # Get the base name of the uploaded file
    base_filename = os.path.splitext(audio_file.name)[0]
    default_txt_filename = f"{base_filename}_transcript.txt"
    
    # Text input for the user to name the file
    txt_filename = st.text_input("Enter the filename for the transcript:", default_txt_filename)

    # Download button
    st.download_button(
        label="Download as .txt",
        data=transcript_text,
        file_name=txt_filename,
        mime="text/plain"
    )


