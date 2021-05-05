#!/home/sp/auto_env/bin/python
import sys
import configargparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class KingOfTimeLog():
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('window-size=1920x1080')
        self.chrome_options.add_argument('--disable-dev-shm-usage')

        # Open King of Time
        self.browser = webdriver.Chrome('/usr/local/bin/chromedriver', options=self.chrome_options)
        self.browser.get('https://s2.kingtime.jp/independent/recorder/personal/#')

    def site_login(self, username, password):
        self.browser.find_element_by_css_selector('#id').send_keys(username)
        self.browser.find_element_by_css_selector('#password').send_keys(password)
        self.browser.find_element_by_css_selector('#modal_window > div > div > div.btn-control-outer.btn-control-outer-size-short.align-right > div').click()

    def clock_in(self):
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_css_selector('#record_qmXXCxw9WEWN3X\/YrkMWuQ\=\= > div > div.record-btn-message.text-bold.btn-text-middle').click()

    def clock_out(self):
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_css_selector('#record_j8ekmJaw6W3M4w3i6hlSIQ\=\= > div > div.record-btn-message.text-bold.btn-text-middle').click()

    def __del__(self):
        self.browser.close()


def main(argv):
    parser = configargparse.ArgParser()

    parser.add("--clock_status", type=str,
               required=True,
               help="Clock In Or Clock Out")

    args = parser.parse_args()

    clock_status = args.clock_status

    # Get the login credentials
    with open("login_details.txt", "r") as f:
        lines = f.readlines()
        username = lines[0]
        password = lines[1]

    # Open King of Time Website
    king_of_time = KingOfTimeLog()
    # Login with your credentials
    king_of_time.site_login(username, password)

    if clock_status == "In":
        king_of_time.clock_in()
    elif clock_status == "Out":
        king_of_time.clock_out()
    else:
        print("Type: In or Out")


if __name__ == "__main__":
    main(sys.argv[1:])

