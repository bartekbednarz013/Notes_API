# Notes_API
Complete REST API for Notes app. Authentication is based on OAuth2 with JWT.


## Tech stack
- FastAPI
- SQLAlchemy
- SQLite


## Endpoints
| Method | Endpoint | Request data | Authorization | Action |
| :-: | - | - | :-: | --- |
| GET | / |  | - | Get welcome message |
| POST | /register | JSON: username, password | - | Register new user |
| POST | /login | Form-data: username, password | - | Login for access token |
| DELETE | /delete_account |  | required | Delete account |
| GET | /users |  | - | Get all users |
| POST | /notes | JSON: text | required | Add new note |
| GET | /notes |  | required | Get all your notes |
| GET | /notes/<note_id> |  | required | Get note by id |
| PUT | /notes/<note_id> | JSON: text | required | Edit note |
| DELETE | /notes/<note_id> |  | required | Delete note |
