import streamlit as st
from faster_whisper import WhisperModel
import os

# App title
st.title("Audio Transcription App")

@st.cache_resource
def load_model(size):
    """Loads and caches the Whisper model."""
    # or run on GPU with PyTorch
    # model = WhisperModel(size, device="cuda", compute_type="float16")
    model = WhisperModel(size, device="cpu", compute_type="int8")
    return model

# Model selection
model_size = "tiny"  # or "base", "small", "medium", "large"
model = load_model(model_size)

# File uploader
audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

if audio_file is not None:
    st.audio(audio_file, format='audio/wav')

    # Save the uploaded file temporarily
    with open(audio_file.name, "wb") as f:
        f.write(audio_file.getbuffer())
    
    st.info("Transcribing...")

    segments, info = model.transcribe(audio_file.name, beam_size=5)

    st.success("Transcription Complete")

    # Display transcription
    for segment in segments:
        st.write("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

    # Clean up the temporary file
    os.remove(audio_file.name)
