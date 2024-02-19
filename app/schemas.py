from datetime import datetime
from pydantic import BaseModel, constr


class PaymentBase(BaseModel):
    amount: float
    date: datetime


class PaymentCreate(PaymentBase):
    contract_id: int

    class Config:
        orm_mode = True


class Payment(PaymentBase):
    id: int

    class Config:
        orm_mode = True


class ContractBase(BaseModel):
    number: constr(pattern=r'^[a-zA-Z0-9\-/]*$')
    full_name: str
    entity_type: str
    status: str


class ContractCreate(ContractBase):
    address_id: int
    tariff_id: int

    class Config:
        orm_mode = True


class Contract(ContractBase):
    id: int
    payments: list[Payment]

    class Config:
        orm_mode = True

