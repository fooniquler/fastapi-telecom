import sqlalchemy.exc
from fastapi import Depends, FastAPI
from .utils import initial_database_insert
from sqlalchemy.orm import Session
from datetime import datetime
from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Initial database insertion
@app.get('/database_insert/')
def init(db: Session = Depends(get_db)):
    try:
        initial_database_insert(db)
    except sqlalchemy.exc.IntegrityError:
        return {'message': 'Initial data already in database'}
    return {'message': 'Now there is data in database'}


@app.post('/contracts/', response_model=schemas.Contract)
def create_contract(contract: schemas.ContractCreate, db: Session = Depends(get_db)):
    return crud.create_contract(db=db, contract=contract)


@app.get('/contracts/{contract_id}', response_model=schemas.Contract)
def get_contract(contract_id: int, db: Session = Depends(get_db)):
    return crud.get_contract(db=db, contract_id=contract_id)


@app.put('/contracts/{contract_id}', response_model=schemas.Contract)
def update_contract(contract_id: int, contract: schemas.ContractCreate, db: Session = Depends(get_db)):
    return crud.update_contract(db=db, contract=contract, contract_id=contract_id)


@app.delete('/contracts/{contract_id}')
def delete_contract(contract_id: int, db: Session = Depends(get_db)):
    return crud.delete_contract(db=db, contract_id=contract_id)


@app.post('/payments/{contract_id}', response_model=schemas.Contract)
def make_payment(contract_id: int, payment: schemas.PaymentBase, db: Session = Depends(get_db)):
    return crud.make_payment(db=db, contract_id=contract_id, payment=payment)


@app.get('/balances/{contract_id}')
def get_balance(contract_id: int, date: datetime, db: Session = Depends(get_db)):
    return crud.get_balance(db=db, contract_id=contract_id, date=date)
