from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base


class Contract(Base):
    __tablename__ = 'contracts'

    id = Column(Integer, primary_key=True)
    number = Column(String, unique=True, index=True)
    full_name = Column(String)
    entity_type = Column(String)
    status = Column(String)

    address_id = Column(Integer, ForeignKey('addresses.id'))
    tariff_id = Column(Integer, ForeignKey('tariffs.id'))

    address = relationship('Address', back_populates='contracts')
    tariff = relationship('Tariff', back_populates='contracts')
    payments = relationship('Payment', back_populates='contract')


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    city = Column(String)
    street = Column(String)
    house = Column(String)
    apartment = Column(String)

    contracts = relationship('Contract', back_populates='address')


class Tariff(Base):
    __tablename__ = 'tariffs'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    cost = Column(Float)
    start_date = Column(Date)
    end_date = Column(Date)

    contracts = relationship('Contract', back_populates='tariff')


class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    date = Column(Date)

    contract_id = Column(Integer, ForeignKey('contracts.id'))

    contract = relationship('Contract', back_populates='payments')
