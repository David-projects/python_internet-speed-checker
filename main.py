from internetSpeedTwitterBot import InternetSpeedTwitterBot

PROMISED_DOWN = 1000
PROMISED_UP = 1000
TWITTER_EMAIL = "**********"
TWITTER_PASSWORD = "***********"

speed_test = InternetSpeedTwitterBot()

internet_speed = speed_test.get_internet_speed()
print(internet_speed)
if float(internet_speed['down']) < float(PROMISED_DOWN):
    config = {
        "message": f"Hey Internet Provider, why is my internet speed {internet_speed['down']}/{internet_speed['up']}"
                   f" when I pay for {PROMISED_DOWN}/{PROMISED_UP}?",
        "username": TWITTER_EMAIL,
        "password": TWITTER_PASSWORD
    }

    speed_test.tweet_at_provider(config=config)

print(internet_speed)
