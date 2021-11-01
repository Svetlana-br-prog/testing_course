# Google Maps Add API

- POST: </br>
Base URL:  https://rahulshettyacademy.com </br>
Resource: /maps/api/place/add/json</br>
Query Parameters: key=qaclick123</br>
http method: POST</br>

Sample Body:
```json
{
  "location": {
    "lat": -38.383494,
    "lng": 33.427362
  },
  "accuracy": 50,
  "name": "Frontline house",
  "phone_number": "(+91) 983 893 3937",
  "address": "29, side layout, cohen 09",
  "types": [
    "shoe park",
    "shop"
  ],
  "website": "http://google.com",
  "language": "French-IN"
}
```
Response:
```json
{
    "status": "OK",
    "place_id": "149059cf3edff71d78f0ff76ddaa8e38",
    "scope": "APP",
    "reference": "0850d04c48df4ee88ebafe5b2a90ed0e0850d04c48df4ee88ebafe5b2a90ed0e",
    "id": "0850d04c48df4ee88ebafe5b2a90ed0e"
}
```
- GET: </br>
Base URL:  https://rahulshettyacademy.com </br>
Resource: /maps/api/place/get/json</br>
Query Parameters: key=qaclick123, place_id ( place_id  value comes from Add place response)</br>
http method: GET</br>

Response:
```json
{
    "location": {
        "latitude": "-38.383494",
        "longitude": "33.427362"
    },
    "accuracy": "50",
    "name": "Frontline house",
    "phone_number": "(+91) 983 893 3937",
    "address": "29, side layout, cohen 09",
    "types": "shoe park,shop",
    "website": "http://google.com",
    "language": "French-IN"
}
```
- PUT: </br>
Base URL:  https://rahulshettyacademy.com </br>
Resource: /maps/api/place/update/json </br>
Query Parameters: key=qaclick123, place_id ( place_id  value comes from Add place response) </br>
http method: PUT </br>

Sample Body:
```json
{
  "place_id":"8d2573bdf6ceec0e474c5f388fa917fb",
  "address":"Titova 270, Russia",
  "key":"qaclick123"
}
```
Response:
```json
{
    "msg": "Address successfully updated"
}
```
- DELETE: </br>
Base URL:  https://rahulshettyacademy.com </br>
Resource: /maps/api/place/update/json </br>
Query Parameters: key=qaclick123, place_id ( place_id  value comes from Add place response) </br>
http method: DELETE </br>

Sample Body:
```json
{
    "place_id":"928b51f64aed18713b0d164d9be8d67f"
}
```
Response:
```json
{
    "status": "OK"
}
```
