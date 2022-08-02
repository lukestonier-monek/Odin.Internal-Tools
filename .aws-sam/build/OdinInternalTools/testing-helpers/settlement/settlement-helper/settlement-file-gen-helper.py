import json
import random
import os
import sys
sys.path.insert(0, '.')
from _assets.helper_param_constructor import helper_param_constructor

# REQUIRED PARAMETERS:
# date => 2022-06-20
# merchant_id => 0000000
# number_of_transactions => 1
#
# OUTPUTS:
# [date]_[merchant_id]_settlement_file.json
#

class settlement_file_gen_helper(object):

    parent_file: str = None
    settled_transaction_file: str = None

    @staticmethod
    def start():
        params = helper_param_constructor.eval()
        settlement_file_gen_helper.fetch_settlement_models()
        settlement_file_gen_helper.generate(params['date'], params['merchant_id'], params['number_of_transactions'])
    
    @staticmethod
    def generate(date_of_gen: str = '2022-06-20', thor_merchant_id: str = '0150748', number_of_transactions: str = 0):
        date_of_gen = '{}-{}-{}'.format(date_of_gen[0:4], date_of_gen[4:6], date_of_gen[6:8])
        total_settlement_amount = 0
        total_fee_amount = 0
        settled_transactions = []

        # TRANSACTIONS
        for _ in range(int(number_of_transactions)):
            transaction_string = '{}'.format(settlement_file_gen_helper.settled_transaction_file)   # prevents changing original model
            last_4_digits = random.randint(1000, 9999)
            transaction_amount = random.randint(1000,10000) / 100
            fee_percentage = random.randint(1,10)
            fee_amount = transaction_amount * (fee_percentage / 100)
            settled_amount = transaction_amount - fee_amount

            transaction_amount = round(transaction_amount, 2)
            fee_amount = round(fee_amount, 2)
            settled_amount = round(settled_amount, 2)

            print(f'({_}) :: last4digits: {last_4_digits} :: £{transaction_amount} - £{fee_amount} ({fee_percentage}%) = £{settled_amount}')

            transaction_string = transaction_string.replace('|*LAST_4_DIGITS*|', str(last_4_digits))
            transaction_string = transaction_string.replace('|*TRANSACTION_AMOUNT*|', str(transaction_amount))
            transaction_string = transaction_string.replace('|*TRANSACTION_DATE*|', '2022-01-01T09:00:00.000Z')
            transaction_string = transaction_string.replace('|*TRANSACTION_CROSS_REF*|', '20110090006006970A57')
            transaction_string = transaction_string.replace('|*TRANSACTION_TOTAL_FEE_AMOUNT*|', str(fee_amount))
            transaction_string = transaction_string.replace('|*TRANSACTION_TOTAL_SETTLED_AMOUNT*|', str(settled_amount))

            transaction = json.loads(transaction_string)
            settled_transactions.append(transaction)

            total_settlement_amount += settled_amount
            total_fee_amount += fee_amount

        total_settlement_amount = round(total_settlement_amount, 2)
        total_fee_amount = round(total_fee_amount, 2)

        # PARENT FILE
        parent_file = '{}'.format(settlement_file_gen_helper.parent_file)
        parent_file = parent_file.replace('|*DATE_GENERATED*|', date_of_gen)
        parent_file = parent_file.replace('|*THOR_MERCHANT_ID*|', str(thor_merchant_id))
        parent_file = parent_file.replace('|*TOTAL_FEE_AMOUNT*|', str(total_fee_amount))
        parent_file = parent_file.replace('|*TOTAL_SETTLEMENT_AMOUNT*|', str(total_settlement_amount))

        parent_obj = json.loads(parent_file)
        parent_obj['settledTransactions'] = settled_transactions
        parent_obj['settlementReports'][0]['settledTransactions'] = settled_transactions

        parent_obj['summary']['settledTransactions']['quantity'] = int(number_of_transactions)
        parent_obj['settlementReports'][0]['summary']['settledTransactions']['quantity'] = int(number_of_transactions)


        file_json = [parent_obj]
        f = open(f"./_local_data/{date_of_gen}_{thor_merchant_id}_settlement_file.json", "w")
        f.write(json.dumps(file_json, indent=4))
        f.close()

    @staticmethod
    def fetch_settlement_models():
        dir_path = os.path.dirname(os.path.realpath(__file__))

        f = open(f"{dir_path}/data/settlement.json", "r")
        settlement_file_gen_helper.parent_file = f.read()
        f.close()

        f = open(f"{dir_path}/data/settled-transaction.json", "r")
        settlement_file_gen_helper.settled_transaction_file = f.read()
        f.close()
        
if __name__ == "__main__":
    settlement_file_gen_helper.start()