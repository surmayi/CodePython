import random
import logging
import sys
import time
from datetime import datetime

logger = logging.getLogger()
def simAxis(received_string):
    global logger
    received_string = str(received_string).split("'")[1]
    received_string = list(received_string.split('&'))
    request = {}
    temp = []
    for i in received_string:
        temp = i.split('=')
        request[temp[0]] = temp[1]
    response = {}
    response['vpc_Amount'] = request['vpc_Amount']
    response['vpc_Command'] = request['vpc_Command']
    response['vpc_Version'] = request['vpc_Version']
    response['vpc_Merchant'] = request['vpc_Merchant']
    response['vpc_MerchTxnRef'] = request['vpc_MerchTxnRef']
    response['vpc_Locale'] = 'en_US'
    response['vpc_Card'] = 'VC'
    if(request['vpc_Amount']=='500'):
        logger.info('Marking Refund as Failure')
        response['vpc_AcqResponseCode'] = 99
        response['vpc_Mesaage'] ='Rejected'
        response['vpc_TxnResponseCode'] = 9
    elif(request['vpc_Amount']=='1200'): 
        logger.info('Sleeping threadfor 40 secs')
        time.sleep(40)
        return response
    elif(request['vpc_Amount']=='1100'): 
        logger.info('Exiting thread, invalid response provided')
        sys.exit()       
    else:
        logger.info('Marking Refund as Success')
        response['vpc_AcqResponseCode'] = 00
        response['vpc_Mesaage'] ='Approved'
        response['vpc_AuthorisedAmount'] = request['vpc_Amount']
        response['vpc_BatchNo'] = int(''.join(c for c in datetime.now().strftime('%Y%m%d')))
        response['vpc_CapturedAmount'] = request['vpc_Amount']
        response['vpc_ReceiptNo'] = random.randint(10**11, 10**12)
        response['vpc_RefundedAmount'] = request['vpc_Amount']
        response['vpc_ShopTransactionNo'] = random.randint(10**10, 10**11)
        response['vpc_TransactionNo'] = random.randint(10**10, 10**11)
        response['vpc_TxnResponseCode'] = 0
    final_response=""
    for key,value in response.items():
        final_response+=key+'='+str(value)+'&'
    l = len(final_response) -1
    final_response=final_response[:l]
    return final_response