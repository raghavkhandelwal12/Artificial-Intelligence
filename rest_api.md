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

# Rest method example.py

```
import requests
Base_URL="https://jsonplaceholder.typicode.com"

def example_get():
    """GET request ka example
    Get method ka kam hai resource reterive karna
    id=1 fetch in this place"""
    
    url=f"{Base_URL}/posts/1"
    response=requests.get(url)
    #check HTTP status code (200 means success)
    response.raise_for_status()
    data=response.json()#converts response to python dict
    print("GeET Response")
    print(data)
    print("-" * 50)
example_get()
```
**Output** : 

```
GeET Response
{'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
--------------------------------------------------
```

**Post method example**
```
import requests
BASE_URL = "https://jsonplaceholder.typicode.com"
def example_post():
    """Post request ka example.
    Post method new resource create karne ke liye use hota hai.
    """
    url=f"{BASE_URL}/posts"
    payload={
        "title":"foo",
        "body":"bar",
        "userId":1
    }
    response=requests.post(url,json=payload,timeout=5)
    response.raise_for_status()
    data=response.json()
    print("Post response")
    print(data)
    print("-" *50)
example_post()
```
**Output** 
```
Post response
{'title': 'foo', 'body': 'bar', 'userId': 1, 'id': 101}
--------------------------------------------------
```

**Put Method Example**

```
import requests
BASE_URL = "https://jsonplaceholder.typicode.com"
def example_put():
    """Put request ka example
    Put method ek existing resource ko completely update karta hai"""
    url=f"{BASE_URL}/posts/1"
    payload={
        "title":"Updated Title",
        "body":"Updated body",
        "userId":1
    }
    response = requests.put(url, json=payload, timeout=5)
    response.raise_for_status()
    data = response.json()
    print("PUT Response:")
    print(data)
    print("-" * 50)
example_put()
```
**Output** :
```
PUT Response:
{'title': 'Updated Title', 'body': 'Updated body', 'userId': 1, 'id': 1}
--------------------------------------------------
```

**Patch Method Example**

```
import requests
BASE_URL = "https://jsonplaceholder.typicode.com"
def example_patch():
    """Patch request ka example
    Patch method exisiting resource ka partial update karta hai"""
    url=f"{BASE_URL}/posts/1"
    payload={
        "title":"patched title"
    }
    response=requests.patch(url,json=payload,timeout=5)
    response.raise_for_status()
    data=response.json()
    print(data)
    print("-"*50)
example_patch()
```
**Output** : 

```
{'userId': 1, 'id': 1, 'title': 'patched title', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
--------------------------------------------------
```

**Delete Method Example** 

```
import requests
BASE_URL = "https://jsonplaceholder.typicode.com"
def example_delete():
    """Delete request ka example
    DELETE method resource ko delete karta hai"""
    url=f"{BASE_URL}/posts/1"
    response=requests.delete(url,timeout=5)
     # JSONPlaceholder returns an empty object {} on delete.
    if response.status_code == 200 or response.status_code == 204:
        print("DELETE Response: Resource deleted successfully.")
    else:
        print("DELETE Response: Failed to delete resource.")
    print("-" * 50)
example_delete()
```

**Output** : 

```
DELETE Response: Resource deleted successfully.
--------------------------------------------------
```

**Options method example**
```
import requests
BASE_URL = "https://jsonplaceholder.typicode.com"
def example_options():
    """Options method sever se batata hai ki is resource per konsa
    HTTP method allowed hai"""
    
    url=f"{BASE_URL}/posts"
    response=requests.options(url,timeout=5)
    allow_methods=response.headers.get("Allow")
    print(f"Allowed methods for {url}: {allow_methods}")
    print("-" * 50)
example_options
```
**Output** : 

```
<function __main__.example_options()>
```

**Head method example** 

```
import requests
BASE_URL = "https://jsonplaceholder.typicode.com"
def example_head():
    """
    Example of sending a HEAD request to a URL and printing the response headers.
    """
    # Sending a HEAD request to the URL
    # The URL is for a specific post on the JSONPlaceholder API
    # This API is a fake online REST API for testing and prototyping
    url = f"{BASE_URL}/posts/1"

    response = requests.head(url, timeout=5)
    response.raise_for_status()
    # Print headers only
    print("HEAD Response Headers:")
    print(response.headers)
    print("-" * 50)
example_head()
```
**Options** 

```
HEAD Response Headers:
{'Date': 'Tue, 01 Apr 2025 15:20:03 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Connection': 'keep-alive', 'Report-To': '{"group":"heroku-nel","max_age":3600,"endpoints":[{"url":"https://nel.heroku.com/reports?ts=1738265099&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&s=k5%2F8pjjAdp0ulTl1%2FMlEVVh%2FLvpGISgzWq9GOo8Gg3U%3D"}]}', 'Reporting-Endpoints': 'heroku-nel=https://nel.heroku.com/reports?ts=1738265099&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&s=k5%2F8pjjAdp0ulTl1%2FMlEVVh%2FLvpGISgzWq9GOo8Gg3U%3D', 'Nel': '{"report_to":"heroku-nel","max_age":3600,"success_fraction":0.005,"failure_fraction":0.05,"response_headers":["Via"]}', 'X-Powered-By': 'Express', 'X-Ratelimit-Limit': '1000', 'X-Ratelimit-Remaining': '999', 'X-Ratelimit-Reset': '1738265115', 'Vary': 'Origin, Accept-Encoding', 'Access-Control-Allow-Credentials': 'true', 'Cache-Control': 'max-age=43200', 'Pragma': 'no-cache', 'expires': '-1', 'X-Content-Type-Options': 'nosniff', 'etag': 'W/"124-yiKdLzqO5gfBrJFrcdJ8Yq0LGnU"', 'Via': '1.1 vegur', 'Age': '14208', 'cf-cache-status': 'HIT', 'Server': 'cloudflare', 'CF-RAY': '9299117cec8f9d5d-AMS', 'Content-Encoding': 'gzip', 'alt-svc': 'h3=":443"; ma=86400', 'server-timing': 'cfL4;desc="?proto=TCP&rtt=206964&min_rtt=194805&rtt_var=78030&sent=5&recv=6&lost=0&retrans=0&sent_bytes=2840&recv_bytes=786&delivery_rate=14079&cwnd=252&unsent_bytes=0&cid=362cdba2e1b434ee&ts=288&x=0"'}
--------------------------------------------------
```











