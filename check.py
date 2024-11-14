from Digit_Recognizer import logger
from box.exceptions import BoxValueError

print("hello")
logger.info("hello")

try:
    a = 1/0
except Exception as e:
    raise BoxValueError(e)
