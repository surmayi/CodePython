import random
import logging
import sys
import time
from datetime import datetime

logger = logging.getLogger()
def olaMoneySim(data):
    global logger
    received_json_data=data
    my__response = {
        "type": "refund",
        "merchantBillId": received_json_data['uniqueId'],
        "transactionId": received_json_data['olaTransactionId'],
        "amount": received_json_data['amount'],
        "hash": received_json_data['hash'],
        "timestamp": (datetime.utcnow()-datetime.fromtimestamp(0)).total_seconds(),
        "comments": 'optional',
        "udf": received_json_data['udf']
    }
    if received_json_data['amount'] == '5.00':
        logger.info('Marking Refund as Invalid Amount')
        my__response['status'] = "Invalid Amount"

    elif received_json_data['amount'] == '2.00':
        logger.info('Marking Refund as Failure')
        my__response['status'] = "Failure"
    elif received_json_data['amount'] == '11.00':
        logger.info('Exiting thread, invalid response provided')
        sys.exit()
    elif received_json_data['amount'] == '12.00':
        logger.info('Sleeping threadfor 40 secs')
        time.sleep(40)  
        my__response['status'] = "Failure"
    else:
        logger.info('Marking Refund as Success')
        my__response['status'] = "Success"
    return my__response