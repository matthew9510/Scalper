from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import user

# Sets the browser to the Chrome Driver
PATH = "/Users/daniel/Documents/dev/Scalper/chromedriver"
driver = webdriver.Chrome(PATH)
driver.maximize_window()

RTX3070LINK = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442"
PS5LINK = "https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149"
GT1030TEST = "https://www.bestbuy.com/site/pny-nvidia-geforce-gt-1030-2gb-gddr5-pci-express-3-0-graphics-card-black/5901353.p?skuId=5901353"

# ----------------------------- Bot -----------------------------
driver.get(GT1030TEST)
isPurchased = False

while not isPurchased:
    # Searches for the add to cart button
    try:
        addToCartBtn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button"))
        )
    except:
        driver.refresh()
        continue

    # Add the item to the cart
    addToCartBtn.click()

    try:
        # Go to the cart to begin the checkout process
        driver.get("https://www.bestbuy.com/cart")

        # Click the checkout button
        checkoutBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div[2]/div[1]/div/div/span/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[1]/button"))
        )
        checkoutBtn.click()

        # Fill in user email and password
        emailInput = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "fld-e"))
        )
        emailInput.send_keys(user.email)

        passwordInput = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "fld-p1"))
        )
        passwordInput.send_keys(user.password)

        # Sign in
        signInBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[3]/button"))
        )
        signInBtn.click()

        # Fill in CVV for credit card
        cvvInput = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "credit-card-cvv"))
        )
        cvvInput.send_keys(user.cvv)

        # Place the order
        placeOrderBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".button__fast-track"))
        )
        placeOrderBtn.click()

        isPurchased = True

    except:
        # If something goes wrong, restart the bot
        driver.get(GT1030TEST)
        print("Error - Restarting")
        continue

print("The order has been placed.")
# ----------------------------- Bot -----------------------------