import datetime

import logging
import time
import os.path

# types

from ContractSamples import ContractSamples
#from OrderSamples import OrderSamples
#from AvailableAlgoParams import AvailableAlgoParams
#from ScannerSubscriptionSamples import ScannerSubscriptionSamples
#from FaAllocationSamples import FaAllocationSamples
#from ibapi.scanner import ScanData



def SetupLogger():
    if not os.path.exists("log"):
        os.makedirs("log")

    time.strftime("pyibapi.%Y%m%d_%H%M%S.log")

    recfmt = '(%(threadName)s) %(asctime)s.%(msecs)03d %(levelname)s %(filename)s:%(lineno)d %(message)s'

    timefmt = '%y%m%d_%H:%M:%S'

    # logging.basicConfig( level=logging.DEBUG,
    #                    format=recfmt, datefmt=timefmt)
    logging.basicConfig(filename=time.strftime("log/pyibapi.%y%m%d_%H%M%S.log"),
                        filemode="w",
                        level=logging.INFO,
                        format=recfmt, datefmt=timefmt)
    logger = logging.getLogger()
    console = logging.StreamHandler()
    console.setLevel(logging.ERROR)
    logger.addHandler(console)


def historicalData_req(self):
    # Requesting historical data
    query_time = (datetime.datetime.today() - datetime.timedelta(days=180)).strftime("%Y%m%d %H:%M:%S")
    self.reqHistoricalData(4102, ContractSamples.EurGbpFx(), query_time,
                           "1 M", "1 day", "MIDPOINT", 1, 1, False, [])
    self.reqHistoricalData(4103, ContractSamples.EurGbpFx(), query_time,
                           "10 D", "1 hour", "MIDPOINT", 1, 1, False, [])