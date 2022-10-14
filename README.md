Python request
1.
    requests.request("POST", url=endpoint, headers=self.header, data=payload)

2.
    requests.post(url=endpoint, headers=self.header, json=payload)

get with query params:
    - dictionary: {key: value}
    - tuple: [(key, value)]
    - directly: ?key=value

request data vs json:   
    Passing a dict to data causes the dict to be form-encoded, 
    as though you were submitting a form on an HTML page; e.g., data={"example": "request"} 
    will be sent in the request body as example=request. The json keyword, on the other hand, 
    encodes its argument as a JSON value instead (and also sets the Content-Type header to application/json).