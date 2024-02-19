from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas


def get_contract(db: Session, contract_id: int):
    db_contract = db.query(models.Contract).filter(models.Contract.id == contract_id).first()
    if not db_contract:
        raise HTTPException(status_code=404, detail='Contract not found')
    return db_contract


def create_contract(db: Session, contract: schemas.ContractCreate):
    db_contract = models.Contract(number=contract.number, full_name=contract.full_name,
                                  entity_type=contract.entity_type, status=contract.status,
                                  address_id=contract.address_id, tariff_id=contract.tariff_id)

    db.add(db_contract)
    db.commit()
    db.refresh(db_contract)
    return db_contract


def update_contract(db: Session, contract_id: int, contract: schemas.ContractCreate):
    db_contract = db.query(models.Contract).filter(models.Contract.id == contract_id).first()

    if not db_contract:
        raise HTTPException(status_code=404, detail='Contract not found')

    db_contract.number = contract.number
    db_contract.full_name = contract.full_name
    db_contract.entity_type = contract.entity_type
    db_contract.status = contract.status
    db_contract.address_id = contract.address_id
    db_contract.tariff_id = contract.tariff_id
    db.commit()
    return db_contract


def delete_contract(db: Session, contract_id: int):
    db_contract = db.query(models.Contract).filter(models.Contract.id == contract_id).first()

    if not db_contract:
        raise HTTPException(status_code=404, detail='Contract not found')

    db.delete(db_contract)
    db.commit()
    return {'message': 'Contract deleted successfully'}


def make_payment(db: Session, contract_id: int, payment: schemas.PaymentBase):
    db_contract = db.query(models.Contract).filter(models.Contract.id == contract_id).first()

    if not db_contract:
        raise HTTPException(status_code=404, detail='Contract not found')

    db_payment = models.Payment(amount=payment.amount, date=payment.date, contract_id=contract_id)
    db.add(db_payment)
    db.commit()
    db.refresh(db_contract)
    return db_contract


def get_balance(db: Session, contract_id: int, date: datetime):
    db_contract = db.query(models.Contract).filter(models.Contract.id == contract_id).first()

    if not db_contract:
        raise HTTPException(status_code=404, detail='Contract not found')

    balance = sum([payment.amount for payment in db_contract.payments if payment.date <= datetime.date(date)])
    return {'balance': balance}
