from abc import ABC, abstractmethod
from typing import List, Optional

from ..entities.transaction import Transaction



class ITransactionRepository(ABC):

    @abstractmethod
    def get_all_transactions(self) -> List[Transaction]:
        ''''
        Returns all the transactions in database
        '''
        pass

    @abstractmethod
    def get_transaction(self, transaction_id) -> Optional[Transaction]:
        ''''
        Returns a the transaction whit the transaction_id.
        If the transaction doens't exit, retuns None
        '''
        pass
    
    @abstractmethod
    def create_withdraw_transaction(self, transaction:Transaction, transaction_id:int) -> Optional[Transaction]:
        ''''
        Creates a new withdraw Transaction.
        If the transaction_type is deposit, returns None
        '''
        pass

    @abstractmethod
    def create_deposit_transaction(self, transaction:Transaction, transaction_id:int) -> Optional[Transaction]:
        ''''
        Creates a new deposit Transaction.
        If the transaction_type is withdraw, returns None
        '''
        pass