import random
import read_file, browser

list = read_file.read_phrases()

date = list[random.randint(0, len(list))]

browser.open_browser(date, 3, 2)