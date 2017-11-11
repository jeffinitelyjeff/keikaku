"""Interact with queue git repo."""

import os

import pytz
import yaml

from settings import QUEUE_CONFIG_FILE, QUEUE_DIRECTORY


def config():
  q_config_path = os.path.expanduser(os.path.join(QUEUE_DIRECTORY, QUEUE_CONFIG_FILE))

  with open(q_config_path, 'r') as f:
    config = yaml.load(f)

  return config


def config_tz_name():
  return config()['default_timezone']


def config_timezone():
  return pytz.timezone(config_tz_name())


def get_files():
  # FIXME:
  # - crawl directories
  # - return a list of files to process
  return []


def get_posts_ready_to_launch():
  files = get_files()

  # FIXME:
  # - parse out queue objects
  # - filter out just posts ready to go up now
  # - need to make sure the yaml dictionaries returned here have the origin
  #   filename added so we can update the file after post.
  return []


def update_posted_yaml(fname, post):
  # FIXME:
  # - get yaml
  # - insert post info
  # - find and remove original post in queue
