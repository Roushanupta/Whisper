import whisper

model = whisper.load_model("base")  # Choose "tiny", "small", "medium", "large"

def transcribe_audio(file_path):
    result = model.transcribe(str(file_path))
    transcript_path = file_path.with_suffix(".txt")
    
    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write(result["text"])
    
    print(f"Transcription saved: {transcript_path}")
