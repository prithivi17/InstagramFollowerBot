from followerbot import InstaFollower

CHROME_DRIVER_PATH = "D:\Python course\chromedriver_win32\chromedriver.exe"

bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()


