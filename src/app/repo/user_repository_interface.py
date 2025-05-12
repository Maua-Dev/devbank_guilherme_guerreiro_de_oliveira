from abc import ABC, abstractmethod
from typing import List, Optional

from src.app.entities.transaction import Transaction

from ..entities.user import User

class IUserRepositoy(ABC):

    
    @abstractmethod
    def get_user(self, id_user:int) -> Optional[User]:
        ''''
        Return the user with the id_user.
        If the user doens't exist, retuns None
        '''
        pass

    @abstractmethod
    def current_balance_after_transaction(self, transaction:Transaction, id_user: int) -> float:
        ''''
        Updates the user's current balance with a transaction and the id_user.
        If the id_user doensn't exist, returns None
        '''
        pass