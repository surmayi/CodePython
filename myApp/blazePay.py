import random
import logging
import sys
import time

logger = logging.getLogger()

def simBp(data):
    global logger
    received_json_data=data
    my__response = {
        "respCode": 1,
        "statusCode": 0,
        "respMsg": "",
        "merchantTxnId": random.randint(19, 4819),
        "transactionId": received_json_data['merchantTxnId'],
        "pgTxnId": received_json_data['pgTxnId'],
        "RNN": received_json_data['rrn'],
        "rnn": received_json_data['rrn'],
        "authIdCode": received_json_data['authIdCode'],
        "amount": received_json_data['amount'],
        "currency": received_json_data['currencyCode'],
        "merchantRefundTxnId": received_json_data['merchantRefundTxnId']
    }
    status_dictionary = {
        "Refund Succcessful.": 0,
        "Refund already processed with amount 2.0": 110,
        "Invalid Amount": 110,
    }
    
    if received_json_data['amount'] == 5:
        logger.info('Marking Refund as Invalid Amount')
        my__response['respMsg'] = "Invalid Amount"

    elif received_json_data['amount'] == 2:
        logger.info('Marking Refund as Already Processed')
        my__response['respMsg'] = "Refund already processed with given amount"
        error_resp = {
            "respCode": 110,
            "statusCode": 110,
            "respMsg": "Refund already processed with given amount",
        }
        return error_resp
    elif received_json_data['amount'] == 11:
        logger.info('Exiting request, invalid response provided ')
        sys.exit()
    elif received_json_data['amount'] == 12:
        logger.info('Sleeping thread for 40 secs ')
        time.sleep(40)
        return my__response
    else:
        logger.info('Marking Refund as Success')
        my__response['respMsg'] = "Refund Succcessful."

    my__response['statusCode'] = status_dictionary[my__response['respMsg']]
    my__response['respCode'] = status_dictionary[my__response['respMsg']]
    return my__response
