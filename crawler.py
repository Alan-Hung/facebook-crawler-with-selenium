"""Website crawler for facebook pages"""
import selenium
from selenium.webdriver.common.by import By
import selenium.webdriver.remote.webelement as web_element
import time
import datetime
import json
import helper
from typing import Union

Post = Union[str, dict, datetime.datetime]
Article = web_element.WebElement
Webdriver = selenium.webdriver.Firefox


def login(url: str, email: str, password: str) -> Webdriver:
    options = selenium.webdriver.FirefoxOptions()
    driver = selenium.webdriver.Firefox(options=options)
    driver.get(url)
    input_username = driver.find_element("id", "m_login_email")
    input_password = driver.find_element("id", "m_login_password")
    submit = driver.find_element("id", "login_password_step_element")
    input_username.send_keys(email)
    input_password.send_keys(password)
    submit.click()
    time.sleep(5)
    return driver


def processing_posts(article: Article, screenshot_path: str) -> dict[str, Post]:
    data: dict[str, Post] = {"description": article.text}

    # Find the element that contains information about the post
    data_ft = article.get_attribute("data-ft")
    if data_ft is None:
        return data
    post_data = json.loads(data_ft)
    data["data_ft"] = post_data

    # Post id
    post_id: str = post_data["mf_story_key"]
    data["post_id"] = post_id

    # Screenshot
    article.screenshot(screenshot_path + post_id + ".png")

    # Number of reaction
    footer = article.find_element(By.TAG_NAME, "footer")
    container_name = '[data-sigil="reactions-sentence-container"]'
    like_element = footer.find_element(By.CSS_SELECTOR, container_name)
    if like_element is not None:
        data["like"] = like_element.text if like_element else "0"

    # Publish_time
    if "page_insights" not in post_data:
        return data
    page_insights = post_data["page_insights"]
    for _, value in page_insights.items():
        if "post_context" in value:
            publish_time = value["post_context"]["publish_time"]
            data["publish_time"] = datetime.datetime.fromtimestamp(publish_time)

    return data


def save_posts(data: list[dict[str, Post]],
               filename: str,
               articles: list[Article],
               screenshot_path: str
               ) -> None:
    for article in articles:
        post = processing_posts(article, screenshot_path)
        data.append(post)
    helper.export_object(filename, data)


def crawl_url(driver: Webdriver,
              post_limit: int,
              target_url: str,
              screenshot_path: str,
              ) -> None:
    filename = target_url.split("/")[-1]
    data: list[dict[str, Post]] = []

    # Visit url
    driver.get(target_url)

    while len(data) < post_limit:
        # Scroll to the end of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for the page to finish loading
        time.sleep(3)

        # Retrieve posts
        articles = driver.find_elements("tag name", "article")
        save_posts(data, filename, articles, screenshot_path)
