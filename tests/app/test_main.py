from time import time
from fastapi.exceptions import HTTPException
import pytest

from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.main import deposit_transaction, get_history, get_user, withdraw_transaction
from src.app.repo.transaction_repository_mock import TransactionRepositoryMock
from src.app.repo.user_repository_mock import UserRepositoryMock


class Test_Main:
    def test_get_history(self):
        repo=TransactionRepositoryMock().get_all_transactions()

        history= get_history()

        assert history == {
                "all_transaction": [transaction.to_dict() for transaction in repo]
        }
        
    def test_get_user(self):
        repo= UserRepositoryMock()
        response= get_user()
        assert response == {
                "user": repo.users.get(1).to_dict()
        }
    
    def test_deposit_transaction(self):
        body = {
            '2': 0,
            '5': 2,
            '10': 0,
            '20': 0,
            '50': 0,
            '100': 0,
            '200': 0
        }

        response= deposit_transaction(request=body)

        assert response == {
            "Current balance": 1210.0,
            "timestamp": round(time())
        }

    def test_deposit_transaction_value_is_none(self):

        with pytest.raises(HTTPException) as err:
            deposit_transaction(request=None)

    def test_deposit_transaction_value_is_not_dict(self):

        with pytest.raises(HTTPException) as err:
            deposit_transaction(request=1)

    def test_deposit_transaction_request_have_none_arg(self):

        body = {
            '2': 0,
            '5': None,
            '10': 0,
            '20': 0,
            '50': 0,
            '100': 0,
            '200': 0,
        }
        
        with pytest.raises(HTTPException) as err:
            deposit_transaction(request=body)

    def test_deposit_transaction_value_is_negative(self):

        body = {
            '2': 0,
            '5': -2,
            '10': 0,
            '20': 0,
            '50': 0,
            '100': 0,
            '200': 0,
        }

        with pytest.raises(HTTPException) as err:
            deposit_transaction(request=body)

    def test_deposit_transaction_value_to_higher(self):

        body = {
            '2': 0,
            '5': 0,
            '10': 0,
            '20': 0,
            '50': 0,
            '100': 0,
            '200': 13
        }

        with pytest.raises(HTTPException) as err:
            deposit_transaction(request=body)

    def test_withdraw_transaction(self):
        body = {
            '2': 0,
            '5': 0,
            '10': 0,
            '20': 0,
            '50': 0,
            '100': 0,
            '200': 1
        }
        response= withdraw_transaction(request=body)

        assert response == {
            "Current balance": 1010.0,
            "timestamp": round(time())
        }

    def test_withdraw_transaction_value_is_none(self):

        with pytest.raises(HTTPException) as err:
            withdraw_transaction(request=None)

    def test_withdraw_transaction_value_is_not_dict(self):

        with pytest.raises(HTTPException) as err:
            withdraw_transaction(request=1)

    def test_withdraw_transaction_request_have_none_arg(self):

        body = {
            '2': 0,
            '5': None,
            '10': 0,
            '20': 0,
            '50': 0,
            '100': 0,
            '200': 0,
        }
        
        with pytest.raises(HTTPException) as err:
            withdraw_transaction(request=body)

    def test_withdraw_transaction_value_is_negative(self):

        body = {
            '2': 0,
            '5': -2,
            '10': 0,
            '20': 0,
            '50': 0,
            '100': 0,
            '200': 0,
        }

        with pytest.raises(HTTPException) as err:
            withdraw_transaction(request=body)

    def test_withdraw_transaction_value_to_higher(self):

        body = {
            '2': 0,
            '5': 0,
            '10': 0,
            '20': 0,
            '50': 0,
            '100': 0,
            '200': 13
        }

        with pytest.raises(HTTPException) as err:
            withdraw_transaction(request=body)

    

