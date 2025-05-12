from src.app.entities.transaction import Transaction
from src.app.entities.user import User
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.repo.user_repositoy_mock import UserRepositoryMock


class Test_UserRepositoryMock:

    def test_get_user(self):
        repo= UserRepositoryMock()

        user= repo.get_user(1)
        exceptUser = repo.users.get(1)

        assert user == exceptUser

    def test_get_user_not_found(self):
        repo= UserRepositoryMock()

        user= repo.get_user(id_user=10)

        assert user is None

    def test_current_balance_after_transaction_withdraw(self):
        repo= UserRepositoryMock()

        widrawTransaction= Transaction(transaction_type=TransactionTypeEnum.withdraw, value=100.0, current_balance=1000.0, timestamp=123.4)
        balance_after_transaction= repo.current_balance_after_transaction(widrawTransaction, id_user=1)

        assert balance_after_transaction == 1100.0

    def test_current_balance_after_transaction_deposit(self):
        repo= UserRepositoryMock()

        depositTransaction= Transaction(transaction_type=TransactionTypeEnum.deposit, value=100.0, current_balance=1000.0, timestamp=123.4)
        balance_after_transaction= repo.current_balance_after_transaction(depositTransaction, id_user=1)

        assert balance_after_transaction == 1300.0 