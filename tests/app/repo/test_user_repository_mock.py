from src.app.entities.user import User
from src.app.repo.user_repositoy_mock import UserRepositoryMock


class Test_UserRepositoryMock:
    def test_get_all_user(self):
        repo= UserRepositoryMock()

        users = repo.get_all_users()
        expectUsers= repo.users

        assert expectUsers == users

    def test_get_user(self):
        repo= UserRepositoryMock()

        user= repo.get_user(1)
        exceptUser = repo.users.get(1)

        assert user == exceptUser

    def test_get_user_not_found(self):
        repo= UserRepositoryMock()

        user= repo.get_user(id_user=10)

        assert user is None

    def test_create_user(self):
        repo= UserRepositoryMock()

        len_before= len(repo.users)
        user= User("Rodrigo", agency= 8989, account= 349076)
        repo.create_user(user=user, id_user=0)
        len_after = len(repo.users)

        assert len_after == len_before + 1
        assert repo.users.get(0) == user

    def test_delete_user(self):
        repo= UserRepositoryMock()

        user_expected_to_be_deleted= repo.users.get(1)
        len_before= len(repo.users)
        user= repo.delete_user(id_user=1)
        len_after= len(repo.users)

        assert len_after == len_before -1
        assert user == user_expected_to_be_deleted

    def test_delete_user_not_found(self):
        repo= UserRepositoryMock()

        user= repo.delete_user(id_user=12)

        assert user is None
    
    def test_update_user_current_balance(self):
        repo= UserRepositoryMock()
        user= User(name="test", agency=8090, account=786745)
        user_updated= repo.update_user_current_balance(id_user=1, current_balance=1200.0)

        assert  user_updated.current_balance == user.current_balance + 200
        assert repo.users.get(1).current_balance ==  user_updated.current_balance

    def test_update_user_current_balance_not_found(self):
        repo= UserRepositoryMock()
        user_updated= repo.update_user_current_balance(id_user=5, current_balance=1200.0)

        assert user_updated == None