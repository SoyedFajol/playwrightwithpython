from playwright.sync_api import sync_playwright
import traceback

def main():
    try:
        with sync_playwright() as p:
            # run with headless=False to see the browser window while debugging
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto("https://www.google.com", wait_until="load")
            print("Page title:", page.title())
            browser.close()
    except Exception as e:
        print("Error running script:")
        traceback.print_exc()

if __name__ == "__main__":
    main()