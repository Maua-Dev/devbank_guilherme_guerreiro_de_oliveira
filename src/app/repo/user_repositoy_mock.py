from typing import Dict, List, Optional

from ..enums.transaction_type_enum import TransactionTypeEnum

from ..entities.transaction import Transaction

from ..repo.user_repository_interface import IUserRepositoy



from ..entities.user import User



class UserRepositoryMock(IUserRepositoy):
    users: Dict[int, User]

    def __init__(self):
        self.users = {
            1: User("Victor Soller", agency=1234, account=123456),
            2: User("Enzo Sakamoto", agency=8933, account=223456),
            3: User("Mateus", agency=8912, account=349812),
            4: User("Rubio", agency=5678, account=345678)
        }

    # def get_all_users(self) -> List[User]:
    #     return self.users
    
    def get_user(self, id_user: int) -> Optional[User]:
        return self.users.get(id_user, None)
    
    # def create_user(self, user: User, id_user: int) -> User:
    #     self.users[id_user] = user
    #     return user
    
    # def delete_user(self, id_user) -> User:
    #     user= self.users.pop(id_user, None)
    #     return user
    
    # def update_user_current_balance(self, id_user:int, current_balance:float) -> User:
    #     user= self.users.get(id_user, None)
    #     if user is None:
    #         return None
        
    #     if current_balance is not None:
    #         user.current_balance= current_balance
    #     self.users[id_user]= user

    #     return user
    
    def current_balance_after_transaction(self, transaction:Transaction, id_user: int) -> float:
        user= self.users.get(id_user, None)
        if transaction.transaction_type == TransactionTypeEnum.withdraw:
            user.current_balance -= transaction.value
        if transaction.transaction_type == TransactionTypeEnum.deposit:
            user.current_balance += transaction.value
        return user.current_balance