from pathlib import Path

SUPPORTED_FORMATS = (".mp3", ".wav", ".mp4", ".mkv", ".mov", ".flv", ".aac", ".m4a")

def scan_directory(base_dir):
    return [file for file in Path(base_dir).rglob("*") if file.suffix.lower() in SUPPORTED_FORMATS]
