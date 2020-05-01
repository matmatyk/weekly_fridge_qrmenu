#!/usr/bin/env python3
"""Generates lunch menu with QR codes linking to online recipes.

Supports description on config file without recipe link, like 'my mothers
cake from family cookbook'.
"""
import calendar
import datetime
import json
import locale
import os
import shutil
import sys
import urllib.request
from urllib.parse import urlparse

import qrcode
from bs4 import BeautifulSoup

locale.setlocale(locale.LC_ALL, 'pl_PL.utf8')
START_DATE_KEY = "start_date"
MENU_KEY = "menu"
OTHERS_KEY = "others"
OUTPUT_DIR = "output"


def read_lunch_menu_from_file(path):
    """Read lunch menu from file. Accepts format described in README.md."""
    with open(path, 'r') as menu_file:
        menu_data = json.load(menu_file)
        return (menu_data[START_DATE_KEY],
                menu_data[MENU_KEY],
                menu_data[OTHERS_KEY])


def is_valid_url(url_candidate):
    """Validate whether 'url_candidate' is valid URL."""
    try:
        result = urlparse(url_candidate)
        return all([result.scheme, result.netloc, result.path])
    except ValueError:
        return False


def extract_valid_urls(data):
    """Extract url from lunch menu entries.

    Other entries can be just descriptions.
    """
    links = []
    for url_candidate in data:
        if not is_valid_url(url_candidate):
            continue
        links.append(url_candidate)
    return links


def get_title_for_url(page_url):
    """Extract page title (which usually is a dish name) from web page.

    Furthermore, strips extra info from page title (like page name).
    """
    soup = BeautifulSoup(urllib.request.urlopen(page_url), features="lxml")
    split_title = soup.title.string.split("|")
    return split_title[0].replace("przepis Olga Smile", "") \
                         .replace("przepis", "") \
                         .strip()


def date_from_string(date_str):
    """Transform date in format YYYY-MM-DD to date object."""
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("start_date in wrong format. Supported format is YYYY-MM-DD")
        return None


def date_of_first_weekday_containing(start_date):
    """Return first day of the week which contains 'start_date'."""
    while start_date.weekday() != calendar.firstweekday():
        start_date = start_date - datetime.timedelta(days=1)
    return start_date


def print_menu(start_date_str, menu_to_print, other_recipes):
    """Print given data as HTML source."""
    current_day = date_of_first_weekday_containing(
        date_from_string(start_date_str))
    result_str = """
<head>
    <link rel="stylesheet" href="resources/style.css">
</head>
<body>
    <table>
        <tr>
"""
    for weekday in calendar.Calendar(calendar.firstweekday()).iterweekdays():
        result_str += "<th>" + calendar.day_abbr[weekday] + "</th>"

    result_str += """
        </tr>
"""
    # printing weeks menu
    cnt = 0
    while True:
        if cnt % 7 == 0:
            if not menu_to_print:
                break
            result_str += """
        <tr>
            <td colspan="7">
            <h2>""" + current_day.isoformat() + " --- " + \
                (current_day + datetime.timedelta(days=6)).isoformat() + \
                """</h2>
            </td>
        </tr>
"""
        entry_desc = ""
        entry_qr = None
        if current_day in menu_to_print:
            entry_desc = menu_to_print[current_day]["title"]
            entry_qr = menu_to_print[current_day]["img"]
            menu_to_print.pop(current_day, None)
        result_str += "<td>" + entry_desc + "</br>"
        if entry_qr:
            result_str += "<img src=\"" + entry_qr + \
                          "\" alt=\"" + entry_desc + "\">"
        result_str += "</td>"

        current_day = current_day + datetime.timedelta(days=1)
        cnt = cnt + 1

    # print other recipes
    cnt = 0
    while True:
        if cnt % 7 == 0:
            if cnt >= len(other_recipes):
                break
            if other_recipes and cnt == 0:
                result_str += """
        <tr>
            <td colspan="7">
            <h2>Inne</h2>
            </td>
        </tr>
"""
        entry_desc = ""
        entry_qr = None
        if cnt < len(other_recipes):
            entry_desc = other_recipes[cnt]["title"]
            entry_qr = other_recipes[cnt]["img"]
        result_str += "<td>" + entry_desc + "</br>"
        if entry_qr:
            result_str += "<img src=\"" + entry_qr + \
                          "\" alt=\"" + entry_desc + "\">"
        result_str += "</td>"

        cnt = cnt + 1

    # footer
    result_str += """
    </table>
</body>"""
    return result_str


def do_processing(path):
    """Do all the work related to lunch menu processing. Just main function."""
    (start_date, menu, others) = read_lunch_menu_from_file(path)
    url_to_metadata = {}
    for url in extract_valid_urls(menu):
        title = get_title_for_url(url)
        img_path = os.path.join("images/", start_date + "-" +
                                title.replace(" ", "-") + ".png")
        qrcode.make(url).save(os.path.join(OUTPUT_DIR, img_path))
        url_to_metadata[url] = {
            "title": title,
            "img": img_path
        }

    others_to_print = []
    for url in extract_valid_urls(others):
        title = get_title_for_url(url)
        img_path = os.path.join("images", start_date + "-" +
                                title.replace(" ", "-") + ".png")
        qrcode.make(url).save(os.path.join(OUTPUT_DIR, img_path))
        others_to_print.append({
            "title": title,
            "img": img_path
        })

    menu_to_print = {}
    current_day = date_from_string(start_date)
    for entry in menu:
        title = entry
        img = None
        if entry in url_to_metadata:
            title = url_to_metadata[entry]["title"]
            img = url_to_metadata[entry]["img"]
        menu_to_print[current_day] = {
            "title": title,
            "img": img
        }
        current_day = current_day + datetime.timedelta(days=1)

    with open(os.path.join(OUTPUT_DIR, 'menu_' + start_date + '.html'),
              'w') as result_file:
        result_file.write(print_menu(start_date,
                                     menu_to_print,
                                     others_to_print))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Execution: {} path/to/menu.json".format(sys.argv[0]))
        sys.exit(1)
    os.makedirs(os.path.join(OUTPUT_DIR, "images"), exist_ok=True)
    os.makedirs(os.path.join(OUTPUT_DIR, "resources"), exist_ok=True)
    shutil.copytree("resources", os.path.join(OUTPUT_DIR, "resources"),
                    dirs_exist_ok=True)
    do_processing(sys.argv[1])
