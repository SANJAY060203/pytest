import threading
import time
import os
import pytest
import uvicorn

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from src.ui.fastapi_ui import app as fastapi_app


@pytest.fixture(scope="module")
def live_server():
    """
    In CI: FastAPI runs in Docker → DO NOT start local server.
    Locally: start uvicorn on 127.0.0.1:5005.
    """
    fastapi_url = os.getenv("FASTAPI_URL")

    # CI mode
    if fastapi_url:
        return fastapi_url  # use running container

    # Local mode: start uvicorn manually
    config = uvicorn.Config(fastapi_app, host="127.0.0.1", port=5005, log_level="info")
    server = uvicorn.Server(config)

    thread = threading.Thread(target=server.run, daemon=True)
    thread.start()
    time.sleep(1)

    return "http://127.0.0.1:5005"


def create_driver():
    """Create a webdriver that works locally AND in Docker."""
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    selenium_url = os.getenv("SELENIUM_URL")

    # If SELENIUM_URL is set → use RemoteWebDriver (Docker / CI)
    if selenium_url:
        return webdriver.Remote(
            command_executor=selenium_url,
            options=options
        )

    # Otherwise use local Chrome
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service as ChromeService

    service = ChromeService(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


@pytest.mark.ui
def test_selenium_fastapi_echo(live_server):
    driver = create_driver()

    try:
        driver.get(live_server + "/")

        text_input = driver.find_element(By.ID, "text")
        btn = driver.find_element(By.ID, "btn")

        text_input.send_keys("fastapi-selenium")
        btn.click()
        time.sleep(0.5)

        result = driver.find_element(By.ID, "result").text
        assert result == "Echo: fastapi-selenium"

    finally:
        driver.quit()
