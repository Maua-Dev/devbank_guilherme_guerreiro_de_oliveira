from time import time
from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .enums.type_enum import TransactionTypeEnum

from .entities.user import User
from .entities.transaction import Transaction

from .environments import Environments
from .errors.entity_errors import ParamNotValidated

app = FastAPI()

user_repo= Environments.get_user_repo()()
transaction_repo= Environments.get_transaction_repo()()

@app.get("/history")
def get_history():
    transactions= transaction_repo.get_all_transactions()
    return {
        "all_transaction": [transaction.to_dict() for transaction in transactions]
    }

@app.get("/")
def get_user():
    user= user_repo.get_user(1)

    if user is None:
        raise HTTPException(status_code=404, detail="User Not found")

    return user.to_dict()

@app.post("/deposit", status_code=201)
def deposit_transaction(request: dict):
    validation_request= Transaction.validate_request(request=request)
    if not validation_request[0]:
        raise HTTPException(status_code=400, detail=validation_request[1])
    
    options=['2', '5', '10', '20', '50', '100', '200']
    total_value= 0
    for i in options:
        if request.get(i,0) == None:
            raise HTTPException(status_code=400, detail="Valor inválido")
        value = float(i) * request.get(i,0)
        validation_value= Transaction.validate_value(value=value)
        if not validation_value[0]:
            raise HTTPException(status_code=400, detail=validation_value
            [1])
        total_value+= value

    user_current_balance= user_repo.get_user(1).current_balance
    
    if total_value > (2 * user_current_balance):
        raise HTTPException(status_code=403, detail="Depósito suspeito")
    
    user_current_balance+= total_value
    
    deposit_transaction= Transaction(type=TransactionTypeEnum.deposit, value=total_value, current_balance=user_current_balance, timestamp=time())

    transaction= transaction_repo.create_deposit_transaction(transaction=deposit_transaction)

    current_balance= user_repo.current_balance_after_transaction(transaction, 1)

    return {
        "Current balance" : current_balance,
        "timestamp": deposit_transaction.timestamp
    }

@app.post("/withdraw", status_code=201)
def withdraw_transaction(request: dict):
    validation_request= Transaction.validate_request(request=request)
    if not validation_request[0]:
        raise HTTPException(status_code=400, detail=validation_request[1])
    
    options=['2', '5', '10', '20', '50', '100', '200']
    total_value= 0
    for i in options:
        if request.get(i,0) == None:
            raise HTTPException(status_code=400, detail="Valor inválido")
        value = float(i) * request.get(i,0)
        validation_value= Transaction.validate_value(value=value)
        if not validation_value[0]:
            raise HTTPException(status_code=400, detail=validation_value[1])
        total_value+= value

    user_current_balance= user_repo.get_user(1).current_balance
    
    if total_value > (user_current_balance):
        raise HTTPException(status_code=403, detail="Saldo insuficiente para a transação") 
    
    user_current_balance-= total_value
    
    withdraw_transaction= Transaction(type=TransactionTypeEnum.withdraw, value=total_value, current_balance=user_current_balance, timestamp=time())

    transaction= transaction_repo.create_withdraw_transaction(transaction=withdraw_transaction)

    current_balance= user_repo.current_balance_after_transaction(transaction, 1)

    return {
        "Current balance" : current_balance,
        "timestamp": withdraw_transaction.timestamp
    }

handler = Mangum(app, lifespan="off")