from taobao_auto_buy.utils.base import *
class TM_Market(AutoBuyBase):

    def __init__(self, main_url, target_url, buy_time):

        super().__init__(main_url, target_url, buy_time)

    def _login(self):

        self._browser.get(self._main_url)
        self._browser.find_element_by_link_text("亲，请登录").click()

        current_url = self._browser.current_url
        self._wait_redirect(current_url)

    def _goto_detail(self):

        self._browser.get(self._target_url)

    def _buy(self):


        buy_element = WebDriverWait(self._browser, 20).until(EC.presence_of_element_located((By.ID, "J_LinkBasket")))

        self._timer(self._buy_time)
        self._logger.info("start race !")

        buy_element = WebDriverWait(self._browser, 20).until(EC.element_to_be_clickable((By.ID, "J_LinkBasket")))
        buy_element.click()
        #self._click_until_redirect(buy_element, self._browser.current_url)

        sumit_element = WebDriverWait(self._browser, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@data-tmc='cart' and @class='tm-mcCartBtn']")))
        sumit_element = WebDriverWait(self._browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-tmc='cart' and @class='tm-mcCartBtn']")))
        self._click_until_new_tab(sumit_element)

        self._checkout()

    def _checkout(self):

        sumit_element = WebDriverWait(self._browser, 60).until(EC.presence_of_element_located((By.ID, "J_Go")))
        self._click_until_redirect(sumit_element, self._browser.current_url)

        checkout_element = WebDriverWait(self._browser, 60).until(EC.presence_of_element_located((By.XPATH, "//div[@id='submitOrderPC_1']//a[@class='go-btn']")))
        self._click_until_redirect(checkout_element, self._browser.current_url)

    def start(self):

        self._login()
        self._goto_detail()
        self._buy()