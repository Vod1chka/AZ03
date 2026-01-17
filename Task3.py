from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import matplotlib.pyplot as plt
import re
import time

driver = webdriver.Chrome()

driver.get("https://www.divan.ru/category/divany")
time.sleep(3)

price_elements = driver.find_elements(By.CSS_SELECTOR, "span[class*='FullPrice_actual']")

prices = []
for elem in price_elements:
    text = elem.text
    number = re.sub(r"[^\d]", "", text)
    if number:
        prices.append(int(number))

driver.quit()

df = pd.DataFrame(prices, columns=["price"])
df.to_csv("divan_prices.csv", index=False)

average_price = df["price"].mean()
print(f"Средняя цена дивана: {average_price:.2f} руб.")

plt.figure()
plt.hist(df["price"], bins=20)
plt.title("Гистограмма цен на диваны")
plt.xlabel("Цена (руб.)")
plt.ylabel("Количество")
plt.show()