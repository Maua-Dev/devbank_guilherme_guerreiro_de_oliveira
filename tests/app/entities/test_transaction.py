import pytest
from src.app.errors.entity_errors import ParamNotValidated
from src.app.entities.transaction import Transaction
from src.app.enums.type_enum import TransactionTypeEnum


class Test_transaction:
    def test_transaction(self):
        transaction= Transaction(type=TransactionTypeEnum.deposit, value=200.2, current_balance=1200.2, timestamp="123")

        assert transaction.type == TransactionTypeEnum.deposit
        assert transaction.value == 200.2
        assert transaction.current_balance == 1200.2
        assert transaction.timestamp == "123"
    
    def test_type_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(value=200.2, current_balance=1200.2, timestamp="123")

    def test_type_is_not_enum(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type="deposit",value=200.2, current_balance=1200.2, timestamp="123")

    def test_value_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.deposit, current_balance=1200.2, timestamp="123")
    
    def test_value_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.deposit, value=200, current_balance=1200.2, timestamp="123")
    
    def test_value_is_negative(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.deposit, value=-200.2, current_balance=1200.2, timestamp="123")

    def test_current_balance_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.deposit, value=200.2, timestamp="123")
    
    def test_current_balance_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.deposit, value=200.2, current_balance=1200, timestamp="123")
    
    def test_current_balance_is_negative(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.deposit, value=200.2, current_balance=-1200.2, timestamp="123")

    def test_timestamp_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.deposit, value=200.2, current_balance=1200.2)
    
    def test_timestamp_is_not_str(self):
        with pytest.raises(ParamNotValidated):
            Transaction(type=TransactionTypeEnum.deposit, value=200.2, current_balance=1200.2, timestamp=123)
    