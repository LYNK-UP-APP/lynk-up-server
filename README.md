# Lynk Up Server

## Introduction
Welcome to the backend repository of Lynk Up! Lynk Up is a social event management app designed to streamline the organization, attendance, and management of events across different friend groups. This repository houses the codebase for our backend services, intricately crafted using Python and the Django REST framework.

---
## Table of Contents
- [Directory](#directory) 
- [About](#about) 
- [Tech Stack](#tech-stack) 
- [Key Features](#key-features)
- [Getting Started](#getting-started)
- [Endpoints](#restful-endpoints)
- [Team](#team)
- [Contact](#contact)
- [Contribute](#contribute)
- [Licensing](#licensing)
---

## Directory
  [Hosted Website](<blank>)

  [Hosted Server](<blank>)

  [Client Repository](https://github.com/LYNK-UP-APP/lynk-up-client)
## About
Our backend services are at the heart of the Lynk Up app. They manage data, ensure smooth API integrations, provide secure user authentication, enable efficient event management, and prompt notification services. With Python and Django REST framework, we ensure a fast, reliable, and secure environment for our users.

## Tech Stack
- **Python:** Our primary programming language offering simplicity and versatility.
- **Django REST Framework:** Used for building APIs, ensuring a scalable and secure connection between our frontend and backend services.

## Key Features
1. **Data Management:** Employs Django ORM for seamless database queries and data manipulation.
2. **API Integrations:** Manages and integrates external APIs to augment app functionality.
3. **Event Management:** Handles all CRUD operations related to events, enabling the creation, updates, deletions, and RSVP functionalities.
---
## Getting Started
1. **Clone the Repository:** Get started with Lynk Up Backend by cloning the repository to your local machine.
2. **Install Dependencies:** Navigate into the cloned repository and install necessary dependencies.
3. **Start the Server:** Fire up the Django server.
Note: Please ensure you have Python and pip installed on your machine before running these commands.

---
## RESTful Endpoints

<details close>
<summary> All Endpoints </summary>

### Get a User

```http
GET /api/v1/users/:phone_number
```

<details close>
<summary>  Details </summary>
<br>
    
Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

{
    "data": {
        "id": "1",
        "type": "user",
        "attributes": {
            "full_name": "Antonio King Hunt",
            "phone_number": "888-888-8888",
            "email": "tesseractcode@gmail.com",
            "events": [
                {
                    "id": 1
                    "title": "Magic Tournament"
                    "date": "05/20/2023"
                    "time": "7:00 PM MST"
                    "address": { 
                                    "street": "1940 Harve. Ave.",
                                    "unit": "Ste. 1-A",
                                    "city": "Missoula",
                                    "state": "MT",
                                    "zip_code": 59801
                    }
                },
                {etc}
            ]
        }
    }
}
```

| Code | Description |
| :--- | :--- |
| 404 | `NOT FOUND` |

Response:

```json

{
    "error": [
        "title": "NOT FOUND",
        "status": "404"
    ]
}
```

</details>

---

### Get Events for a User

```http
GET /api/v1/events/:user_id
```

<details close>
<summary>  Details </summary>
<br>
    
Request: <br>
```json
{
    "user_id": 1
}
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

{
    "data": {
        "events": [
            {
                "id": "1",
                "name": "Party in the park",
                "date": "05/10/2023",
                "time": "7:00 PM MST"
            },
            {
                "id": "4",
                "name": "Another Party in the park",
                "date": "06/10/2023",
                "time": "7:00 PM MST"
            },
            {"etc": ""}
        ]
    }
}
```

| Code | Description |
| :--- | :--- |
| 404 | `NOT FOUND` |

Response:

```json

{
    "error": [
        "title": "NOT FOUND",
        "status": "404"
    ]
}
```

</details>

---

### Create Event

```http
POST /api/v1/events/
```

<details close>
<summary>  Details </summary>
<br>
    
Request: <br>
```json
{
    "title": "Party at the Park",
    "details": "PARTY IN THE PARK LETS GO",
    "address_1": "123 Main st",
    "address_2": "Unit 3",
    "city": "Fort Collins",
    "state": "CO",
    "zip_code": "80525",
    "date": "01/01/2024",
    "time": "7:00 PM MST",
    "groups": [
        {
            "id": "1"
        },
        {
            "id": "4"
        }
    ]
}
```

| Code | Description |
| :--- | :--- |
| 201 | `Created` |

Response:

```json

{
    "data": {
    "id": "1",
        "title": "Party at the Park",
        "details": "12345 W. East St.",
        "address_1": "Unit 101",
        "address_2": "Fort Collins",
        "city": "Fort Collins",
        "state": "CO",
        "zip_code": "80525",
        "date": "01/01/2024",
        "time": "7:00 PM MST",
        "groups": [
            {
                "name": "Brunch",
                "friends": [
                    {
                        "id": "1",
                        "name": "Andra Helton"
                    },
                    {
                        "id": "4",
                        "name": "Antonio King Hunt"
                    }
                ]
            }
        ]
    }
}
```

</details>

---

### Get one Event

```http
GET /api/v1/events/:event_id
```

<details close>
<summary>  Details </summary>
<br>
    
Request: <br>
```json
{
    "id": 1
}
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

{
    "data": {
        "id": "1",
        "title": "Party at the Park",
        "details": "PARTY",
        "address_1": "123 Main St",
        "address_2": "Unit 101",
        "city": "Fort Collins",
        "state": "CO",
        "zip_code": "80525",
        "date": "01/01/2024",
        "time": "7:00 PM MST",
        "group": {
            "id": "1",
            "name": "Brunch",
            "friends": [
                {
                    "id": "1",
                    "name": "Andra Helton"
                },
                {
                    "id": "4",
                    "name": "Antonio King Hunt"
                }
            ]
        }
    }
}
```

| Code | Description |
| :--- | :--- |
| 404 | `NOT FOUND` |

Response:

```json

{
    "error": [
        "title": "NOT FOUND",
        "status": "404"
    ]
}
```

</details>

---

### Get Friends

```http
GET /api/v1/users/:user_id/friends
```

<details close>
<summary>  Details </summary>
<br>
    
Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

{
    "data": {
        "friends": [
            {
                "user_id": 1,
                "user_name": "Joe Fogiato"
            },
            {
                "user_id": 2,
                "user_name": "Dawson T"
            }
        ]
    }
}
```

| Code | Description |
| :--- | :--- |
| 404 | `NOT FOUND` |

Response:

```json

{
    "error": [
        "title": "NOT FOUND",
        "status": "404"
    ]
}
```

</details>

---

### Create Friend

```http
POST /api/v1/users/:user_id/friends
```

<details close>
<summary>  Details </summary>
<br>
    
Request: <br>
```json
{
    "friend_id": 1,
    "user_id": 1
}
```

| Code | Description |
| :--- | :--- |
| 201 | `Created` |

Response:

```json

{
    "data": {
        "friends": [
            {
                "user_name": "Harrison Ryan",
                "user_id": 1
            },
            {
                "user_name": "Joe Fogiato",
                "user_id": 3
            },
            {
                "user_name": "Antonio KH",
                "user_id": 4
            },
            {
                "user_name": "Trevor Fitz",
                "user_id": 5
            }
        ]
    }
}
```

</details>

---

### Get one Group

```http
GET /api/v1/users/:user_id/groups/:group_id
```

<details close>
<summary>  Details </summary>
<br>
    
Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

{
    "data": {
        "id": "1",
        "user_id": "1"
    }
}
```

| Code | Description |
| :--- | :--- |
| 404 | `NOT FOUND` |

Response:

```json

{
    "error": [
        "title": "NOT FOUND",
        "status": "404"
    ]
}
```

</details>
</details>

---

## Team
<table>
  <tr>
    <th>Andra Helton</th>
    <th>Antonio King Hunt</th>
    <th>Dawson Timmons</th>
    <th>Harrison Ryan</th>
    <th>William Lampke</th>
  </tr>
  
<tr>
  <td><img src="https://avatars.githubusercontent.com/u/116662742?v=4" width="135" height="135"></td>
  <td><img src="https://avatars.githubusercontent.com/u/89714398?v=4" width="135" height="135"></td>
  <td><img src="https://avatars.githubusercontent.com/u/117066950?v=4" width="135" height="135"></td>
  <td><img src="https://avatars.githubusercontent.com/u/116698937?v=4" width="135" height="135"></td>
  <td><img src="https://avatars.githubusercontent.com/u/109244868?v=4" width="135" height="135"></td>
</tr>


  <tr>
    <td>
      <a href="https://github.com/ALHelton" rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
        </a><br>
      <a href="https://www.linkedin.com/in/andrahelton/" rel="nofollow noreferrer">
    <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
        </a>
    </td>
        <td>
       <a href="https://github.com/4D-Coder" rel="nofollow noreferrer">
            <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
      </a><br>
        <a href="https://www.linkedin.com/in/antoniokinghunt-4d-coder/" rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
      </a>
    </td>
        <td>
       <a href="https://github.com/DMTimmons1" rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
      </a><br>
        <a href="https://www.linkedin.com/in/dawson-timmons/" rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
      </a>
    </td>
        <td>
       <a href="https://github.com/hwryan12" rel="nofollow noreferrer">
            <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
      </a><br>
        <a href="https://www.linkedin.com/in/harrison-ryan-2b987725a/" rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
      </a>
    </td>
        <td>
       <a href="https://github.com/WilliamLampke" rel="nofollow noreferrer">
            <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
      </a><br>
        <a href="" rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
      </a>
    </td>
  </tr>   
</table>

## Contact
For any questions or suggestions, please open an issue in this repository.

---

## Contribute
We're excited to welcome contributions from everyone, irrespective of their experience level. Your input is crucial in helping us make Lynk Up better. Let's collaborate and build a top-notch social event management app together!

## Licensing
BLANK ON PURPOSE

---

Thank you for being part of our community! Together, let's make Lynk Up the best social event management app on the market.
