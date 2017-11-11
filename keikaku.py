"""
All according to keikaku*

*Note: 'keikaku' means plan.
"""

import datetime
import pytz

import facebook
import tumblr
import twitter
import qrepo


def get_local_time():
  return ""


def main():
  local_tz = qrepo.config_timezone()
  local_dt = datetime.datetime.now(tz=pytz.utc).astimezone(local_tz)
  print("Starting keikaku at {:%H:%M} in {}".format(local_dt, local_tz))

  posts = qrepo.get_posts_ready_to_launch()
  for p in posts:
    twitter.post(p)
    tumblr.post(p)
    facebook.post(p)


if __name__ == "__main__":
  main()
