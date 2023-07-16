# Google Image downloader

Google Image Viewer is a Python application that allows you to search for images on Google using Selenium and view the search results using Tkinter.

## Prerequisites

- Python 3.x
- Selenium
- Tkinter
- Pillow
- Chrome browser
- ChromeDriver

## Installation

1. Clone the repository:

2. Install the required dependencies using pip:


3. Download ChromeDriver from the official website: [https://chromedriver.chromium.org/](https://chromedriver.chromium.org/)

4. Update the `chromedriver_path` variable in the code with the path to the ChromeDriver executable on your system.

## Usage

1. Run the program:

2. Enter the search query in the provided input field.

3. Click the "Search" button to initiate the search.

4. The program will open a new window displaying the search results as images. The window size is set to 500x500 pixels.

5. Use the scrollbar to scroll through the images if there are more images than can fit within the window.

## Customization

- You can modify the `num_images` variable in the `search_images` function to change the number of images retrieved from the search results.

- You can modify the code to customize the window size, image size, layout, and appearance according to your preferences.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The code is based on the example provided by OpenAI in their GPT-3 Playground.
- Thanks to the contributors and maintainers of the Selenium, Tkinter, and Pillow libraries.



