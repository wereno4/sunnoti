import datetime
from suntime import Sun
from mastodon import Mastodon
import time
import schedule

client_key=             #Your Client key
client_secret=          #Your Client secret
access_token=           #Your access token
target_instance=        #Address of your instance

latitude=               #latitude (XX.XX)
longitude=              #longitude (XX.xx)
sun = Sun(latitude, longitude)

mastodon = Mastodon(client_key, client_secret, access_token, api_base_url=target_instance)

mastodon.status_post("running test", visibility="private")

def suntoot():
    if datetime.datetime.now().replace(second=0, microsecond=0) == sun.get_sunrise_time().replace(tzinfo=None):
        mastodon.status_post("아니 벌써 해가 솟았나", visibility="public")
    elif datetime.datetime.now().replace(second=0, microsecond=0) == sun.get_sunset_time().replace(tzinfo=None):
        mastodon.status_post("아니 벌써 밤이 깊었나", visibility="public")

schedule.every(1).minutes.do(suntoot)

while True:
    schedule.run_pending()
    time.sleep(1)
