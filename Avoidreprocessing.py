import json

PROCESSED_LOG = "processed_files.json"

def load_processed_files():
    try:
        with open(PROCESSED_LOG, "r") as f:
            return set(json.load(f))
    except FileNotFoundError:
        return set()

def save_processed_file(file_path):
    processed_files = load_processed_files()
    processed_files.add(str(file_path))
    with open(PROCESSED_LOG, "w") as f:
        json.dump(list(processed_files), f)
    
def transcribe_audio(file_path):
    processed_files = load_processed_files()
    
    if str(file_path) in processed_files:
        print(f"Skipping already processed file: {file_path}")
        return
    
    result = model.transcribe(str(file_path))
    transcript_path = file_path.with_suffix(".txt")
    
    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write(result["text"])
    
    save_processed_file(file_path)
    print(f"Transcription saved: {transcript_path}")
