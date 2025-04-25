import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


ROOT_FOLDER = Path(__file__).parent.parent
DRIVER_PATH = ROOT_FOLDER / "bin" / "chromedriver.exe"

LAUNCHER_PATH = Path.home() / "AppData" / "Local" / "Programs"


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    if os.environ.get("SELENIUM_HEADLESS") == "1":
        chrome_options.add_argument("--headless")

    chrome_service = Service(
        executable_path=str(DRIVER_PATH),
    )

    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

    return browser


if __name__ == "__main__":
    print(ROOT_FOLDER)
