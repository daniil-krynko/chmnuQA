class BaseApp:
    def __init__(self, page, base_url):
        self.page = page
        self.base_url = base_url

    def go_to_site(self):
        self.page.goto(self.base_url)

    def find_element(self, locator, timeout=7000):
        return self.page.wait_for_selector(locator, timeout=timeout)