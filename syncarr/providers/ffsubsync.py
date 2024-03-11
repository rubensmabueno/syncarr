import os
import subprocess


class FFSubsyncSync:
    def sync(self, video_path: str, input_subtitle_path: str) -> None:
        command = ["ffs", video_path, "-i", input_subtitle_path, "-o", f"{input_subtitle_path}_new.srt"]

        try:
            subprocess.run(command, check=True)
            os.rename(input_subtitle_path, f"{input_subtitle_path}.bak")
            os.rename(f"{input_subtitle_path}_new.srt", input_subtitle_path)
            print("Command executed successfully.")
        except subprocess.CalledProcessError as e:
            print("Error while executing command:", e)
