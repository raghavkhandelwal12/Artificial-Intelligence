# Introduction to APIs and Their Types

## What is an API?
- API(Application Programming Interface) is a set of rules and protocol that allow different software applications to communicate with each other. It defines how requests and responses should be formatted, enabling seamless interaction between systems, even if they are built with different technologies.

## Role of APIs in Software Architecture

- APIs play a crucial role in modern software architecture by allowing modular design, where different components of an application interact with each other without being tightly coupled. Some key benefits include.

1. `Scalability` : Microservices architecture relies on APIs to enable independent scaling of different application modules.

2. `Reusability` : APIs allow code reuse across different applications.

3. `Interoperability` : APIs facilitate communication between different programming languages and platforms.

4. `Security` : APIs define access rules, ensuring only autorized requests are processed.


## How APIs Work in Python
- In Python, APIs are commonly accessed using the `requests` library. APIs follow client-server model where a client sends a requests to an API endpoint, and the server return a response.

```
## Basic API Request in Python
import requests
url="https://api.github.com/user"
response=requests.get(url)

if response.status_code==200:
    data=response.json()
    print(data)
else:
    print(f"Error:{response.status_code}")
    
```
- `requests.get(url)`: Sends a request to the API.
- `response.json()`: Converts the response into a Python dictionary.
- `status_code` : Check whether the request was successful.

## API Authentication Methods

- APIs may require authentication for secure access. Common method include.

1. `API Keys` : 

```
headers={"Authorization" : "Bearer Your_API_KEY"}
response = requests.get(url,headers=headers)
```

**What is HTTP Headers?**

- `HTTP` headers are key-value pairs sent in the request and response between a client and a server. They contain metadata about the request/response, such as.

    - `Authentication Credentials`
    - `Content-Type(JSON, XML, etc.)`
    - `User-Agent(browser type, client type, etc.)`
    - `Cahing Information`

**What is an API Key?**
- An `API key` is a unique identifier used to authenticate requests. APIs often require authentication to ensure secure access and prevent `unauthorized usage.` The API key acts like a `password` that grant permission to use the `API`.

**What is Bearer Authentication?**

- `Bearer Authenitcation(also called token authentication)` is a method where a `token` is sent in the `authorization` header. The server verifies the token to allow access.

```
Authorization: Bearer YOUR_API_KEY
```
- `Bearer` : A keyword indicating that the request uses token-based authentication.

2. `OAuth 2.0` 
 
- Used for servies like Google APIs, OpenAI etc.
- Requires client credentials and access-tokens

## Connecting with Large Language Models(LLMs) via API

**Example : Calling ChatGPT API using Python**

```
pip install openai
```

**Python code to get LLM response**

```
import openai
openai.api_key="your_openai_api_key"

response=openai.ChatCompletion.create(
    model="gpt-4"
    messages=[
        {"role":"system","content":"You are a helpful assistant."},
        {"role": "user", "content": "What is an API?"}

    ]
)
print(response["choices"][0]["message"]["content"])
```


