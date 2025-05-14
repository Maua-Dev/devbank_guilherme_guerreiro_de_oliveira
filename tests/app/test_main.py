from time import time
from fastapi.exceptions import HTTPException
import pytest

from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.main import deposit_transaction, get_user
from src.app.repo.transaction_repository_mock import TransactionRepositoryMock
from src.app.repo.user_repository_mock import UserRepositoryMock


class Test_Main:
    def test_get_user(self):
        repo= UserRepositoryMock()
        id_user= 1
        response= get_user(id_user)
        assert response == {
                "user": repo.users.get(id_user).to_dict()
        }
    
    def test_get_id_user_is_none(self):
        id_user= None
        with pytest.raises(HTTPException) as err:
            get_user(id_user)

    def test_get_id_user_is_not_int(self):
        id_user= 1.2
        with pytest.raises(HTTPException) as err:
            get_user(id_user)

    def test_get_id_user_is_not_positive(self):
        id_user= -1
        with pytest.raises(HTTPException) as err:
            get_user(id_user)

    def test_deposit_transaction(self):
        repo_user= UserRepositoryMock()
        repo_trans= TransactionRepositoryMock()

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
        
        