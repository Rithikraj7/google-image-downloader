from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *
from PIL import ImageTk, Image
import urllib.request
import os


def search_images():
    search_query = entry.get()
    num_images = 5

    # Set up Selenium
    chromedriver_path = "D:/nmiit project/python/chromedriver.exe"  # Update this with the path to the Chrome driver executable
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chrome in headless mode (without opening a window)
    options.add_argument(f'--webdriver.chrome.driver={chromedriver_path}')
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.google.com/imghp')

    # Find the search bar and enter the search query
    wait = WebDriverWait(driver, 10)
    search_bar = wait.until(EC.presence_of_element_located((By.NAME, 'q')))
    search_bar.send_keys(search_query)
    search_bar.submit()

    # Find the image results and extract the image URLs
    image_urls = set()
    while len(image_urls) < num_images:
        images = driver.find_elements(By.CSS_SELECTOR, 'img.rg_i')
        for image in images:
            try:
                image_urls.add(image.get_attribute('src'))
            except Exception as e:
                print(f"Error: {e}")

        # Scroll down to load more images
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Close the browser
    driver.quit()

    # Create a new window for image display
    image_window = Toplevel()
    image_window.title("Image Viewer")
    image_window.geometry("500x500")
    image_window.resizable(False, False)

    # Create a frame with a scrollbar
    frame = Frame(image_window)
    frame.pack(fill=BOTH, expand=True)

    canvas = Canvas(frame)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    inner_frame = Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    row_num = 0
    col_num = 0

    for i, url in enumerate(image_urls):
        # Download the image
        try:
            image_path = f'image{i+1}.jpg'
            urllib.request.urlretrieve(url, image_path)
        except Exception as e:
            print(f"Error downloading image: {e}")
            continue

        # Open and resize the image
        image = Image.open(image_path)
        image.thumbnail((100, 100))  # Resizes the image to fit within 100x100 while maintaining aspect ratio
        photo = ImageTk.PhotoImage(image)

        # Create a label for the image
        label = Label(inner_frame, image=photo)
        label.image = photo
        label.grid(row=row_num, column=col_num, padx=5, pady=5)
        label.configure(bg='black')

        col_num += 1
        if col_num == 4:  # Display 4 images per row
            col_num = 0
            row_num += 1

    # Delete the downloaded images
    for i in range(1, num_images + 1):
        image_path = f'image{i}.jpg'
        if os.path.exists(image_path):
            os.remove(image_path)

    # Run the Tkinter event loop
    image_window.mainloop()

# Create the main Tkinter window
window = Tk()
window.title("Image Viewer")
heading_label = Label(window, text="Image Viewer", font=("Helvetica", 20, "bold"), pady=20, bg='#abb8c3')
heading_label.pack()

image_path = "D:/nmiit project/python/google.png"
image = Image.open(image_path)
resized_image = image.resize((300, 205), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized_image)
image_label = Label(window, image=photo)
image_label.pack()

# Create the search input field and label
search_label = Label(window, text="Search query:")
search_label.pack()
entry = Entry(window)
entry.pack()

# Create the search button
search_button = Button(window, text="Search", command=search_images)
search_button.pack()

# window resizable and coloring
window.resizable(False, False)
window.geometry("400x600")
window.configure(bg='#abb8c3')
# Run the Tkinter event loop
window.mainloop()

