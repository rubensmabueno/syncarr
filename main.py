from pathlib import Path

from syncarr.services.scanner_service import ScannerService

if __name__ == '__main__':
    ScannerService().execute(Path("./resources"))
