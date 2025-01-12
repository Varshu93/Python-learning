import requests


url="https://jsonplaceholder.typicode.com/posts/2"
print(url)

response=requests.get(url)

print(response.text)
print(response.json())
print(response.status_code)
print(response)
