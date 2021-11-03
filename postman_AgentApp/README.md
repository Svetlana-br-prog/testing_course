# AgentApp b2b

```
Base URL: https://partner.agentapp.ru/
Login: qa@qa.qa
Password: 111
Api_version: v1
```
### Аутентификация 
- Получение токена осуществляется через метод /users/obtain-token</br>
Sample Body: 

```json
{
"username": "qa@qa.qa",
"password": 111
}
```
Response: 

```json
{
 "token": "a3f1f7e29076fc6ecc4f3b49c7ee8e71c605a37c"
}
```
### Создание водителя
- POST
```
Base URL: https://partner.agentapp.ru/
Api_version: v1
Resource: /insured_objects/drivers
Header: Authorization: Token {{token}}
http method: POST
```
Sample Body:
```json
{
  "first_name": "Oleg",
  "last_name": "Denisov",
  "patronymic": "Alexeevich",
  "birth_date": "1995-01-01",
  "driving_experience_started": "2015-12-09",
  "driver_licenses": [
    {
      "credential_type": "DRIVER_LICENSE",
      "number": "012345",
      "series": "1234",
      "issue_date": "2010-10-10"
    }
  ]
}
```
Response: 
```json
{
    "id": "8385cd93-ab7c-423b-a7a5-8fa0d66c87c2",
    "fact_address": null,
    "legal_address": null,
    "contact": [],
    "driver_licenses": [
        {
            "number": "012345",
            "series": "1234",
            "issue_date": "2010-10-10",
            "credential_type": "DRIVER_LICENSE"
        }
    ],
    "first_name": "Oleg",
    "last_name": "Denisov",
    "patronymic": "Alexeevich",
    "previous_last_name": null,
    "birth_date": "1995-01-01",
    "gender": "M",
    "driving_experience_started": "2015-12-09",
    "is_rsa_checked": true,
    "is_kbm_found": false,
    "kbm_value": "1.00",
    "previous_policy_serial": null,
    "previous_policy_number": null
}
```
### Создание собственника 
- POST
```
Base URL: https://partner.agentapp.ru/
Api_version: v1
Resource: /insured_objects/owners/natural_persons
Header: Authorization: Token {{token}}
http method: POST
```
Sample Body:
```json
{
  "last_name": "Olishova",
  "first_name": "Alina",
  "patronymic": "Sergeevna",
  "birth_date": "1990-01-01",
  "credential": [
    {
      "credential_type": "RUSSIAN_INTERNAL_PASSPORT",
      "issue_date": "2017-03-08",
      "issue_point": "УФМС",
      "issue_point_code": "123-456",
      "number": "123456",
      "series": "1234"
    }
  ],
  "address": [
    {
      "address_query": "г Санкт-Петербург, г Ломоносов, ул Швейцарская, д 1 к 1, кв 1",
      "address_type": "LEGAL_ADDRESS",
      "region_kladr_id": "7800000000000",
      "city_kladr_id": "7800000600000"
    },
    {
      "address_query": "г Санкт-Петербург, г Ломоносов, ул Швейцарская, д 1 к 1, кв 1",
      "address_type": "ACTUAL_ADDRESS",
      "region_kladr_id": "7800000000000",
      "city_kladr_id": "7800000600000"
    }
  ]
}
```
Response: 
Для создания страхового объекта брать ID из поля Person
### Создание страхователя  
- POST
```
Base URL: https://partner.agentapp.ru/
Api_version: v1
Resource: /insured_objects/insurants/natural_persons
Header: Authorization: Token {{token}}
http method: POST
```
Sample Body:
```json
{
  "last_name": "Olifeev",
  "first_name": "Alexander",
  "patronymic": "Petrovich",
  "birth_date": "1990-01-01",
  "credential": [
    {
      "credential_type": "RUSSIAN_INTERNAL_PASSPORT",
      "issue_date": "2010-10-10",
      "issue_point": "УФМС",
      "issue_point_code": "123-456",
      "number": "123456",
      "series": "1234"
    }
  ],
  "address": [
    {
      "address_query": "г Санкт-Петербург, г Ломоносов, ул Швейцарская, д 1 к 1, кв 1",
      "address_type": "LEGAL_ADDRESS",
      "region_kladr_id": "7800000000000",
      "city_kladr_id": "7800000600000"
    },
    {
      "address_query": "г Санкт-Петербург, г Ломоносов, ул Швейцарская, д 1 к 1, кв 1",
      "address_type": "ACTUAL_ADDRESS",
      "region_kladr_id": "7800000000000",
      "city_kladr_id": "7800000600000"
    }
  ]
}
```
Response: 
Для создания страхового объекта брать ID из поля Person
### Создание автомобиля
- POST
```
Base URL: https://partner.agentapp.ru/
Api_version: v3
Resource: /insured_objects/cars
Header: Authorization: Token {{token}}
http method: POST
```
Sample Body:
```json
{
  "car_model_id": 864026180,
  "engine_power": 211,
  "chassis_number": null,
  "car_body_number": null,
  "vin_number": "WAUZZZ8T4BA037241",
  "number_plate": "Р904МХ178",
  "manufacturing_year": 2010,
  "max_mass": null,
  "credential": [
    {
      "credential_type": "VEHICLE_REGISTRATION",
      "issue_date": "2010-11-01",
      "number": "267461",
      "series": "78УН"
    }
  ]
}
```
Response: 
```json
{
    "id": "93037dbd-84d2-4e76-99b3-37d839b79918",
    "credential": [
        {
            "id": "b4ae19f6-d241-409e-8cda-5c7d55b1500a",
            "issue_date": "2010-11-01",
            "issue_point": null,
            "issue_point_code": null,
            "expiration_date": null,
            "number": "267461",
            "series": "78УН",
            "credential_type": "VEHICLE_REGISTRATION"
        },
        {
            "id": "6ceea836-7723-43f1-a52a-b255a323fab4",
            "issue_date": "2021-09-22",
            "issue_point": null,
            "issue_point_code": null,
            "expiration_date": "2022-09-22",
            "number": "104620112101150",
            "series": null,
            "credential_type": "DIAGNOSTIC_CHART"
        }
    ],
    "car_mark": "Audi",
    "car_mark_id": "471",
    "car_type": "B",
    "car_model": "A5",
    "car_model_id": "864026180",
    "rsa_code": "9020018",
    "manufacturing_year": 2010,
    "vin_number": "WAUZZZ8T4BA037241",
    "car_body_number": null,
    "chassis_number": null,
    "car_modification": null,
    "car_modification_id": null,
    "transdekra_id": null,
    "number_plate": "Р904МХ178",
    "has_trailer": false,
    "is_foreign": true,
    "color": null,
    "engine_displacement": null,
    "engine_power": 211.0,
    "pts_mark": null,
    "pts_model": null,
    "max_mass": null,
    "seats_count": null,
    "is_rsa_checked": false,
    "is_deprecated": false
}
```
### Объединение субъектов и объектов страхования в одну сущность “объект страхования”
- POST
```
Base URL: https://partner.agentapp.ru/
Api_version: v1
Resource: /insured_objects/
Header: Authorization: Token {{token}}
http method: POST
```
Sample Body:
```json
{
    "drivers": ["{{id_driver}}"],
    "owner": "{{id_person}}",
    "car": "{{id_vehicle}}",
    "insurant": "{{id_insurer}}"
}
```
Response:
```json
{
    "id": "08f0db81-eb05-41d6-acec-63f3e36ae76f",
    "drivers": [
        "8385cd93-ab7c-423b-a7a5-8fa0d66c87c2"
    ],
    "car": "93037dbd-84d2-4e76-99b3-37d839b79918",
    "owner": "a60c8d68-a52b-429a-8971-8a8267ceeb0c",
    "insurant": "8a22f21d-2c6d-49f6-9e0d-fce0d01bee32"
}
```
