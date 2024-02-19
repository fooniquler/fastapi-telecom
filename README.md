# fastapi-telecom

## Description
FastAPI app with the following functionality:
* #### Database
  * Contract (contract number (can contain latin letters, digits, hyphens, slashes 'abcd123-/'), full name of client, entity type, status, address, tariff, list of payments).
  * Address (city, street, house, apartment, list of contracts).
  * Tariff (tariff name, cost, start date, end date, list of contracts).
  * Payment (amount, date, contract).
* #### End-points
  * Method GET: /database_insert/ - Initial data entry into database.
  * Method POST: /contracts/ - Create contract.
  * Method GET: /contracts/{contract_id} - Get contract info
  * Method PUT: /contracts/{contract_id} - Update contract info
  * Method DELETE: /contracts/{contract_id} - Delete contract
  * Method POST: /payments/{contract_id} - Make payment
  * Method GET: /balances/{contract_id} - Get contract balance

## Technologies
* Python
* FastAPI
* SQLAlchemy
* PostgreSQL

## Installation and usage
Install requirements
```
pip install -r requirements.txt
```
Store database credentials as environment variables in .env file or edit database.py file.

Run server
```
uvicorn app.main:app --reload
```
