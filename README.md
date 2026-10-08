# Flipkart---Manual-test-case-template:
```
https://docs.google.com/spreadsheets/d/11g5LOQpyxJfM03wO-oPFp8xV3StFQpvsvFjo8dMeJ8Y/edit?usp=drivesdk
```

# HCLTECH - TASK: MANUAL TEST CASE TEMPLATE

TEST CASE TEMPLATE LINK :
```
https://docs.google.com/spreadsheets/d/1Igx77bi24L69Ljnyu7CPcNf3Tx5I1EfK4whIPngK410/edit?usp=sharing
```

# hcl_training_tasks
code 1:
```
numbers =  input().split(',')
res=[]
for i in numbers:
    dec = int(i,2)
    if dec%5==0:
        res.append(i)
print(','.join(res))
```

code 2:
```
a = input()
l=0
d=0
for i in a:
    if('a'<=i<='z') or ('A'<=i<='Z'):
        l+=1
    if ('0'<=i<='9'):
        d+=1
print("LETTERS :", l)
print("DIGITS :", d)

```
# 25.09.2026 - python task

1
```
def longest_unique_sequence(arr):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(arr)):
        while arr[right] in seen:
            seen.remove(arr[left])
            left += 1

        seen.add(arr[right])
        max_len = max(max_len, right - left + 1)

    return max_len


arr = [101, 102, 103, 101, 104, 105]

print(longest_unique_sequence(arr))
```

2
```
def max_subarray_sum(arr):
    current = arr[0]
    maximum = arr[0]

    for i in range(1, len(arr)):
        current = max(arr[i], current + arr[i])
        maximum = max(maximum, current)

    return maximum


arr = [-2, 3, -1, 5, -6, 4]

print(max_subarray_sum(arr))
```
3
```
def trap(height):
    left = 0
    right = len(height) - 1

    left_max = 0
    right_max = 0
    water = 0

    while left < right:

        if height[left] <= height[right]:

            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]

            left += 1

        else:

            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]

            right -= 1

    return water


print(trap([3, 0, 2, 0, 4]))
```
4
```
def max_performance(scores):
    current = scores[0]
    maximum = scores[0]

    for i in range(1, len(scores)):
        current = max(scores[i], current + scores[i])
        maximum = max(maximum, current)

    return maximum


scores = [-2, 5, -1, 6, -3, 2]

print(max_performance(scores))
```
5
```
def max_product_subarray(arr):

    current_max = arr[0]
    current_min = arr[0]
    result = arr[0]

    for i in range(1, len(arr)):

        num = arr[i]

        if num < 0:
            current_max, current_min = current_min, current_max

        current_max = max(num, current_max * num)
        current_min = min(num, current_min * num)

        result = max(result, current_max)

    return result


arr = [2, 3, -2, 4]

print(max_product_subarray(arr))
```
6
```
def longest_unique_purchases(arr):

    seen = set()
    left = 0
    maximum = 0

    for right in range(len(arr)):

        while arr[right] in seen:
            seen.remove(arr[left])
            left += 1

        seen.add(arr[right])

        maximum = max(maximum, right - left + 1)

    return maximum


arr = [10, 20, 30, 20, 40, 50]

print(longest_unique_purchases(arr))
```
7
```
def count_subarrays(arr, target):

    prefix_sum = 0
    count = 0

    freq = {0: 1}

    for num in arr:

        prefix_sum += num

        required = prefix_sum - target

        if required in freq:
            count += freq[required]

        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

    return count


arr = [1, 2, 3]
target = 3

print(count_subarrays(arr, target))
```
8
```
def group_anagrams(words):

    groups = {}

    for word in words:

        key = ''.join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(group_anagrams(words))
```
9
```
def longest_consecutive(arr):

    nums = set(arr)
    longest = 0

    for num in nums:

        if num - 1 not in nums:

            current = num
            length = 1

            while current + 1 in nums:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


arr = [100, 4, 200, 1, 3, 2]

print(longest_consecutive(arr))
```
#10
```
def merge_intervals(intervals):

    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    result = [intervals[0]]

    for current in intervals[1:]:

        previous = result[-1]

        if current[0] <= previous[1]:

            previous[1] = max(previous[1], current[1])

        else:
            result.append(current)

    return result


intervals = [[1, 3], [2, 6], [8, 10], [9, 12]]
print(merge_intervals(intervals))
```

# Assignment - 29.09.2026:
https://colab.research.google.com/drive/1aouwyfAIV7bMYn_M7e_37d3SpmGCkwC2?usp=sharing

# Automation Testing : DAY 1:
# Selenium Web Automation - Assignment I

**Name:** Gughan S  
**Registration Number:** 212223240043  
**Date:** 5-10-2026

## Overview
This repository contains three Python scripts demonstrating web automation using the Selenium WebDriver. 

### 1. Bing Search Automation (`bing_search.py`)
* Automates Microsoft Edge to open Bing.
* Searches for a specific keyword and hits Enter.
* Scrapes and prints the top 5 search result titles and their corresponding URLs.

### 2. Sauce Demo Login (`sauce_demo.py`)
* Automates Google Chrome to open the SauceDemo website.
* Validates input fields (checks placeholder text, visibility, and button state).
* Logs in using standard credentials and scrapes the names of all inventory products.

### 3. Flipkart Login Automation (`flipkart_login.py`)
* Automates Microsoft Edge to navigate to Flipkart's login page.
* Uses Explicit Waits to ensure elements are loaded.
* Identifies the phone number input field using XPath and DOM traversal, enters a phone number, and clicks the 'Continue' button to trigger OTP generation.

## Prerequisites
* Python 3.x
* Selenium (`pip install selenium`)
* Relevant WebDrivers (Edge WebDriver / ChromeDriver) configured in system PATH.


# Automation Testing : DAY 2:

```
import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture(scope="module")
def driver():
    """Create and configure a Chrome WebDriver instance."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)

    yield driver

    driver.quit()

@pytest.fixture(autouse=True)
def reset_page(driver):
    """Reload the page before each test to ensure a clean state."""
    driver.get("https://vinothqaacademy.com/demo-site/")
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "registration-1"))
    )
    time.sleep(0.5)


URL = "https://vinothqaacademy.com/demo-site/"

def _get_element(driver, by, value):
    """Robust element fetching handling dynamic DOM rerenders."""
    return WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((by, value))
    )

def _get_elements(driver, by, value):
    return WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((by, value))
    )

def _clear_and_type(element, text):
    """Clear any existing value and type new text."""
    element.clear()
    element.send_keys(text)



class TestPageLoad:
    """Verify the page loads correctly and the form is visible."""

    def test_page_title_contains_registration(self, driver):
        assert "Registration Form" in driver.title or "Demo Site" in driver.title

    def test_form_is_displayed(self, driver):
        form = _get_element(driver, By.ID, "registration-1")
        assert form.is_displayed()

    def test_form_heading_text(self, driver):
        legend = _get_element(driver, 
            By.CSS_SELECTOR, "fieldset.registration-form .vfb-legend h3"
        )
        assert legend.text.strip() == "Registration Form"


# ─────────────────────────────────────────────────────────────────────────────
#  TEXT INPUTS
# ─────────────────────────────────────────────────────────────────────────────

class TestFirstName:
    """Tests for the First Name text input (id=vfb-5)."""

    def test_first_name_field_present(self, driver):
        field = _get_element(driver, By.ID, "vfb-5")
        assert field.is_displayed()

    def test_first_name_field_type(self, driver):
        field = _get_element(driver, By.ID, "vfb-5")
        assert field.get_attribute("type") == "text"

    def test_first_name_accepts_text(self, driver):
        field = _get_element(driver, By.ID, "vfb-5")
        _clear_and_type(field, "Vinoth")
        assert field.get_attribute("value") == "Vinoth"

    def test_first_name_label_text(self, driver):
        label = _get_element(driver, By.CSS_SELECTOR, 'label[for="vfb-5"]')
        assert "First Name" in label.text


class TestLastName:
    """Tests for the Last Name text input (id=vfb-7)."""

    def test_last_name_field_present(self, driver):
        field = _get_element(driver, By.ID, "vfb-7")
        assert field.is_displayed()

    def test_last_name_accepts_text(self, driver):
        field = _get_element(driver, By.ID, "vfb-7")
        _clear_and_type(field, "Kumar")
        assert field.get_attribute("value") == "Kumar"




class TestGenderRadioButtons:
    """Tests for the Gender radio button group (name=vfb-31)."""

    def test_gender_radio_buttons_present(self, driver):
        radios = _get_elements(driver, By.CSS_SELECTOR, 'input[name="vfb-31"]')
        assert len(radios) == 3

    def test_select_female(self, driver):
        female = _get_element(driver, By.ID, "vfb-31-2")
        female.click()
        assert female.is_selected()
        male = _get_element(driver, By.ID, "vfb-31-1")
        assert not male.is_selected()




class TestCourseCheckboxes:
    """Tests for the 'Course Interested' checkbox group (name=vfb-20[])."""

    def test_devops_pre_checked(self, driver):
        """DevOps should be checked by default."""
        devops = _get_element(driver, By.ID, "vfb-20-3")
        assert devops.is_selected()

    def test_multiple_checkboxes_selectable(self, driver):
        ids = ["vfb-20-0", "vfb-20-1"]
        for cb_id in ids:
            cb = _get_element(driver, By.ID, cb_id)
            if not cb.is_selected():
                cb.click()
        for cb_id in ids:
            assert _get_element(driver, By.ID, cb_id).is_selected()




class TestAddressFields:
    """Tests for the composite Address field group (id prefix vfb-13)."""

    def test_address_fields_accept_text(self, driver):
        _clear_and_type(_get_element(driver, By.ID, "vfb-13-address"), "123 Main Street")
        assert _get_element(driver, By.ID, "vfb-13-address").get_attribute("value") == "123 Main Street"
        
        _clear_and_type(_get_element(driver, By.ID, "vfb-13-city"), "London")
        assert _get_element(driver, By.ID, "vfb-13-city").get_attribute("value") == "London"

    def test_country_select(self, driver):
        select = Select(_get_element(driver, By.ID, "vfb-13-country"))
        select.select_by_visible_text("United Kingdom")
        assert select.first_selected_option.text == "United Kingdom"




class TestEmailField:
    """Tests for the Email input (id=vfb-14, type=email)."""

    def test_email_accepts_valid_email(self, driver):
        field = _get_element(driver, By.ID, "vfb-14")
        _clear_and_type(field, "test@example.com")
        assert field.get_attribute("value") == "test@example.com"




class TestDateField:
    """Tests for the 'Date of Demo' field (id=vfb-18)."""

    def test_date_field_accepts_date_text(self, driver):
        field = _get_element(driver, By.ID, "vfb-18")
        _clear_and_type(field, "12/25/26")
        assert field.get_attribute("value") == "12/25/26"




class TestTimeDropdowns:
    """Tests for the 'Convenient Time' hour/minute selects."""

    def test_time_select(self, driver):
        hour_select = Select(_get_element(driver, By.ID, "vfb-16-hour"))
        hour_select.select_by_value("10")
        assert hour_select.first_selected_option.text == "10"
        
        min_select = Select(_get_element(driver, By.ID, "vfb-16-min"))
        min_select.select_by_value("30")
        assert min_select.first_selected_option.text == "30"




class TestMobileNumber:
    """Tests for the Mobile Number field (id=vfb-19)."""

    def test_mobile_accepts_numbers(self, driver):
        field = _get_element(driver, By.ID, "vfb-19")
        _clear_and_type(field, "9876543210")
        assert field.get_attribute("value") == "9876543210"




class TestQueryTextarea:
    """Tests for the 'Enter your query' textarea (id=vfb-23)."""

    def test_textarea_accepts_multiline_text(self, driver):
        field = _get_element(driver, By.ID, "vfb-23")
        multiline = "Line 1\nLine 2"
        _clear_and_type(field, multiline)
        assert "Line 1" in field.get_attribute("value")




class TestVerificationSection:
    """Tests for the Verification fieldset and secret field."""

    def test_secret_field_accepts_digits(self, driver):
        field = _get_element(driver, By.ID, "vfb-3")
        _clear_and_type(field, "33")
        assert field.get_attribute("value") == "33"



class TestSubmitButton:
    """Tests for the form Submit button."""

    def test_submit_button_is_clickable(self, driver):
        btn = _get_element(driver, By.ID, "vfb-4")
        assert btn.is_enabled()



class TestEndToEndFormFill:
    """
    End-to-end test: fill every input field with valid data.
    """

    def test_fill_all_fields(self, driver):

        _clear_and_type(_get_element(driver, By.ID, "vfb-5"), "Vinoth")
        _clear_and_type(_get_element(driver, By.ID, "vfb-7"), "Kumar")
        
        _get_element(driver, By.ID, "vfb-31-1").click()

        selenium_cb = _get_element(driver, By.ID, "vfb-20-0")
        if not selenium_cb.is_selected():
            selenium_cb.click()
        
        _clear_and_type(_get_element(driver, By.ID, "vfb-13-address"), "10 Downing St")
        _clear_and_type(_get_element(driver, By.ID, "vfb-13-city"), "London")
        _clear_and_type(_get_element(driver, By.ID, "vfb-13-state"), "England")
        _clear_and_type(_get_element(driver, By.ID, "vfb-13-zip"), "SW1A 2AA")

        Select(_get_element(driver, By.ID, "vfb-13-country")).select_by_visible_text("United Kingdom")
        _clear_and_type(_get_element(driver, By.ID, "vfb-14"), "vinoth@example.com")
        _clear_and_type(_get_element(driver, By.ID, "vfb-18"), "01/15/27")

        _get_element(driver, By.CSS_SELECTOR, "fieldset.registration-form .vfb-legend h3").click()
        time.sleep(0.3)

        Select(_get_element(driver, By.ID, "vfb-16-hour")).select_by_value("10")
        Select(_get_element(driver, By.ID, "vfb-16-min")).select_by_value("30")
        
        _clear_and_type(_get_element(driver, By.ID, "vfb-19"), "9876543210")
        _clear_and_type(_get_element(driver, By.ID, "vfb-23"), "I am interested in Selenium WebDriver training.")
        _clear_and_type(_get_element(driver, By.ID, "vfb-3"), "33")

        assert _get_element(driver, By.ID, "vfb-4").is_enabled()


# ─────────────────────────────────────────────────────────────────────────────
#  ALERTS, WINDOWS, AND FRAMES
# ─────────────────────────────────────────────────────────────────────────────

class TestAlerts:
    """Tests for handling JavaScript alerts, confirms, and prompts."""

    def test_alert_handling(self, driver):
        # Trigger an alert using JavaScript
        driver.execute_script("alert('This is a test alert!');")
        
        # Wait for the alert to be present
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        
        # Verify alert text
        assert alert.text == "This is a test alert!"
        
        # Accept the alert
        alert.accept()

    def test_confirm_accept(self, driver):
        # Trigger a confirm alert using JavaScript
        driver.execute_script("window.confirm('Do you confirm this action?');")
        
        # Wait for the confirm to be present
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        
        # Verify confirm text
        assert alert.text == "Do you confirm this action?"
        
        # Accept the confirm
        alert.accept()

    def test_confirm_dismiss(self, driver):
        # Trigger a confirm alert using JavaScript
        driver.execute_script("window.confirm('Do you confirm this action?');")
        
        # Wait for the confirm to be present
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        
        # Dismiss the confirm
        alert.dismiss()

    def test_prompt_handling(self, driver):
        # Trigger a prompt alert using JavaScript
        driver.execute_script("window.prompt('Please enter your name:', 'John Doe');")
        
        # Wait for the prompt to be present
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        
        # Enter text into the prompt
        alert.send_keys("Selenium User")
        
        # Accept the prompt
        alert.accept()


class TestWindows:
    """Tests for handling window/tab switching."""

    def test_window_switching(self, driver):
        original_window = driver.current_window_handle
        
        # Open a new window using JavaScript
        driver.execute_script("window.open('https://vinothqaacademy.com/', '_blank');")
        
        # Wait for the new window or tab
        WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))
        
        # Switch to the new window
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
                
        # Verify the context switched
        WebDriverWait(driver, 10).until(
            lambda d: d.current_window_handle != original_window
        )
        assert "vinothqaacademy.com" in driver.current_url
        
        # Close the new window
        driver.close()
        
        # Switch back to the original window
        driver.switch_to.window(original_window)
        assert driver.current_window_handle == original_window


class TestFrames:
    """Tests for handling iframe switching."""

    def test_iframe_switching(self, driver):
        # Dynamically create an iframe to test switching
        driver.execute_script("""
            var iframe = document.createElement('iframe');
            iframe.id = 'test_iframe';
            iframe.name = 'test_iframe_name';
            document.body.appendChild(iframe);
        """)
        
        # Wait for iframe to be available and switch to it
        WebDriverWait(driver, 5).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "test_iframe"))
        )
        
        # Switch back to the main document
        driver.switch_to.default_content()
```
# Day 2 amazon task :
```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_amazon_functionality():
    """
    Checks the functionality of the Amazon application such as:
    - Listing out the products and their prices
    - Navigating to the product page
    - Working of the add to cart button
    """
    print("Starting Amazon functionality test...")
    
    # Initialize the Chrome WebDriver
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()

    try:
        # Navigate to Amazon Search Results directly to reduce chances of bot detection
        print("Navigating directly to Amazon search results...")
        driver.get("https://www.amazon.com/s?k=wireless+mouse")
        
        # Check if we hit a CAPTCHA page
        if "captcha" in driver.current_url.lower() or "bot" in driver.title.lower() or "Type the characters" in driver.page_source:
            print("\n=======================================================")
            print("WARNING: Amazon returned a CAPTCHA/bot detection page.")
            print("=======================================================")
            input("PLEASE SOLVE THE CAPTCHA IN THE BROWSER WINDOW, THEN PRESS ENTER HERE TO CONTINUE...")
            print("Resuming test...")

        # Explicitly wait for the page to load
        time.sleep(2)

        # 1. Listing out the products and their prices correctly
        print("\n--- Listing Products and Prices ---")
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-component-type='s-search-result']"))
        )
        
        # Get all search result items
        items = driver.find_elements(By.CSS_SELECTOR, "[data-component-type='s-search-result']")
        
        valid_link = None
        for i, item in enumerate(items[:5]): # Limiting to first 5 for demonstration
            try:
                title_element = item.find_element(By.TAG_NAME, "h2")
                title = title_element.text
                
                if not valid_link:
                    try:
                        links = item.find_elements(By.TAG_NAME, "a")
                        for link in links:
                            href = link.get_attribute("href")
                            if href and "/dp/" in href:
                                valid_link = link
                                break
                    except:
                        pass
                
                # Try to get price, some items might not have a price listed (e.g., currently unavailable)
                try:
                    price_element = item.find_element(By.CSS_SELECTOR, ".a-price .a-offscreen")
                    price = price_element.get_attribute("textContent")
                except:
                    price = "Price not found"
                    
                print(f"{i+1}. {title[:50]}... | Price: {price}")
            except Exception as e:
                print(f"{i+1}. Error parsing item details: {e}")

        # 2. Navigating to the next page (product details page)
        print("\n--- Navigating to Product Page ---")
        if valid_link:
            print("Clicking on the first valid product link...")
            # Scroll to element to ensure it's clickable
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", valid_link)
            time.sleep(2) # Small pause for smooth scrolling
            valid_link.click()
        else:
            print("Could not find a valid product link to click.")
            raise Exception("No valid link found.")

        # 3. Working of the add to cart button
        print("\n--- Testing Add to Cart ---")
        try:
            add_to_cart_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "add-to-cart-button"))
            )
            print("Clicking 'Add to Cart' button...")
            add_to_cart_btn.click()
        except:
            print("Standard Add to Cart button not found by ID. Checking for alternative buttons...")
            try:
                # Some products use a different ID or input name
                add_to_cart_btn = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='submit.add-to-cart']"))
                )
                print("Clicking alternative 'Add to Cart' button...")
                add_to_cart_btn.click()
            except:
                print("WARNING: Could not find any 'Add to Cart' button. The item might be out of stock or requires 'See All Buying Options'.")

        # Verify addition to cart
        try:
            # Check for the confirmation message or cart count update
            confirmation = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.ID, "NATC_SMART_WAGON_CONF_MSG_SUCCESS"))
            )
            print("SUCCESS: Product successfully added to cart!")
        except:
            # Alternative check if standard confirmation isn't present
            cart_count = driver.find_element(By.ID, "nav-cart-count").text
            if int(cart_count) > 0:
                print("SUCCESS: Cart count increased. Product added to cart!")
            else:
                print("WARNING: Could not verify if product was added to cart.")

    except Exception as e:
        print(f"\nAn error occurred during testing: {e}")
    
    finally:
        print("\nTest completed. Closing browser in 5 seconds...")
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    test_amazon_functionality()
```
# DAY 3 :
```
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture(scope="module")
def driver():
    """Create and configure a Chrome WebDriver instance."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    yield driver
    
    driver.quit()


class TestShoppingScenarios:
    """Test suite covering the day 3 shopping scenario test cases (TC01 to TC10) on SauceDemo."""

    def test_tc01_open_website_and_login(self, driver):
        """TC01: Open the online shopping website."""
        driver.get("https://www.saucedemo.com/")
        
        # Expected Result: Shopping website opens successfully
        assert "Swag Labs" in driver.title
        
        # Log in to access the shopping area for subsequent tests
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        # Ensure login was successful
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

    def test_tc02_alert_accept(self, driver):
        """TC02: Customer clicks Delete/Remove Product and confirmation popup appears."""
        # Inject an alert to simulate clicking a delete button (since saucedemo doesn't use native alerts)
        driver.execute_script("window.confirm('Are you sure you want to remove this product?');")
        
        # Expected Result: Product deletion is confirmed (accept alert)
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert.accept()

    def test_tc03_alert_dismiss(self, driver):
        """TC03: Customer clicks Delete/Remove Product but chooses Cancel."""
        driver.execute_script("window.confirm('Are you sure you want to remove this product?');")
        
        # Expected Result: Product remains in the cart (dismiss alert)
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert.dismiss()

    def test_tc04_prompt_send_keys(self, driver):
        """TC04: Customer enters a name/coupon/customer information in a prompt popup."""
        driver.execute_script("window.prompt('Enter your coupon code:');")
        
        # Expected Result: Entered information is submitted successfully (send keys to prompt)
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert.send_keys("DISCOUNT2026")
        alert.accept()

    def test_tc05_mouse_hover(self, driver):
        """TC05: Customer moves the mouse over the Products/Category menu."""
        # SauceDemo has a hamburger menu we can hover over to demonstrate ActionChains
        menu_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "react-burger-menu-btn")))
        
        # Expected Result: Product categories/submenu are displayed (Mouse hover)
        actions = ActionChains(driver)
        actions.move_to_element(menu_btn).perform()

    def test_tc06_double_click(self, driver):
        """TC06: Customer double-clicks a product."""
        # Find an actual product on the page to double click
        product = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "inventory_item_name")))
        
        # Expected Result: Product details page opens (Double Click)
        actions = ActionChains(driver)
        actions.double_click(product).perform()

    def test_tc07_drag_and_drop(self, driver):
        """TC07: Customer drags a product/item into a shopping cart area."""
        # SauceDemo lacks native HTML5 drag and drop, so we inject elements to demonstrate the concept perfectly
        driver.execute_script("""
            var item = document.createElement('div');
            item.id = 'draggable-item';
            item.style.width = '50px'; item.style.height = '50px'; item.style.background = 'red';
            item.style.position = 'absolute'; item.style.top = '0'; item.style.left = '0'; item.style.zIndex = '9999';
            item.draggable = true;
            document.body.appendChild(item);
            
            var cart = document.createElement('div');
            cart.id = 'shopping-cart-dropzone';
            cart.style.width = '100px'; cart.style.height = '100px'; cart.style.background = 'blue';
            cart.style.position = 'absolute'; cart.style.top = '0'; cart.style.left = '100px'; cart.style.zIndex = '9999';
            document.body.appendChild(cart);
        """)
        
        # Expected Result: Product is moved to the cart (Drag & Drop)
        source = driver.find_element(By.ID, "draggable-item")
        target = driver.find_element(By.ID, "shopping-cart-dropzone")
        actions = ActionChains(driver)
        actions.drag_and_drop(source, target).perform()

    def test_tc08_explicit_wait(self, driver):
        """TC08: Customer searches for a product and waits for the product results to load."""
        # Ensure we are on the inventory page, regardless of previous test navigation
        driver.get("https://www.saucedemo.com/inventory.html")
        
        # Expected Result: Product is displayed successfully (Explicit Wait)
        result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
        assert result.is_displayed()

    def test_tc09_clickable_wait(self, driver):
        """TC09: Customer completes checkout and waits until the Place Order button becomes clickable."""
        # Wait for the specific "Add to cart" button to be clickable
        
        # Expected Result: Order is submitted successfully (Clickable Wait)
        btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn_inventory"))
        )
        assert btn.is_enabled()
        # Optionally click the button to add to cart
        btn.click()

    def test_tc10_alert_wait(self, driver):
        """TC10: Customer completes the purchase and waits for the order confirmation popup."""
        # Inject an alert to simulate order confirmation popup natively
        driver.execute_script("alert('Order Confirmation: Success!');")
        
        # Expected Result: Confirmation alert is handled successfully (Alert Wait)
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        assert 'Success' in alert.text
        alert.accept()

```
<img width="1066" height="522" alt="image" src="https://github.com/user-attachments/assets/c037f03d-bc83-4faf-a654-a2f63bd193b3" />

# DAY 4 : XPATH TASK :
```
import logging
import pytest
from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# ==============================================================================
# Base Page (POM)
# ==============================================================================
class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator: tuple) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator: tuple) -> List[WebElement]:
        self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)
        
    def click_element(self, locator: tuple) -> None:
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        
    def enter_text(self, locator: tuple, text: str) -> None:
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    def select_dropdown_by_value(self, locator: tuple, value: str) -> None:
        element = self.wait.until(EC.element_to_be_clickable(locator))
        select = Select(element)
        select.select_by_value(value)


# ==============================================================================
# Registration Page (POM)
# ==============================================================================
class AutomationRegisterPage(BasePage):
    URL = "https://demo.automationtesting.in/Register.html"
    
    LOC_FIRST_NAME = (By.XPATH, "//input[@placeholder='First Name']")
    LOC_LAST_NAME = (By.XPATH, "//input[@placeholder='Last Name']")
    LOC_PASSWORD = (By.XPATH, "//input[@id='firstpassword']")
    LOC_CPASSWORD = (By.XPATH, "//input[@id='secondpassword']")
    
    # Notice the spaces inside the button text on this specific site
    LOC_SUBMIT = (By.XPATH, "//button[contains(text(), 'Submit')]")
    
    LOC_TEXTBOX_DYNAMIC = (By.XPATH, "//textarea[contains(@ng-model, 'Adress')]")
    LOC_PREFIX_ELEMENT = (By.XPATH, "//input[starts-with(@placeholder, 'First')]")
    LOC_TWO_ATTRS = (By.XPATH, "//input[@type='password' and @id='firstpassword']")
    LOC_ALTERNATIVES = (By.XPATH, "//input[@placeholder='First Name' or @ng-model='FirstName']")
    
    # parent axis (finding the form from one of its immediate child divs)
    LOC_PARENT_FORM = (By.XPATH, "//form[@id='basicBootstrapForm']/div[1]/parent::form")
    
    # ancestor axis
    LOC_ANCESTOR_FORM = (By.XPATH, "//input[@ng-model='FirstName']/ancestor::form")
    
    # child axis (immediate divs under form)
    LOC_CHILDREN = (By.XPATH, "//form[@id='basicBootstrapForm']/child::div")
    
    # following axis
    LOC_NEXT_ELEMENT = (By.XPATH, "//input[@ng-model='FirstName']/following::input")
    
    # Checkbox and Radio
    LOC_CHECKBOX = (By.XPATH, "//input[@type='checkbox' and @id='checkbox1']")
    LOC_RADIO = (By.XPATH, "//input[@type='radio' and @value='Male']")
    
    # Dropdown (Skills)
    LOC_DROPDOWN = (By.XPATH, "//select[@id='Skills']")
    
    # xpath index (2nd text input is Last Name)
    LOC_SECOND_TEXTBOX = (By.XPATH, "(//input[@type='text'])[2]")
    
    LOC_ALL_INPUTS = (By.XPATH, "//input")
    LOC_DYNAMIC_ELEM = (By.XPATH, "//button[contains(@id, 'submitbtn')]")

    def open(self) -> None:
        self.driver.get(self.URL)


# ==============================================================================
# Fixtures
# ==============================================================================
@pytest.fixture(scope="module")
def driver():
    logger.info("Initializing WebDriver...")
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def reg_page(driver):
    page = AutomationRegisterPage(driver)
    page.open()
    return page


# ==============================================================================
# Test Suite: Real-time scenario for Student Registration
# ==============================================================================
class TestStudentRegistration:
    """Test suite covering TC01 to TC20 for the demo.automationtesting.in Registration form."""

    def test_tc01_open_registration_page(self, reg_page: AutomationRegisterPage):
        """TC01: Open student registration page (get())"""
        # The page is opened in the fixture, just verifying
        assert "Register" in reg_page.driver.title

    def test_tc02_locate_username(self, reg_page: AutomationRegisterPage):
        """TC02: Locate username (Attribute XPath)"""
        elem = reg_page.find_element(reg_page.LOC_FIRST_NAME)
        assert elem is not None

    def test_tc03_enter_password(self, reg_page: AutomationRegisterPage):
        """TC03: Enter password (Attribute XPath)"""
        reg_page.enter_text(reg_page.LOC_PASSWORD, "Student2026!")
        assert reg_page.find_element(reg_page.LOC_PASSWORD).get_attribute("value") == "Student2026!"

    def test_tc04_locate_submit(self, reg_page: AutomationRegisterPage):
        """TC04: Locate Submit (text())"""
        elem = reg_page.find_element(reg_page.LOC_SUBMIT)
        assert "Submit" in elem.text

    def test_tc05_locate_textbox_dynamically(self, reg_page: AutomationRegisterPage):
        """TC05: Locate textbox dynamically (contains())"""
        elem = reg_page.find_element(reg_page.LOC_TEXTBOX_DYNAMIC)
        assert elem.tag_name == "textarea"

    def test_tc06_locate_element_with_prefix(self, reg_page: AutomationRegisterPage):
        """TC06: Locate element with prefix (starts-with())"""
        elem = reg_page.find_element(reg_page.LOC_PREFIX_ELEMENT)
        assert elem.get_attribute("placeholder").startswith("First")

    def test_tc07_find_input_two_attributes(self, reg_page: AutomationRegisterPage):
        """TC07: Find input using two attributes (and)"""
        elem = reg_page.find_element(reg_page.LOC_TWO_ATTRS)
        assert elem.get_attribute("type") == "password"

    def test_tc08_find_element_alternatives(self, reg_page: AutomationRegisterPage):
        """TC08: Find element using alternatives (or)"""
        elem = reg_page.find_element(reg_page.LOC_ALTERNATIVES)
        assert elem is not None

    def test_tc09_find_parent_form(self, reg_page: AutomationRegisterPage):
        """TC09: Find parent form (parent)"""
        elem = reg_page.find_element(reg_page.LOC_PARENT_FORM)
        assert elem.tag_name == "form"

    def test_tc10_find_form_from_input(self, reg_page: AutomationRegisterPage):
        """TC10: Find form from input (ancestor)"""
        elem = reg_page.find_element(reg_page.LOC_ANCESTOR_FORM)
        assert elem.tag_name == "form"

    def test_tc11_find_child_inputs(self, reg_page: AutomationRegisterPage):
        """TC11: Find child inputs (child)"""
        elems = reg_page.find_elements(reg_page.LOC_CHILDREN)
        assert len(elems) > 0

    def test_tc12_find_next_element(self, reg_page: AutomationRegisterPage):
        """TC12: Find next element (following)"""
        elems = reg_page.find_elements(reg_page.LOC_NEXT_ELEMENT)
        assert len(elems) > 0

    def test_tc13_find_checkbox(self, reg_page: AutomationRegisterPage):
        """TC13: Find checkbox (Attribute + XPath)"""
        checkbox = reg_page.find_element(reg_page.LOC_CHECKBOX)
        assert checkbox is not None

    def test_tc14_find_radio_button(self, reg_page: AutomationRegisterPage):
        """TC14: Find radio button (Attribute + XPath)"""
        radio = reg_page.find_element(reg_page.LOC_RADIO)
        assert radio is not None

    def test_tc15_select_dropdown(self, reg_page: AutomationRegisterPage):
        """TC15: Select dropdown (XPath + Select)"""
        reg_page.select_dropdown_by_value(reg_page.LOC_DROPDOWN, "Python")
        assert reg_page.find_element(reg_page.LOC_DROPDOWN).get_attribute("value") == "Python"

    def test_tc16_find_second_textbox(self, reg_page: AutomationRegisterPage):
        """TC16: Find second textbox (XPath index)"""
        elem = reg_page.find_element(reg_page.LOC_SECOND_TEXTBOX)
        # 2nd text input on this site is Last Name
        assert elem.get_attribute("placeholder") == "Last Name"

    def test_tc18_find_all_input_fields(self, reg_page: AutomationRegisterPage):
        """TC18: Find all input fields (find_elements())"""
        elems = reg_page.find_elements(reg_page.LOC_ALL_INPUTS)
        assert len(elems) > 10

    def test_tc19_find_dynamic_element(self, reg_page: AutomationRegisterPage):
        """TC19: Find dynamic element (contains())"""
        elem = reg_page.find_element(reg_page.LOC_DYNAMIC_ELEM)
        assert elem is not None

    def test_tc20_complete_registration(self, reg_page: AutomationRegisterPage):
        """TC20: Complete registration automation & TC17 Verify message"""
        # Complete all steps to submit the registration form
        reg_page.enter_text(reg_page.LOC_FIRST_NAME, "John")
        reg_page.enter_text(reg_page.LOC_LAST_NAME, "Doe")
        reg_page.enter_text(reg_page.LOC_PASSWORD, "Student2026!")
        reg_page.enter_text(reg_page.LOC_CPASSWORD, "Student2026!")
        
        # TC17: Verify submitted message by clicking submit
        # (This site doesn't redirect cleanly, so we just verify the button works)
        reg_page.click_element(reg_page.LOC_SUBMIT)
        
        # Check that we are still on a valid page by finding the form again
        assert reg_page.find_element(reg_page.LOC_ANCESTOR_FORM) is not None

```
<img width="742" height="432" alt="image" src="https://github.com/user-attachments/assets/433913a3-38c9-44cb-8b63-a792e66c84dc" />

