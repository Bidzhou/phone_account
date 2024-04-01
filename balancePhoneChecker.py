from selenium import webdriver
from selenium.webdriver.common.by import By
import traceback
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import beepy
from datetime import time, date


def emp():
    pass


def account_mts(login, password):
    url = 'https://login.mts.ru/amserver/NUI/?service=login-spa&statetrace=21a109bcee8a4a89ac9ed11f8e6a7470&client_id=LK&goto=https%3A%2F%2Flogin.mts.ru%2Famserver%2Foauth2%2Fauthorize%3Fscope%3Dprofile%2520account%2520phone%2520slaves%253Aall%2520slaves%253Aprofile%2520sub%2520email%2520user_address%2520identity_doc%2520lbsv%2520sso%2520openid%26response_type%3Dcode%26client_id%3DLK%26state%3D21a109bcee8a4a89ac9ed11f8e6a7470%26redirect_uri%3Dhttps%253A%252F%252Fauth-lk.ssl.mts.ru%252Faccount%252Fcallback%252Flogin&realm=%2Fusers&utm_referrer=https%3A%2F%2Flk.mts.ru%2F'
    balance = 0
    try:
        driver.get(url)
        driver.find_element(By.XPATH, "//input[@id='login']").send_keys(login)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Далее')]").click()
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Далее')]")
        WebDriverWait(driver, 30).until(
            ec.presence_of_element_located((By.XPATH, "//span[@class='widget-mobile-balance__value-price']")))
        if not (ec.presence_of_element_located((By.XPATH, "//span[@class='widget-mobile-balance__value-price']"))):
            balance = 'Произошла ошибка, не удалось узнать баланс'
        else:
            balance = (driver.find_element(By.XPATH, "//span[@class='widget-mobile-balance__value-price']").text)
            driver.find_element(By.XPATH, '//div[starts-with(@class, "prp-profile-widget-container")]').click()
            driver.find_element(By.XPATH, '//div/span[contains(text(), "Выход")]').click()
            driver.find_element(By.XPATH, '//div/button[contains(text(), "Выйти")]').click()
    except Exception as ex:
        print(ex)
        #print(traceback.format_exc())
    finally:
        driver.delete_all_cookies()
        driver.execute_script('window.localStorage.clear();')
        #driver.close()
        return balance


def account_megaphone(login, password):
    url = "https://lk.megafon.ru/login"
    balance = 0
    try:
        driver.get(url)
        driver.find_element(By.XPATH, "//div[contains(text(), 'Вход по паролю')]").click()
        driver.find_element(By.XPATH, "//input[@class='mfui-text-field__field phone-input__field']").send_keys(login)
        driver.find_element(By.XPATH, "//input[@class='mfui-text-field__field text-field__input']").send_keys(password)
        driver.find_element(By.XPATH, "//span[contains(text(), 'Войти')]").click()
        if ec.presence_of_element_located((By.XPATH, "//input[@data-testid='Captcha-input']")):
            beepy.beep()
            input("Пройдите капчу и введите 'Enter' в консоль")
            driver.find_element(By.XPATH, "//input[@class='mfui-text-field__field phone-input__field']").send_keys(login)
            driver.find_element(By.XPATH, "//input[@class='mfui-text-field__field text-field__input']").send_keys(password)
            driver.find_element(By.XPATH, "//span[contains(text(), 'Войти')]").click()
        WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.XPATH,"//h1[@class='mfui-header mfui-header_color_default mfui-header_level_h1 mfui-header_h-align_inherit main-balance-widget__header']")))
        if not (ec.presence_of_element_located((By.XPATH,"//h1[@class='mfui-header mfui-header_color_default mfui-header_level_h1 mfui-header_h-align_inherit main-balance-widget__header']"))):
            balance = 'Произошла ошибка, не удалось узнать баланс'
        else:
            balance = (driver.find_element(By.XPATH,"//h1[@class='mfui-header mfui-header_color_default mfui-header_level_h1 mfui-header_h-align_inherit main-balance-widget__header']").text)
            driver.find_element(By.XPATH, '//div/div[@class="ym-header-profile-panel"]').click()
            driver.find_element(By.XPATH, '//div/button[@data-ym-action="Выйти из Личного кабинета"]').click()
    except Exception as ex:
        print(ex)
        #print(traceback.format_exc())
    finally:
        driver.delete_all_cookies()
        driver.execute_script('window.localStorage.clear();')
        #driver.close()
        return balance


def account_beeline(login, password):
    url = 'https://moskva.beeline.ru/login/'
    balance = 0
    try:
        driver.get(url)
        WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.XPATH, "//div/span[contains(text(), 'Логин')]")))
        if not ec.presence_of_element_located((By.XPATH, "//div/span[contains(text(), 'С постоянным паролем')]")):
            driver.find_element(By.XPATH, "//div/span[contains(text(), 'С постоянным паролем')]").click()
            driver.find_element(By.XPATH, "//input[@placeholder='Логин']").send_keys(login)
            driver.find_element(By.XPATH, "//input[@placeholder='Пароль']").send_keys(password)
        else:
            driver.find_element(By.XPATH, "//div/span[contains(text(), 'Логин')]").click()
            driver.find_element(By.XPATH, "//input[@placeholder='Введите логин']").send_keys(login)
            driver.find_element(By.XPATH, "//input[@placeholder='Введите пароль']").send_keys(password)
        driver.find_element(By.XPATH, "//button/span[contains(text(), 'Войти')]").click()
        if (ec.presence_of_element_located((By.XPATH, "//span[contains(text(), '₽') and @data-component='Text']"))) \
                or ((ec.presence_of_element_located((By.XPATH, '//input[@placeholder="Символы с картинки"]')))
                    or (ec.presence_of_element_located((By.XPATH, '//div/img')))):
            beepy.beep()
            input("Пройдите капчу и введите 'Enter' в консоль")
        WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.XPATH, "//span[contains(text(), '₽') and @data-component='Text']")))
        if not (ec.presence_of_element_located((By.XPATH, "//span[contains(text(), '₽') and @data-component='Text']"))):
            balance = 'Произошла ошибка, не удалось узнать баланс'
        else:
            balance = (driver.find_element(By.XPATH, "//span[contains(text(), '₽') and @data-component='Text']").text)
            driver.find_element(By.XPATH, '//div/button[@data-selector="account__button-desktop"]').click()
            driver.find_element(By.XPATH, '//div/a/span[contains(text(), "Выйти")]').click()
    except Exception as ex:
        print(ex)
        #print(traceback.format_exc())
    finally:
        driver.delete_all_cookies()
        driver.execute_script('window.localStorage.clear();')
        #driver.close()
        return balance


if __name__ == "__main__":
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(30)
    data_file = "test.xlsx"
    xl = pd.read_excel(data_file, sheet_name="Лист1")
    new_data = {
        "Логин": [],
        "Пароль": [],
        "Провайдер": [],
        "Баланс": []
    }
    for i in range(len(xl)):
        password = str(xl["Пароль"][i])
        login = str(xl["Логин"][i])
        prov = str(xl["Провайдер"][i])
        if xl["Провайдер"][i] == "beeline":
            new_data["Баланс"].append(account_beeline(login, password))
        elif xl["Провайдер"][i] == "mts":
            new_data["Баланс"].append(account_mts(login, password))
        else:
            new_data["Баланс"].append(account_megaphone(login, password))
        new_data["Провайдер"].append(prov)
        new_data["Логин"].append(login)
        new_data["Пароль"].append(password)
    driver.close()
    driver.quit()

    databasa = pd.DataFrame(new_data)

    with pd.ExcelWriter('test.xlsx', engine='openpyxl', mode='a') as writer:
        databasa.to_excel(writer, sheet_name=f'{date.today()}', index=False)


    # cache clearing commands
    # window.localStorage.clear()
    # window.sessionStorage.clear()
    # driver.delete_all_cookies()
    # — disk-cache-size=0