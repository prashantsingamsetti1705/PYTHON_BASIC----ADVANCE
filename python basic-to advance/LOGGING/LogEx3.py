#LogEx3.py
import logging
logging.basicConfig(filename="nit.data",filemode="w",level=40)
print("Logging Concept is going on")
logging.critical("Critical Messages")
logging.error("Error Message")
logging.warning("Warning Message")
logging.info("Information message")
logging.debug("Debuging Message")		