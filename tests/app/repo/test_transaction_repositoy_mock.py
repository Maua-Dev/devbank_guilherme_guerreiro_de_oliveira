from src.app.entities.transaction import Transaction
from src.app.enums.type_enum import TransactionTypeEnum
from src.app.repo.transaction_repository_mock import TransactionRepositoryMock


class Test_TransactionRepositoryMock:
    def test_get_all_transaction(self):
        repo=TransactionRepositoryMock()

        transactions= repo.get_all_transactions()
        expectTransactions= list(repo.transactions.values())

        assert expectTransactions == transactions

    def test_get_transaction(self):
        repo=TransactionRepositoryMock()

        transaction= repo.get_transaction(transaction_id=1)
        exceptTransaction= repo.transactions.get(1, None)

        assert exceptTransaction == transaction

    def test_get_transaction_not_found(self):
        repo= TransactionRepositoryMock()

        transaction= repo.get_transaction(transaction_id=10)

        assert transaction is None

    def test_create_withdraw_transaction(self):
        repo=TransactionRepositoryMock()

        len_before= len(repo.transactions)
        widrawTransaction= Transaction(type=TransactionTypeEnum.withdraw, value=100.0, current_balance=900.0, timestamp=123.4)
        repo.create_withdraw_transaction(transaction=widrawTransaction)
        len_after= len(repo.transactions)

        assert widrawTransaction == repo.transactions.get(3)
        assert len_after == len_before + 1

    def test_create_withdraw_transaction_however_transaction_type_is_deposit(self):
        repo=TransactionRepositoryMock()

        depositTransaction= Transaction(type=TransactionTypeEnum.deposit, value=100.0, current_balance=1100.0, timestamp=123.4)
        exceptTransaction= repo.create_withdraw_transaction(transaction=depositTransaction)
        
        assert None == exceptTransaction

    def test_create_deposit_transaction(self):
        repo=TransactionRepositoryMock()

        len_before= len(repo.transactions)
        depositTransaction= Transaction(type=TransactionTypeEnum.deposit, value=100.0, current_balance=1100.0, timestamp=123.4)
        repo.create_deposit_transaction(transaction=depositTransaction)
        len_after= len(repo.transactions)

        assert depositTransaction == repo.transactions.get(3)
        assert len_after == len_before + 1

    def test_create_deposit_transaction_however_transaction_type_is_withdraw(self):
        repo=TransactionRepositoryMock()

        widrawTransaction= Transaction(type=TransactionTypeEnum.withdraw, value=100.0, current_balance=900.0, timestamp=123.4)
        exceptTransaction= repo.create_deposit_transaction(transaction=widrawTransaction)

        assert exceptTransaction == None
