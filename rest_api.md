# RESTful API
- It is a `Web service architecture` that uses the `HTTP` protocol to represent and manipulate resources.
- It primary focus to access resources through URLs and perform operations using the HTTP methods(GET, POST, PUT, DELETE, PATCH).

# What is REST

- `REST(Representational State Transfer)` is an architectural style for designing networked applications. It is a stateless communication.


# Key REST Principles

1. `Statelessness` : Each request from the client and server must contain all necessary information to process the request. This menas each request is independent and the server does not need to remember previous request or action.

    - `Authentication Info` : If the user logged in, a token or credentials to verify the user.
    - `Request data` : Any specify data needed for the request, like `user ID, query parameters, or data for creating/updating resources.`
    - `Headers` : Additional metadata, `such as content type, language preferences etc`.

2. `Resource-Based` : In `REST` every resources is identified by a unique URL(Uniform Resource Locator).
- like this **https://api.example.com/users/123** represent a specific user with id 123. Resources can by anything that is part fo the web application, such as users, posts, or products.

3. `Cacheable` : Responses from the server can be marked as cacheable, meaning that clients can store responses locally period of time. This reduces the need to repeatedly fetch the same data from the server, thus improving performance and reducing server load.

4. `Layered System` : `REST` allows for a layered architecture where the server components can be organized into different layers, such as load balancer, security filters, and caching system. 
- For example a load balance can be distribute request across multiple servers, and the client does not need to know the internal details.

5. `Uniform Interface` : This means a standard way follow to access and manipulate the resources.

# HTTP Methods(verbs) in RESTful APIs

1. `GET` :  It is used to retrieve the data from the server. Multiple GET requests return the same result , meaning they do not cause any changes to the server.
- `Example` : `GET/users`: Reterive a list of all users.

2. `POST(Create a New Resource)` : Create a new resource on the server.
- `Idempotent` : No(Multiple POST requests create multiple records).
- `Safe Operation` : No(It modifies server data).
- `Example Use Case` : Registering a new user or submitting a contact form.

3. `PUT(Update an Entire Resource)` : 
- **Purpose** : Updates an existing resources by replacing it completely.
- **Idempotent** : Yes(Same request repeatedly result in same state).
- **Safe Operation** : No(It modifies existing data).
- **Example Use Case** : Update user profile information.

4. `PATCH(Partially Update a Resource)` : 
- **Purpose** : Update specific field of a resource instead of replacing it completely.
- **Idempotent** : Usually yes(Depends on implementation)
- **Safe Operation** : No(Modifies existing data).
- **Example Use Case** : Changing a user's email address.

5. `DELETE(Remove a Resource)` : 

- **Purpose** : Deletes a resource from the server.
- **Idempotent** : Yes(Deleting the same resource multiple time give the same result).
- **Safe Operation** : No(Modifies data by removing it).
- **Example Use case** : Removing a user from the database.

6. `OPTIONS(Retrieve Allowed Method)` : 
- **Purpose** : Retrieve allowed HTTP methods for a resources.
- **Example Use Case** : Checking if a resource supports `GET, POST, PUT, etc.

7. `HEAD(Retrieves Headers Only)` : 

- **Purpose** : Similar to GET but only returns response headers(no body).
- **Example Use Case** : Checking if a resource exists without downloading content.

# How Does a REST API Work?

1. `Client Request` : A client(Such as a web browser, mobile app, or another server) initiates an HTTP request tot he REST API. This request contains.
- `URL(Endpoint)` : Specifies the resources being accessed(e.g,/users/123).
- `HTTP Method` : Defines the type of operation(GET, POST, PUT, PATCH, DELETE).
- `Headers` : Contains metadata like authentication tokens, content type, and API version.
- `Request Body`: Include data for methods like `POST and PUT`.

**Example**  : A mobile app requests a user's profile using:
```
GET /users/123 HTTP/1.1
Host : api.example.com
Authorization : Bearer<token>
Accept : application/json
```
2. `Server Processing` : Once the request reaches the server
- The `API sever` validate the request(Check authentication, required parameters, etc.)
- The server `identifies the resources` and executes the corresponding operation.
- The server `Formats the response` in a structured format like `JSON or XML`.
- It attaches an `HTTP status code` to indicate success `(200 ok), failure(404 not found), or error(500 Internal server errors)`.
- **Example** : 
```
{
"id" : 123,
"name" : "John Does",
"email" : "johndoe@example.com",
"role" : "admin
}
```
3. `Response Handling` : The client receives the API response and processes it accordingly.
- If the request was successful `(200 ok)`, the client extract and displays the data.
- If the request failed `(404 not found)`, it may show an error message.
- If the server returns a validation error `(400 Bad Request)`, the client can ask the user to correct input data.
