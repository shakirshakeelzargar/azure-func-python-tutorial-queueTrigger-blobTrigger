import logging
import json
import azure.functions as func
import os
import sys
import inspect
dir_list = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe()))).split(os.sep, 10)
for level in range(5):
    sys.path.insert(0, os.sep.join(dir_list[:(len(dir_list)) - level]))

from emailHandler import send_email

def main(msg: func.QueueMessage) -> None:
    message = msg.get_body().decode('utf-8')
    message_dict=json.loads(message)
    send_email(message_dict)
