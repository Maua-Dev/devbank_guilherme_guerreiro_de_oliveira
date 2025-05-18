from typing import Dict, List, Optional

from ..enums.transaction_type_enum import TransactionTypeEnum

from ..entities.transaction import Transaction

from ..repo.transaction_repository_interface import ITransactionRepository

class TransactionRepositoryMock(ITransactionRepository):
    transactions: Dict[int, Transaction]

    def __init__(self):
        self.transactions = {
            1: Transaction(transaction_type=TransactionTypeEnum.deposit, value=200.0, current_balance=1200.0, timestamp=123.4),

            2: Transaction(transaction_type=TransactionTypeEnum.withdraw, value=200.0, current_balance=800.0, timestamp=123.4)
        }
    
    def get_all_transactions(self) -> List[Transaction]:
        return list(self.transactions.values())
    
    def get_transaction(self, transaction_id:int) -> Optional[Transaction]:
        return self.transactions.get(transaction_id, None)
    
    def create_withdraw_transaction(self, transaction:Transaction) -> Optional[Transaction]:
        if transaction.transaction_type != TransactionTypeEnum.withdraw:
            return None
        self.transactions[len(self.transactions) +1]= transaction
        return transaction

    def create_deposit_transaction(self, transaction: Transaction) -> Optional[Transaction]:
        if transaction.transaction_type != TransactionTypeEnum.deposit:
            return None
        self.transactions[len(self.transactions) + 1]= transaction
        return transaction
    
    
