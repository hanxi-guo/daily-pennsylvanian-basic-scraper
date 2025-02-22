"""
Scrapes a headline from The Daily Pennsylvanian website and saves it to a 
JSON file that tracks headlines over time.
"""

import os
import sys

import daily_event_monitor

import bs4
import requests
import loguru


def scrape_data_point():
    """
    Scrapes the main headline from The Daily Pennsylvanian home page.

    Returns:
        str: The headline text if found, otherwise an empty string.
    """
    headers = {
        "User-Agent": "cis3500-scraper"
    }
    req = requests.get("https://www.thedp.com", headers=headers)
    loguru.logger.info(f"Request URL: {req.url}")
    loguru.logger.info(f"Request status code: {req.status_code}")

    if req.ok:
        soup = bs4.BeautifulSoup(req.text, "html.parser")
        target_element = soup.find("a", class_="frontpage-link")
        data_point = "" if target_element is None else target_element.text
        data_point_link = target_element.get("href", "") if target_element else ""
        loguru.logger.info(f"Data point: {data_point} \n  Link: {data_point_link}")

        most_recent = ""

        most_recent_section = soup.find("div", class_="top-story-sidebar")

        most_recent_article = most_recent_section.find("a", class_="frontpage-link small-link") if most_recent_section else None

        if most_recent_article:
            most_recent = "" if most_recent_article is None else most_recent_article.text
            most_recent_link = most_recent_article.get("href", "") if most_recent_article else ""
            loguru.logger.info (f"Most Recent Article: {most_recent} \n  Link: {most_recent_link}")
        else:
            print("Most Recent article not found.")
    else:
        print("Failed to load the page.")

    return data_point, data_point_link, most_recent, most_recent_link


if __name__ == "__main__":

    # Setup logger to track runtime
    loguru.logger.add("scrape.log", rotation="1 day")

    # Create data dir if needed
    loguru.logger.info("Creating data directory if it does not exist")
    try:
        os.makedirs("data", exist_ok=True)
    except Exception as e:
        loguru.logger.error(f"Failed to create data directory: {e}")
        sys.exit(1)

    # Load daily event monitor
    loguru.logger.info("Loading daily event monitor")
    dem = daily_event_monitor.DailyEventMonitor(
        "data/daily_pennsylvanian_headlines.json"
    )

    # Run scrape
    loguru.logger.info("Starting scrape")
    try:
        data_point, data_point_link, most_recent, most_recent_link  = scrape_data_point()
    except Exception as e:
        loguru.logger.error(f"Failed to scrape data point: {e}")
        data_point = None
        most_recent = None 
        data_point_link = None
        most_recent_link = None

    # Save data
    if data_point is not None:
        dem.add_today(value = data_point, link = data_point_link, event_type="main_headline")
        
    if most_recent is not None:
        dem.add_today(value = most_recent, link = most_recent_link, event_type="most_recent")
        dem.save()
        loguru.logger.info("Saved daily event monitor")

    def print_tree(directory, ignore_dirs=[".git", "__pycache__"]):
        loguru.logger.info(f"Printing tree of files/dirs at {directory}")
        for root, dirs, files in os.walk(directory):
            dirs[:] = [d for d in dirs if d not in ignore_dirs]
            level = root.replace(directory, "").count(os.sep)
            indent = " " * 4 * (level)
            loguru.logger.info(f"{indent}+--{os.path.basename(root)}/")
            sub_indent = " " * 4 * (level + 1)
            for file in files:
                loguru.logger.info(f"{sub_indent}+--{file}")

    print_tree(os.getcwd())

    loguru.logger.info("Printing contents of data file {}".format(dem.file_path))
    with open(dem.file_path, "r") as f:
        loguru.logger.info(f.read())

    # Finish
    loguru.logger.info("Scrape complete")
    loguru.logger.info("Exiting")
