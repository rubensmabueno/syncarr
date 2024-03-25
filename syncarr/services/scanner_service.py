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

                            self._generate_subtitle(
                                os.path.dirname(os.path.abspath(video_file_path)),
                                os.path.basename(video_file_path),
                                os.path.basename(subtitle_file_path)
                            )

    def _generate_subtitle(self, resource_path: str, video_file_name: str, subtitle_file_name: str) -> None:
        FFSubsyncSync(resource_path, video_file_name, subtitle_file_name).sync()


if __name__ == '__main__':
    ScannerService().execute('/home/rubens/k3s/media/tv')
