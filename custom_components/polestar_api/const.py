"""Constants for the Polestar API integration."""

from datetime import timedelta
from typing import Final

DOMAIN = "polestar_api"
ATTRIBUTION = "Data provided by https://polestar.com/"

TIMEOUT = 90

DEFAULT_SCAN_INTERVAL = timedelta(seconds=60)

CONF_VIN: Final[str] = "vin"
