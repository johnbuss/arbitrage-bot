import asyncio
from abc import ABC, abstractmethod
from playwright.async_api import async_playwright

class BaseCollector(ABC):
    @abstractmethod
    async def fetch_html(self, url: str) -> str:
        """Fetch HTML content from the given URL."""
        pass

    @abstractmethod
    async def run_collector(self):
        """Run the collector logic."""
        pass

    async def _launch_playwright(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            return browser

    async def _close_browser(self, browser):
        await browser.close()
