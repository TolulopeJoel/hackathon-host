# Hackaton-Host

This API allows authorized users to create, list, register for, and submit to hackathons. It provides the following endpoints:

- [Hackaton-Host](#hackaton-host)
  - [Create Hackathon](#create-hackathon)
    - [Request](#request)
      - [Parameters](#parameters)
    - [Response](#response)
  - [List Hackathons](#list-hackathons)
    - [Request](#request-1)
      - [Parameters](#parameters-1)
    - [Response](#response-1)
      - [Success Response](#success-response)
  - [Register for Hackathon](#register-for-hackathon)

The API is built using Django and Django Rest Framework with a MySQL or PostgresQL database.

## Create Hackathon

This endpoint allows authorized users to create a new hackathon.

### Request

`POST api/hackathon/`

```json
{
  "title": "Hackathon Title",
  "description": "Hackathon Description",
  "background_image": "https://example.com/background_image.jpg",
  "hackathon_image": "https://example.com/hackathon_image.jpg",
  "submission_type": "image",
  "start_datetime": "2023-06-01T00:00:00Z",
  "end_datetime": "2023-06-30T23:59:59Z",
  "reward_prize": "$1000"
}
```

#### Parameters

| Name               | Type     | Description                                                                         |
| ------------------ | -------- | ----------------------------------------------------------------------------------- |
| `title`            | `string` | **Required**. The title of the hackathon.                                           |
| `description`      | `string` | **Required**. The description of the hackathon.                                     |
| `background_image` | `string` | **Required**. The URL of the background image for the hackathon.                    |
| `hackathon_image`  | `string` | **Required**. The URL of the hackathon image.                                       |
| `submission_type`  | `string` | **Required**. The type of submission. Valid values are "image", "file", and "link". |
| `start_datetime`   | `string` | **Required**. The start date and time of the hackathon in ISO 8601 format.          |
| `end_datetime`     | `string` | **Required**. The end date and time of the hackathon in ISO 8601 format.            |
| `reward_prize`     | `string` | **Required**. The reward prize for the hackathon.                                   |

### Response

```json
POST api/hackathon/ HTTP/1.1
Authorization: Token <user_token>
Content-Type: application/json

{
  "id": 1,
  "title": "Hackathon Title",
  "description": "Hackathon Description",
  "background_image": "https://example.com/background_image.jpg",
  "hackathon_image": "https://example.com/hackathon_image.jpg",
  "submission_type": "image",
  "start_datetime": "2023-06-01T00:00:00Z",
  "end_datetime": "2023-06-30T23:59:59Z",
  "reward_prize": "$1000"
}
```

Sure! Here's the information for the "List Hackathons" API:

## List Hackathons

This endpoint retrieves a list of all hackathons.

### Request

`GET /api/hackathon/`

**Authentication Required:** Yes

#### Parameters

None

### Response

#### Success Response

**Code:** 200 OK

**Content:**

```json
[
    {
        "id": 1,
        "organizer": {
            "id": 1,
            "username": "tolu",
            "first_name": "",
            "last_name": ""
        },
        "title": "AI for Good Hackathon",
        "description": "A hackathon to build AI applications that have a positive impact on society",
        "background_image": "https://example.com/background-image.jpg",
        "hackathon_image": "https://example.com/hackathon-image.jpg",
        "type_of_submission": "file",
        "start_datetime": "2022-01-01T00:00:00Z",
        "end_datetime": "2022-01-03T00:00:00Z",
        "reward_prize": 10000,
        "created_at": "2022-04-20T12:34:56.789Z",
        "updated_at": "2022-04-20T12:34:56.789Z",
        "participants": [
            {
                "id": 1,
                "username": "testuser",
                "first_name": "Test",
                "last_name": "User"
            },
            {
                "id": 3,
                "username": "TolulopeJoel",
                "first_name": "Tolulope",
                "last_name": "Joel"
            }
        ],
    },
    {
        "id": 2,
        "title": "AI for Healthcare Hackathon",
        "description": "A hackathon to build AI applications that improve healthcare outcomes",
        "background_image": "https://example.com/background-image.jpg",
        "hackathon_image": "https://example.com/hackathon-image.jpg",
        "type_of_submission": "link",
        "start_datetime": "2022-02-01T00:00:00Z",
        "end_datetime": "2022-02-03T00:00:00Z",
        "reward_prize": 15000,
        "created_at": "2022-04-20T12:34:56.789Z",
        "updated_at": "2022-04-20T12:34:56.789Z",
        "participants": []
    }
]
```

Sure, here's the documentation for Register for Hackathon:

## Register for Hackathon

Registers a user for a specific hackathon.

**URL:** `/api/hackathon/<int:hackathon_id>/register/`

**Method:** `POST`

**Authentication Required:** Yes

**Parameters:**

None

**Example Response:**

```json
HTTP/1.1 201 Created
Content-Type: application/json

{
    "message": "You have successfully registered for ${hackathon.title}",
}
```****