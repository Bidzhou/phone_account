from selenium import webdriver
from selenium.webdriver.common.by import By
import traceback
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import beepy
import undetected_chromedriver as uc
from datetime import time, date





def account_mts(login, password):
    balance = 0
    try:
        driver.get(mts_url)
        driver.implicitly_wait(2)
        if len(driver.find_elements(By.XPATH, "//title[contains(text(), '403')]")) > 0:
            return "Код ответа 403"
        else:
            driver.implicitly_wait(30)
        driver.find_element(By.XPATH, mts_input_login).send_keys(login)
        driver.find_element(By.XPATH, mts_next_button).click()
        driver.find_element(By.XPATH, mts_input_password).send_keys(password)
        driver.find_element(By.XPATH, mts_next_button).click()
        if len(driver.find_elements((By.XPATH, mts_balance))) < 0:
            balance = 'Произошла ошибка, не удалось узнать баланс'
        else:
            balance = (driver.find_element(By.XPATH, mts_balance).text)
            driver.find_element(By.XPATH, mts_profile_button).click()
            driver.find_element(By.XPATH, mts_exit1_button).click()
            driver.find_element(By.XPATH, mts_exit2_button).click()
    except Exception as ex:
        print(ex)
        #print(traceback.format_exc())
    finally:
        driver.delete_all_cookies()
        driver.execute_script('window.localStorage.clear();')
        return balance


def account_megaphone(login, password):
    balance = 0
    try:
        driver.get(megaphone_url)
        driver.find_element(By.XPATH, megaphone_authorization_button).click()
        driver.find_element(By.XPATH, megaphone_login_input).send_keys(login)
        driver.find_element(By.XPATH, megaphone_password_input).send_keys(password)
        driver.find_element(By.XPATH, megaphone_enter_button).click()
        if len(driver.find_elements((By.XPATH, megaphone_captcha_input))) > 0:
            beepy.beep()
            input("Пройдите капчу и введите 'Enter' в консоль")
            driver.find_element(By.XPATH, megaphone_login_input).send_keys(login)
            driver.find_element(By.XPATH, megaphone_password_input).send_keys(password)
            driver.find_element(By.XPATH, megaphone_enter_button).click()
        if len(driver.find_elements((By.XPATH, megaphone_balance))) < 0:
            balance = 'Произошла ошибка, не удалось узнать баланс'
        else:
            balance = driver.find_element(By.XPATH,megaphone_balance).text
            driver.find_element(By.XPATH, megaphone_profile_button).click()
            driver.find_element(By.XPATH, megaphone_exit_button).click()
    except Exception as ex:
        print(ex)
        #print(traceback.format_exc())
    finally:
        driver.delete_all_cookies()
        driver.execute_script('window.localStorage.clear();')
        return balance


def account_beeline(login, password):

    balance = 0
    try:
        driver.get(beeline_url)
        driver.implicitly_wait(5)
        if len(driver.find_elements((By.XPATH, beeline_authorization1_button))) < 0:
            driver.find_element(By.XPATH, beeline_authorization2_button).click()
            driver.find_element(By.XPATH, beeline_login2_input).send_keys(login)
            driver.find_element(By.XPATH, beeline_password2_input).send_keys(password)
        else:
            driver.find_element(By.XPATH, beeline_authorization1_button).click()
            driver.find_element(By.XPATH, beeline_login1_input).send_keys(login)
            driver.find_element(By.XPATH, beeline_password1_input).send_keys(password)
        driver.find_element(By.XPATH, beeline_enter_button).click()
        if len(driver.find_elements((By.XPATH, beeline_captcha_input))) > 0 or len(driver.find_elements((By.XPATH, beeline_captcha_pic))) > 0:
            beepy.beep()
            input("Пройдите капчу и введите 'Enter' в консоль")
        driver.implicitly_wait(30)
        if len(driver.find_elements((By.XPATH, beeline_balance))) < 0:
            balance = 'Произошла ошибка, не удалось узнать баланс'
        else:
            balance = driver.find_element(By.XPATH, beeline_balance).text
            driver.find_element(By.XPATH, beeline_profile_button).click()
            driver.find_element(By.XPATH, beeline_exit_button).click()
    except Exception as ex:
        print(ex)
        #print(traceback.format_exc())
    finally:
        driver.delete_all_cookies()
        driver.execute_script('window.localStorage.clear();')
        return balance


#XPATHs for MTS
mts_url = 'https://login.mts.ru'
mts_input_login = "//input[@id='login']"
mts_input_password = "//input[@id='password']"
mts_next_button = "//button[contains(text(), 'Далее')]"
mts_balance = "//span[@class='widget-mobile-balance__value-price']"
mts_profile_button = '//div[starts-with(@class, "prp-profile-widget-container")]'
mts_exit1_button = '//div/span[contains(text(), "Выход")]'
mts_exit2_button = '//div/button[contains(text(), "Выйти")]'

#XPATHs for Megaphone
megaphone_url = "https://lk.megafon.ru/login"
megaphone_authorization_button = "//div[contains(text(), 'Вход по паролю')]"
megaphone_login_input = "//input[@class='mfui-text-field__field phone-input__field']"
megaphone_password_input = "//input[@class='mfui-text-field__field text-field__input']"
megaphone_enter_button = "//span[contains(text(), 'Войти')]" 
megaphone_captcha_input = "//input[@data-testid='Captcha-input']"
megaphone_balance = "//h1[@class='mfui-header mfui-header_color_default mfui-header_level_h1 mfui-header_h-align_inherit main-balance-widget__header']"
megaphone_profile_button = '//div/div[@class="ym-header-profile-panel"]'
megaphone_exit_button = '//div/button[@data-ym-action="Выйти из Личного кабинета"]'


#XPATHs for Beeline
beeline_url = 'https://moskva.beeline.ru/login/'
beeline_authorization1_button = "//div/span[contains(text(), 'Логин')]"
beeline_authorization2_button = "//div/span[contains(text(), 'С постоянным паролем')]"
beeline_login2_input = "//input[@placeholder='Логин']"
beeline_password2_input = "//input[@placeholder='Пароль']"
beeline_login1_input = "//input[@placeholder='Введите логин']"
beeline_password1_input = "//input[@placeholder='Введите пароль']"
beeline_enter_button = "//button/span[contains(text(), 'Войти')]"
beeline_captcha_input = '//input[@placeholder="Символы с картинки"]'
beeline_captcha_pic = '//div/img'
beeline_balance = "//span[contains(text(), '₽') and @data-component='Text']"
beeline_profile_button = '//div/button[@data-selector="account__button-desktop"]'
beeline_exit_button = '//div/a/span[contains(text(), "Выйти")]'

if __name__ == "__main__":
    # driver = webdriver.Chrome()
    driver = uc.Chrome()
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


