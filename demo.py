from HateSpeech.logger import logging
from HateSpeech.exception import CustomException
import sys
#logging.info("welcome to our project")
try:
    a=10/2

except Exception as e:
    raise CustomException(e, sys) from e