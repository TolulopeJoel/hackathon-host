# Hackaton-Host

This API allows authorized users to create, list, register for, and submit to hackathons. It provides the following endpoints:

- [Hackaton-Host](#hackaton-host)
- [Hackathon](#hackathon)
  - [Create Hackathon](#create-hackathon)
  - [List Hackathons](#list-hackathons)
  - [Enrolled Hackathons](#enrolled-hackathons)
  - [Register for Hackathon](#register-for-hackathon)
- [Submission](#submission)
  - [Create Submission](#create-submission)
  - [List Submissions](#list-submissions)


The API is built using Django and Django Rest Framework with a **PostgresQL** database

# Hackathon

All APIs related to Hackathon

## Create Hackathon

This endpoint allows authorized users to create a new hackathon.

### Request

`POST api/hackathon/`

**Authentication Required:** Yes

```json
{
  "title": "Hackathon Title",
  "description": "Hackathon Description",
  "background_image": "https://example.com/background_image.jpg",
  "hackathon_image": "https://example.com/hackathon_image.jpg",
  "submission_type": "image",
  "start_datetime": "2023-06-01T00:00:00Z",
  "end_datetime": "2023-06-30T23:59:59Z",
  "reward_prize": 1000
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

```
POST api/hackathon/ HTTP/1.1
Authorization: Token <user_token>
Content-Type: application/json
```

```json

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

## List Hackathons

This endpoint retrieves a list of all hackathons.

### Request

`GET /api/hackathon/`

**Authentication Required:** Yes

#### Parameters

None

### Response

#### Success Response

```json
[
    {
        "id": 16,
        "organizer": {
            "id": 1,
            "username": "TolulopeJoel",
            "first_name": "Tolulope",
            "last_name": "Joel"
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
                "id": 81,
                "username": "testuser",
                "first_name": "Test",
                "last_name": "User"
            },
            {
                "id": 3,
                "username": "Pratham",
                "first_name": "Pratham",
                "last_name": "Ahad"
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

## Enrolled Hackathons

This endpoint retrieves a list of all hackathons current user is a participant in.

### Request

`GET /api/hackathon/enrolled`

**Authentication Required:** Yes

#### Parameters

None

### Response

#### Success Response

```json
[
    {
        "id": 7,
        "organizer": {
            "id": 13,
            "username": "CalebC",
            "first_name": "Caleb",
            "last_name": "Crater"
        },
        "title": "Transforming the Changes of AI",
        "description": "A hackathon to build AI applications based on already existing ones.",
        "background_image": "https://example.com/background-image.jpg",
        "hackathon_image": "https://example.com/hackathon-image.jpg",
        "type_of_submission": "file",
        "start_datetime": "2022-01-01T00:00:00Z",
        "end_datetime": "2022-01-03T00:00:00Z",
        "reward_prize": 7000,
        "created_at": "2022-04-20T12:34:56.789Z",
        "updated_at": "2022-04-20T12:34:56.789Z",
        "participants": [
            {
                "id": 81,
                "username": "testuser",
                "first_name": "Test",
                "last_name": "User"
            },
            {
                "id": 3,
                "username": "Barnabas",
                "first_name": "Tolulope",
                "last_name": "Joel"
            }
        ],
    },
    {
        "id": 16,
        "title": "AI for Good Hackathon",
        "description": "A hackathon to build AI applications that have a positive impact on society",
        "background_image": "https://example.com/background-image.jpg",
        "hackathon_image": "https://example.com/hackathon-image.jpg",
        "type_of_submission": "link",
        "start_datetime": "2022-02-01T00:00:00Z",
        "end_datetime": "2022-02-03T00:00:00Z",
        "reward_prize": 15000,
        "created_at": "2022-04-20T12:34:56.789Z",
        "updated_at": "2022-04-20T12:34:56.789Z",
        "participants": [
            {
                "id": 81,
                "username": "testuser",
                "first_name": "Test",
                "last_name": "User"
            },
            {
                "id": 3,
                "username": "Pratham",
                "first_name": "Pratham",
                "last_name": "Ahad"
            }
        ]
    }
]
```

## Register for Hackathon

This endpoint registers a user for a specific hackathon, by adding them to part of participants of a hackathon.

### Request

`POST /api/hackathon/<int:hackathon_id>/register/`

**Authentication Required:** Yes


#### Parameters

None

### Response

```json
{
    "message": "You have successfully registered for ${hackathon.title}",
}
```



# Submission

All APIs related to Submissions


## Create Submission

This endpoint allows authorized users to create submissions for hackathons.

### Request

`POST api/submissions/`

**Authentication Required:** Yes

```json
{
    "hackathon_id": 23,
    "name": "Using AI to secure users authorization",
    "summary": "Hello World",
    "file": "https://example.com/media/submissions/files/file.pdf",
}
```

#### Parameters

Image, file and link parameters are required based on hackathon submission type.

| Name           | Description                                       |
| -------------- | ------------------------------------------------- |
| `name`         | **Required**. The name of the submission.         |
| `summary`      | **Required**. The summary of the submission.      |
| `file`         | **Not Required**. The file for submission.        |
| `image`        | **Not Required**. The image file for submission.  |
| `link`         | **Not Required**. The URL for submission.         |
| `hackathon_id` | **Required**. The id of the registered hackathon. |

### Response

```json
{
    "id": 23,
    "user": {
        "id": 34,
        "username": "Thomason",
        "first_name": "Thomas",
        "last_name": "Richardson"
    },
    "hackathon": "Bliss Hackathon for Good",
    "name": "Using AI to secure users authorization",
    "summary": "Hello World",
    "file": "https://example.com/media/submissions/files/file.pdf",
    "link": null,
    "image": null,

    "created_at": "2023-05-17T15:05:15.102781Z",
    "updated_at": "2023-05-17T15:05:15.102824Z"
}
```


## List Submissions

This endpoint retrieves a list of all user submission for hackathons.

### Request

`GET /api/submissions/`

**Authentication Required:** Yes

#### Parameters

None

### Response

#### Success Response

```json
[
    {
        "id": 23,
        "user": {
            "id": 34,
            "username": "Thomason",
            "first_name": "Thomas",
            "last_name": "Richardson"
        },
        "hackathon": "Bliss Hackathon for Good",
        "name": "Using AI to secure users authorization",
        "summary": "Hello World",
        "file": "https://example.com/media/submissions/files/file.pdf",
        "link": null,
        "image": null,

        "created_at": "2023-05-17T15:05:15.102781Z",
        "updated_at": "2023-05-17T15:05:15.102824Z"
    },
    {
        "id": 5,
        "user": {
            "id": 34,
            "username": "Thomason",
            "first_name": "Thomas",
            "last_name": "Richardson"
        },
        "hackathon": " Hackathon",
        "name": "To the moon",
        "summary": "Hello World",
        "image": "https://example.com/media/submissions/files/submission.jpeg",
        "link": null,
        "file": null,
        "created_at": "2023-05-15T08:19:44.047406Z",
        "updated_at": "2023-05-15T08:19:44.047436Z"
    },
    {
        "id": 6,
        "user": {
            "id": 34,
            "username": "Thomason",
            "first_name": "Thomas",
            "last_name": "Richardson"
        },
        "hackathon": "Bliss Hackathon",
        "name": "To the moon",
        "summary": "Hello World",
        "file": "https://example.com/media/submissions/files/sad-face-in-rounded-square_OKHspC4.png",
        "link": null,
        "image": null,
        "created_at": "2023-05-17T15:05:15.102781Z",
        "updated_at": "2023-05-17T15:05:15.102824Z"
    }
]
```
