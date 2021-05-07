global driver, URL, domain, username, password
import os

# Values that provide information necessary for the script to run

URL        = os.environ.get("URL", 'N/A')
domain     = os.environ.get("DOMAIN", 'N/A')
username   = os.environ.get("USERNAME", 'N/A')
password   = os.environ.get("PASSWORD", 'N/A')
FILL_HOURS = os.environ.get("FILL_HOURS", 'N/A')
RUN_NOW    = os.environ.get("RUN_NOW", 'False')
RUN_DAYS   = os.environ.get("RUN_DAYS", 'mon,tue,wed,thu,fri')
RUN_HOUR   = os.environ.get("RUN_HOUR", '17')
RUN_MINUTE = os.environ.get("RUN_MINUTE", '0')
