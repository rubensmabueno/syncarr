import os

from syncarr.providers.ffsubsync import FFSubsyncSync


class ScannerService:
    def execute(self, scan_directory):
        for root, dirs, files in os.walk(scan_directory):
            for file in files:
                if file.lower().endswith(('.mp4', '.avi', '.mkv')):
                    video_file_path = os.path.join(root, file)
                    video_file_name = os.path.splitext(file)[0]

                    for subtitle_file in files:
                        if subtitle_file.startswith(video_file_name) and subtitle_file.lower().endswith('.srt'):
                            subtitle_file_path = os.path.join(root, subtitle_file)

                            self._generate_subtitle(video_file_path, subtitle_file_path)

    def _generate_subtitle(self, video_file_path: str, subtitle_file_path: str) -> None:
        FFSubsyncSync().sync(video_file_path, subtitle_file_path)
