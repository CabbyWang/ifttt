#coding:utf-8
import os
import sys
import pathlib

from .config import Config


sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

config = Config()
config.from_object('app.setting')
config.from_object('app.secure')
