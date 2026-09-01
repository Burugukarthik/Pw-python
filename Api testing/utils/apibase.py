from playwright.sync_api import Playwright

ordersPayload={"orders": [{"country": "India","productOrderedId": "6960eac0c941646b7a8b3e68" }]}
class APIUtils:

    # we need to call another Api which is login generate token
    def generate_token(self,playwright: Playwright):
       api_request_context=playwright.request.new_context(base_url="https://rahulshettyacademy.com")
       response=api_request_context.post(url="/api/ecom/auth/login",
                                data={"userEmail": "karthikdevopsit@gmail.com","userPassword":"Test@123"})
       assert response.ok
       print(response.json)
       responseBody=response.json()  #here response.json is in dictionary it will strore in variable
       print(responseBody)
       return responseBody["token"]
    # Almost every API is protected. Before you can create an order,
    # the server needs proof you're logged in — that's the token.
    def createOrder(self,playwright: Playwright):
        token=self.generate_token(playwright) #Dynamically generating token at Runtime
        # request is the property used to make Api calls through playwright
        # first we need to connect to server
        api_request_context=playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        # in noraml uI we will open a new page ,in api terminology opening a page means ,making a call "get,post,put"
        # it generates response storing in response variable
        response=api_request_context.post("/api/ecom/order/create-order",
                                data=ordersPayload,
                                 headers={"Authorization":token,
                                          "Content-Type":"application/json"
                                          })
        print(response.json())
        response_body=response.json()
        orderid=response_body["orders"][0]
        return orderid