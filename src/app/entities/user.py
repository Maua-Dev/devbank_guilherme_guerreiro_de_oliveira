from typing import Tuple
from re import search
from ..errors.entity_errors import ParamNotValidated

class User:
    name: str
    agency: int
    account: str
    current_balance= float

    def __init__(self, name: str=None, agency: int=None, account: str=None, current_balance: float=1000.0):
        validation_name= self.validate_name(name)
        if validation_name[0] is False:
            raise ParamNotValidated("name", validation_name[1])
        self.name= name

        validation_agency= self.validate_agency(agency)
        if validation_agency[0] is False:
            raise ParamNotValidated("agency", validation_agency[1])
        self.agency= agency
        
        validation_account= self.validate_account(account)
        if validation_account[0] is False:
            raise ParamNotValidated("agency", validation_account[1])
        self.account= account

        validation_current_balance= self.validate_current_balance(current_balance)
        if validation_current_balance[0] is False:
            raise ParamNotValidated("current balance", validation_current_balance[1])
        self.current_balance= current_balance

    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        if name is None:
            return(False, "Name is required")
        if type(name) != str:
            return (False, "Name must be a string")
        if name.isdigit():
            return(False, "Name can't be numeric")
        if len(name) < 3:
            return(False, "Name must be at least 3 characters long")
        return(True, "")
    
    @staticmethod
    def validate_agency(agency: int) -> Tuple[bool, str]:
        if agency is None:
            return(False, "Agency is required")
        if type(agency) != int:
            return(False, "Agency must be a integer")
        if agency < 0:
            return(False, "Agency can't be negative")
        if len(str(agency)) != 4:
            return(False, "Agency must have 4 digits")
        return(True, "")
    
    @staticmethod
    def validate_account(account: str) -> Tuple[bool, str]:
        if account is None:
            return(False, "Account is required")
        if type(account) != str:
            return(False, "Account must be a string")
        if not search(r'^\d{5}\-\d$', account):
            return(False, "Account must be in the format '00000-0'")
        return(True, "")
    
    @staticmethod
    def validate_current_balance(current_balance: float) -> Tuple[bool, str]:
        if type(current_balance) != float:
            return(False, "Current balance must be a float")
        if current_balance < 0:
            return(False, "Current balance can't be negative")
        return(True, "")
    
    @staticmethod
    def validate_id_user(id_user: int) -> Tuple[bool, str]:
        if id_user is None:
            return (False, "Missing 'id_user' parameter")

        if type(id_user) != int:
            return (False, "Parameter 'id_user' must be an integer")
        
        if id_user < 0:
            return (False, "Parameter 'id_user' must be a positive integer")

        return (True, "")
    
    def to_dict(self):
        return {
            "name": self.name,
            "agency": self.agency,
            "account": self.account,
            "current_balance": self.current_balance
        }