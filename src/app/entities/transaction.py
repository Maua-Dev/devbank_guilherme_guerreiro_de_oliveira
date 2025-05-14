from typing import Tuple
from ..enums.transaction_type_enum import TransactionTypeEnum
from ..errors.entity_errors import ParamNotValidated

class Transaction:
    transaction_type: TransactionTypeEnum
    value: float
    current_balance: float
    timestamp= float

    def __init__(self, transaction_type: TransactionTypeEnum=None, value: float=None, current_balance: float=None, timestamp: float=None):
        validation_transaction_type= self.validate_transaction_type(transaction_type)
        if validation_transaction_type[0] is False:
            raise ParamNotValidated("transaction_type", validation_transaction_type[1])
        self.transaction_type = transaction_type

        validation_value= self.validate_value(value)
        if validation_value[0] is False:
            raise ParamNotValidated("value", validation_value[1])
        self.value= value

        validation_current_balance= self.validate_current_balance(current_balance)
        if validation_current_balance[0] is False:
            raise ParamNotValidated("current_balance", validation_current_balance[1])
        self.current_balance= current_balance

        validation_timestamp= self.validate_timestamp(timestamp)
        if validation_timestamp[0] is False:
            raise ParamNotValidated("timestamp", validation_timestamp[1])
        self.timestamp= round(timestamp)

    @staticmethod
    def validate_transaction_type(transaction_type: TransactionTypeEnum) -> Tuple[bool, str]:
        if transaction_type is None:
            return(False, "Transaction type is required")
        if type(transaction_type) != TransactionTypeEnum:
            return(False, "Transaction type must be a TransactionTypeEnum")
        return (True, "")
    
    @staticmethod
    def validate_value(value: float) -> Tuple[bool, str]:
        if value is None:
            return(False, "Value is required")
        if type(value) != float:
            return(False, "Value must be a float")
        if value < 0:
            return(False, "Value must be a positive number")
        return(True, "")
    
    @staticmethod
    def validate_current_balance(current_balance: float) -> Tuple[bool, str]:
        if current_balance is None:
            return(False, "Current balance is required")
        if type(current_balance) != float:
            return(False, "Current balance must be a float")
        if current_balance < 0:
            return(False, "Current balance can't be negative")
        return(True, "")

    @staticmethod
    def validate_timestamp(timestamp: float) -> Tuple[bool, str]:
        if timestamp is None:
            return(False, "Timestamp is required")
        if type(timestamp) != float:
            return(False, "Timestamp must be a float")
        if timestamp < 0:
            return(False, "Timestamp can't be negative")
        return(True, "")