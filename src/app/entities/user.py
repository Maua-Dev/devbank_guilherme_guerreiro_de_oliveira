from typing import Tuple
from ..errors.entity_errors import ParamNotValidated

class User:
    name: str
    agency: int
    account: int
    current_balance= 1000

    def __init__(self, name: str=None, agency: int=None, account: int=None):
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
    def validate_account(account: int) -> Tuple[bool, str]:
        if account is None:
            return(False, "Account is required")
        if type(account) != int:
            return(False, "Account must be a integer")
        if account < 0:
            return(False, "Account can't be negative")
        if len(str(account)) != 6:
            return(False, "Account must have 6 digits")
        return(True, "")