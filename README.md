This bot’s purpose is to find and fetch all job openings in Israel within Checkpoint’s website, using Python, Selenium Webdriver, and the Pytest framework.

The file contains the following steps:
* Go to the desired URL.
* Create a list.
* Store all data (job text + individual link) inside the list.
* Move to the next page and repeat until no “Next Page” button is available.
* Print the data in a readable format using spaces and line breaks.
