# Project Jet2Holidays (Transcription App)

This is a Streamlit web application that provides a user-friendly interface to transcribe audio files using the power of Whisper models.

## Features

- **Audio Transcription:** Upload your audio files (MP3, WAV, M4A) and get a full text transcription.
- **Efficient Processing:** The app uses in-memory processing to handle audio files, avoiding slow disk operations and making transcriptions faster.
- **Optimized Model Loading:** The Whisper model is cached on the first run, ensuring that subsequent transcriptions are processed without the delay of reloading the model.
- **Standardized Timestamp Formatting:** Timestamps are displayed in a consistent `MM:SS` format for improved readability.
- **Download Transcripts:** Users can enter a custom filename and download the full transcription as a `.txt` file.
- **User-Friendly Interface:** A spinner indicates when the transcription is in progress, and the final transcript is displayed in a collapsible expander to keep the UI clean.

## Changelog

### Version 1.2.0
- **Feature:** Added a "Transcribe" button, giving users explicit control over when to start the transcription.
- **UI:** Placed the transcription output and download options inside an expander for a cleaner interface.
- **UI:** Added a company logo next to the application title.
- **Improvement:** Standardized the timestamp format to a consistent `MM:SS` for all durations.

### Version 1.1.0
- **Feature:** Added a download button to save the transcript as a `.txt` file.
- **Feature:** Implemented in-memory audio processing, removing the need to save files to disk.
- **Bug Fix:** Cached transcription results to prevent the transcription from re-running when interacting with download widgets.

### Version 1.0.0
- **Feature:** Initial release of the transcription app.
- **Feature:** Implemented model caching (`@st.cache_resource`) to speed up processing on subsequent runs.
- **Feature:** Added a loading spinner to provide feedback during transcription.
- **Feature:** Implemented custom timestamp formatting for better readability.
