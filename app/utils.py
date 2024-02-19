from datetime import datetime
from sqlalchemy.orm import Session
from . import models


def initial_database_insert(db: Session):
    create_addresses(db)
    create_tariffs(db)
    create_contracts(db)
    create_payments(db)


def create_contracts(db: Session):
    contract1 = models.Contract(id=1, number='A-1/1', full_name='Ivanov Ivan Ivanovich',
                                entity_type='Individual entity', status='Active',
                                address_id=1, tariff_id=1)

    contract2 = models.Contract(id=2, number='B-101/a7', full_name='Sergeev Sergey Sergeevich',
                                entity_type='Individual entity', status='Active',
                                address_id=2, tariff_id=2)

    contract3 = models.Contract(id=3, number='IP-111/aj-1', full_name='OOO Company',
                                entity_type='Legal entity', status='Active',
                                address_id=3, tariff_id=3)

    db.add(contract1)
    db.add(contract2)
    db.add(contract3)

    db.commit()

    db.refresh(contract1)
    db.refresh(contract2)
    db.refresh(contract3)


def create_addresses(db: Session):
    address1 = models.Address(id=1, city='Dubna', street='Universitetskaya street', house='19s9', apartment='424')
    address2 = models.Address(id=2, city='Dubna', street='Entusiastov street', house='21', apartment='424')
    address3 = models.Address(id=3, city='Moscow', street='Pr. Vernadskogo', house='17/3', apartment='10')

    db.add(address1)
    db.add(address2)
    db.add(address3)

    db.commit()

    db.refresh(address1)
    db.refresh(address2)
    db.refresh(address3)


def create_tariffs(db: Session):
    tariff1 = models.Tariff(id=1, name='Tariff For Students', cost=500, start_date=datetime(day=1, month=1, year=2024),
                            end_date=datetime(day=1, month=1, year=2025))

    tariff2 = models.Tariff(id=2, name='Tariff Default', cost=1000, start_date=datetime(day=1, month=1, year=2023),
                            end_date=datetime(day=1, month=1, year=2027))

    tariff3 = models.Tariff(id=3, name='Tariff For Companies', cost=1500, start_date=datetime(day=1, month=1, year=2022),
                            end_date=datetime(day=1, month=1, year=2030))

    db.add(tariff1)
    db.add(tariff2)
    db.add(tariff3)

    db.commit()

    db.refresh(tariff1)
    db.refresh(tariff2)
    db.refresh(tariff3)


def create_payments(db: Session):
    payment1 = models.Payment(id=1, amount=200, date=datetime(day=5, month=2, year=2024), contract_id=1)
    payment2 = models.Payment(id=2, amount=300, date=datetime(day=25, month=2, year=2024), contract_id=1)
    payment3 = models.Payment(id=3, amount=500, date=datetime(day=1, month=2, year=2024), contract_id=2)
    payment4 = models.Payment(id=4, amount=500, date=datetime(day=15, month=2, year=2024), contract_id=2)
    payment5 = models.Payment(id=5, amount=500, date=datetime(day=25, month=2, year=2024), contract_id=2)
    payment6 = models.Payment(id=6, amount=100, date=datetime(day=1, month=2, year=2024), contract_id=3)
    payment7 = models.Payment(id=7, amount=700, date=datetime(day=5, month=2, year=2024), contract_id=3)
    payment8 = models.Payment(id=8, amount=700, date=datetime(day=10, month=2, year=2024), contract_id=3)
    payment9 = models.Payment(id=9, amount=700, date=datetime(day=25, month=2, year=2024), contract_id=3)

    db.add(payment1)
    db.add(payment2)
    db.add(payment3)
    db.add(payment4)
    db.add(payment5)
    db.add(payment6)
    db.add(payment7)
    db.add(payment8)
    db.add(payment9)

    db.commit()

    db.refresh(payment1)
    db.refresh(payment2)
    db.refresh(payment3)
    db.refresh(payment4)
    db.refresh(payment5)
    db.refresh(payment6)
    db.refresh(payment7)
    db.refresh(payment8)
    db.refresh(payment9)
