import re
from playwright.sync_api import expect


def test_google_search(page):
    # Use DuckDuckGo for a more automation-friendly search example
    page.goto("https://duckduckgo.com/")

    search = page.locator("input[name='q']")
    search.wait_for(state="visible", timeout=10000)
    search.fill("Playwright")
    search.press("Enter")

    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))
