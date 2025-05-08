import pytest
from src.app.errors.entity_errors import ParamNotValidated
from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum


class Test_transaction:
    def test_transaction(self):
        transaction= Transaction(transaction_type=TransactionTypeEnum.deposit, value=200.2, current_balance=1200.2)

        assert transaction.transaction_type == TransactionTypeEnum.deposit
        assert transaction.value == 200.2
        assert transaction.current_balance == 1200.2
        # I didn't do the timestamp test because it's impossible to assert it to something
    
    def test_transaction_type_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(value=200.2, current_balance=1200.2)

    def test_transaction_type_is_not_enum(self):
        with pytest.raises(ParamNotValidated):
            Transaction(transaction_type="deposit",value=200.2, current_balance=1200.2)

    def test_value_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(transaction_type=TransactionTypeEnum.deposit, current_balance=1200.2)
    
    def test_value_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Transaction(transaction_type=TransactionTypeEnum.deposit, value=200, current_balance=1200.2)
    
    def test_value_is_negative(self):
        with pytest.raises(ParamNotValidated):
            Transaction(transaction_type=TransactionTypeEnum.deposit, value=-200.2, current_balance=1200.2)

    def test_current_balance_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transaction(transaction_type=TransactionTypeEnum.deposit, value=200.2)
    
    def test_current_balance_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            Transaction(transaction_type=TransactionTypeEnum.deposit, value=200.2, current_balance=1200)
    
    def test_current_balance_is_negative(self):
        with pytest.raises(ParamNotValidated):
            Transaction(transaction_type=TransactionTypeEnum.deposit, value=200.2, current_balance=-1200.2)

    