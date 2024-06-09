"""
engeto_projekt2.py: druhý projekt do Engeto Online Testing Akademie

author: Daniel Skřivánek
email: ddaniel.skrivanek@seznam.cz
discord: vetrex89cz #3080
"""
import time
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()


def test_vysledku_stranky(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.startupjobs.cz/")

    # Ověření, že stránka byla načtena správně
    expected_title = "Práce, která vás posune vpřed | StartupJobs.cz"
    text_element = page.locator("footer p", has_text=" © 2012 – 2024 StartupJobs.com s.r.o. ")

    assert page.title() == expected_title
    assert text_element.inner_text() == "© 2012 – 2024 StartupJobs.com s.r.o."

    context.close()


def test_funkce_vyhledavani(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.startupjobs.cz/")

    # Odsouhlasení Cookies
    accept_button = page.get_by_role("button", name="Přijmout")
    accept_button.click()

    # Vyhledání prvku vyhledávacího pole a zadání vyhledávacího dotazu
    search_bar = page.wait_for_selector("div[id^='headlessui-combobox-button'][aria-expanded='false']")
    search_bar.click()

    # Čekání, až se vyhledávací pole otevře
    page.wait_for_selector("div[id^='headlessui-combobox-button'][aria-expanded='true']")

    # Vyplnění vyhledávacího pole
    search_input = page.locator("input[placeholder='Hledejte na StartupJobs...']")
    search_input.fill("Tester")

    # Odeslání formuláře
    search_input.press("Enter")

    # Čekání na výsledky vyhledávání
    results_selector = "div[class*='flex items-center justify-center']"
    page.wait_for_selector(results_selector)

    # Ověříme, že se vyhledavaný výraz nachází v URL
    assert "=Tester" in page.url, "Certain term is not located in URL"

    # Ověříme, že se výsledky vyhledávání zobrazily
    results = page.locator(results_selector)
    assert results.count() > 0, "There are no search results"

    # Ověření, že se výraz nachází ve výsledcích vyhledávání
    job_posts = page.locator("h5").filter(has_text="Tester")
    assert job_posts.count() > 0, "There is no certain search term"
    print(f"{job_posts.count()} search terms were found in the results")

    context.close()


def test_vykonu(browser):
    content = browser.new_context()
    page = content.new_page()
    start_time = time.time()
    page.goto("https://www.startupjobs.cz/")

    # Čekání na načtení důležitých prvků
    page.wait_for_selector("#front-app", timeout=10000)
    page.wait_for_selector("footer", timeout=10000)
    page.wait_for_selector("text=Firmy, ve kterých se posunete", timeout=10000)

    end_time = time.time()
    load_time = end_time - start_time

    print(f"Load time: {load_time:.2f} seconds")
    # Ověření, že načítání stránky je dokončeno do 3 sekund
    assert load_time < 3, f"Page load time is too high: {load_time:.2f} seconds"

    # Další kontrola pro načítání všech důležitých prvků
    assert page.is_visible("#front-app"), "#front-app is not visible"
    assert page.is_visible("footer"), "Footer is not visible"
    assert page.is_visible("text=Firmy, ve kterých se posunete"), "text is not visible"
