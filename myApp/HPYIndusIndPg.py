import random
import logging
import sys
import time
from datetime import datetime

logger = logging.getLogger()

def HPYIndusIndPgSim(data):
    global logger
    received_json_data=data
    my__response = {
        "pMerchantTranRef": received_json_data['pMerchantTranRef'],
        "pMerchantReqRef": received_json_data['pMerchantReqRef'],
        "pTranAmount": received_json_data['pTranAmount'],
        "pRequestId": received_json_data['pRequestId'],
        "pTranTime": received_json_data['pTranTime'],
        "pTranDate": received_json_data['pTranDate'],
        "pRRN": received_json_data['pRRN'],
        "pTranType": received_json_data['pTranType'],
        "pTID": received_json_data['pTID'],
        "pMercID": received_json_data['pMercID']
    }

    if received_json_data['pTranAmount'] == '000000005000':
        logger.info('Marking Refund as Failure 99')
        my__response['pRespCode'] = "99"

    elif received_json_data['pTranAmount'] == '000000002000':
        logger.info('Marking Refund as Failure 10')
        my__response['pRespCode'] = "10"
    elif received_json_data['pTranAmount'] == '000000011000':
        logger.info('Exiting thread, invalid response provided')
        sys.exit()
    elif received_json_data['pTranAmount'] == '000000012000':
        logger.info('Sleeping threadfor 40 secs')
        time.sleep(40)   
    else:
        logger.info('Marking Refund as Success')
        my__response['pRespCode'] = "00"
    return my__response