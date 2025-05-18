from typing import Dict, List, Optional

from ..enums.transaction_type_enum import TransactionTypeEnum

from ..entities.transaction import Transaction

from .user_repository_interface import IUserRepository



from ..entities.user import User



class UserRepositoryMock(IUserRepository):
    users: Dict[int, User]

    def __init__(self):
        self.users = {
            1: User("Victor Soller", agency=1234, account="12345-6", current_balance=1200.0),
            2: User("Enzo Sakamoto", agency=8933, account="22345-6", current_balance=1200.0),
            3: User("Mateus", agency=8912, account="34981-2", current_balance=1200.0),
            4: User("Rubio", agency=5678, account="34567-8", current_balance=1200.0)
        }
    
    def get_user(self, id_user: int) -> Optional[User]:
        return self.users.get(id_user, None)
    
    
    def current_balance_after_transaction(self, transaction:Transaction, id_user: int) -> float:
        user= self.users.get(id_user, None)
        if transaction.transaction_type == TransactionTypeEnum.withdraw:
            user.current_balance -= transaction.value
        if transaction.transaction_type == TransactionTypeEnum.deposit:
            user.current_balance += transaction.value
        return user.current_balance