import os
import subprocess


class FFSubsyncSync:
    def __init__(self, resource_path: str, video_file_name: str, subtitle_file_name: str):
        self._resource_path = resource_path
        self._video_file_name = video_file_name
        self._subtitle_file_name = subtitle_file_name

    @property
    def video_file_path(self) -> str:
        return os.path.join(self._resource_path, self._video_file_name)

    @property
    def original_subtitle_file_path(self) -> str:
        return os.path.join(self._resource_path, self._subtitle_file_name)

    @property
    def new_file_name(self) -> str:
        name_part, extension = os.path.splitext(self._subtitle_file_name)

        new_name = f"{name_part}-ffsubsync"

        return f"{new_name}{extension}"

    @property
    def new_subtitle_file_path(self) -> str:
        return os.path.join(self._resource_path, self.new_file_name)

    def sync(self) -> None:
        command = ["ffs", self.video_file_path, "-i", self.original_subtitle_file_path, "-o", self.new_subtitle_file_path]

        try:
            subprocess.run(command, check=True)
            print("Command executed successfully.")
        except subprocess.CalledProcessError as e:
            print("Error while executing command:", e)
