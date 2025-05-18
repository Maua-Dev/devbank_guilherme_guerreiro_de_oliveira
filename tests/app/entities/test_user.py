import pytest

from src.app.entities.user import User
from src.app.errors.entity_errors import ParamNotValidated

class Test_user:
    def test_user(self):
        user= User("test", agency="1234", account="12345-6")

        assert user.name == "test"
        assert user.agency == "1234"
        assert user.account == "12345-6"
        assert user.current_balance == 1000

    def test_user_name_is_none(self):
        with pytest.raises(ParamNotValidated):
            User(agency="1234", account="12345-6")

    def test_user_name_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            User(name=1, agency="1234", account="12345-6")

    def test_user_name_is_digit(self):
        with pytest.raises(ParamNotValidated):
            User(name="1234", agency="1234", account="12345-6")

    def test_user_name_is_too_short(self):
        with pytest.raises(ParamNotValidated):
            User(name="t", agency="1234", account="12345-6")
    
    def test_user_agency_is_none(self):
        with pytest.raises(ParamNotValidated):
            User(name="test", account="12345-6")

    def test_user_agency_is_not_str(self):
        with pytest.raises(ParamNotValidated):
            User(name="test", agency=1234, account="12345-6")

    def test_user_agency_len_is_not_on_the_digit_model(self):
        with pytest.raises(ParamNotValidated):
            User(name="test",agency="12345", account="12345-6")

    def test_user_account_is_none(self):
        with pytest.raises(ParamNotValidated):
            User(name="test",agency="1234")
    
    def test_user_account_is_not_str(self):
        with pytest.raises(ParamNotValidated):
            User(name="test", agency="1234", account=123456)

    def test_user_account_is_not_on_the_digit_model(self):
        with pytest.raises(ParamNotValidated):
            User(name="test",agency="1234", account="123456")
    
    def test_current_balance_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            User(name="test",agency="1234", account="12345-6", current_balance=1000)
    
    def test_current_balance_is_negative(self):
        with pytest.raises(ParamNotValidated):
            User(name="test",agency="1234", account="12345-6", current_balance=-1000.0)
    
