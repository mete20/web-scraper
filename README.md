# Web Scraper Project

This is a simple web scraper built in Python using the Beautiful Soup and requests libraries.
It scrapes quotes from http://quotes.toscrape.com, a website designed for scraping practice.

## Installation

This project requires Python 3.6+ and the following Python libraries installed:

*Beautiful Soup
*requests

To run the project, you will also need to have software installed to run and execute a Python script.

If you do not have Python installed yet, it is highly recommended that you install the Anaconda distribution of Python, which already has the above packages.

## Running the Script

In a terminal or command window, navigate to the top-level project directory web-scraper/ (that contains this README) and run the following command:

$python app.py

## Project Details

The script sends a GET request to the webpage, "http://quotes.toscrape.com", and receives the HTML content of the page in the response. It then creates a Beautiful Soup object from this HTML content.

It finds all the div tags with the class 'quote', each of which represents a quote. For each quote, it extracts the quote text and the author name by finding the respective tags and extracting their text. Finally, it prints out each quote and the corresponding author name.

Please note that this project is for educational purposes and should not be used for scraping websites without permission.

## License

This project is licensed under the MIT License.



