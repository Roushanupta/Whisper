if __name__ == "__main__":
    DIRECTORY_TO_WATCH = "path/to/media/files"
    
    # Initial scan and processing
    for media_file in scan_directory(DIRECTORY_TO_WATCH):
        transcribe_audio(media_file)

    # Start monitoring for new files
    monitor_directory(DIRECTORY_TO_WATCH)
