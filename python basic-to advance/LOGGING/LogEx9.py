#LogEx9.py
import logging
logging.basicConfig(format='%(asctime)s  : %(levelname)s: %(message)s',datefmt='%d-%m-%Y  %I:%M:%S %p ')
print("Logging Concept is going on")
logging.critical("Critical Messages")
logging.error("Error Message")
logging.warning("Warning Message")
logging.info("Information message")
logging.debug("Debuging Message")		