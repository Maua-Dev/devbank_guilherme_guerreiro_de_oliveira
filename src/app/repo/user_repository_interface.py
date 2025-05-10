from abc import ABC, abstractmethod
from typing import List, Optional

from ..entities.user import User

class IUserRepositoy(ABC):

    @abstractmethod
    def get_all_users(self) -> List[User]:
        '''
        Returns all the users in the database 
        '''
        pass
    @abstractmethod
    def get_user(self, id_user:int) -> Optional[User]:
        ''''
        Return the user with the id_user.
        If the user doens't exist, retuns None
        '''
        pass

    @abstractmethod
    def create_user(self, user:User, id_user:int) -> User:
        ''''
        Creates a new User in the database
        '''
        pass

    @abstractmethod
    def delete_user(self, id_user:int) -> User:
        ''''
        Deletes the user with the given pos.
        If the id_user doesn't exist, returns None
        '''

    @abstractmethod
    def update_user_current_balance(self, id_user:int, current_balance:float) -> User:
        ''''
        Updates the user's current balance with the given pos and new balance.
        If the id_user doensn't exist, returns None
        '''
        pass