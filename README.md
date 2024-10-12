# SEE-NEMA API

## Overview
SEE-NEMA API is a robust REST API built using Django REST Framework that allows users to create and manage personalized movie watchlists. The API offers secure JWT authentication for user registration and login, enabling users to perform CRUD operations on their watchlists. Movie details are dynamically fetched from TMDb (The Movie Database), providing users with up-to-date movie information.

## Live Demo
The API is deployed on PythonAnywhere for ease of access. You can try it out live here: [Live API](https://seenema.pythonanywhere.com/api/)

## API Documentation
The API is fully documented using DRF Spectacular, and you can explore the available endpoints and their usage directly through this link: [API Documentation](https://seenema.pythonanywhere.com/api/schema/docs/).

## How to Use the API
You can interact with the API directly using tools like [Postman](https://www.postman.com/) or cURL. Below are some example requests for the key functionalities:

### 1. User Registration
**Endpoint:** `POST /api/register/`  
**Request Body:**
```json
{
  "username": "your_username",
  "password": "your_password",
  "email": "your_email@example.com"  // Optional
}
```

### 2. Obtain JWT Token
**Endpoint:** `POST /api/token/`  
**Request Body:**
```json
{
  "username": "your_username",
  "password": "your_password"
}
```

### 3. Refresh JWT Token
**Endpoint:** `POST /api/token/refresh/`  
**Request Body:**
```json
{
  "refresh": "your_refresh_token"
}
```

### 4. Manage Watchlist
#### Get Watchlist
**Endpoint:** `GET /api/watchlist/`  
**Headers:**
```
Authorization: Bearer <your_access_token>
```

#### Add a Movie
**Endpoint:** `POST /api/watchlist/add/`  
**Request Body:**
```json
{
  "title": "Inception"
}
```
**Headers:**
```
Authorization: Bearer <your_access_token>
```

#### Update a Movie
**Endpoint:** `PUT /api/watchlist/{id}/update/`  
**Request Body:**
```json
{
  "title": "Updated Title",
  "description": "Updated Description",
  "release_date": "2023-01-01"
}
```
**Headers:**
```
Authorization: Bearer <your_access_token>
```

#### Delete a Movie
**Endpoint:** `DELETE /api/watchlist/{id}/delete/`  
**Headers:**
```
Authorization: Bearer <your_access_token>
```

## Contributing
Contributions are welcome! If you're interested in improving the API or adding a frontend, feel free to reach out on [LinkedIn](https://www.linkedin.com/in/vtbossss/) or submit a pull request.

## Owner
This API is developed and maintained by [vtbossss](https://www.linkedin.com/in/vtbossss/).
