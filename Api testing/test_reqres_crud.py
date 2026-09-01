from playwright.sync_api import Playwright

BASE_URL = "https://reqres.in/api"
API_KEY = "free_user_3HoejTtfwwfGuNXQLMRjDpwKj8O"

# def test_get_user(playwright: Playwright):
#     request_context = playwright.request.new_context()
'''
    response=request_context.get(f"{BASE_URL}/user/2",headers={"x-api-key":API_KEY})
    assert response.status==200
    response_body=response.json()
    assert response_body["data"]["year"] == 2001
    print(response.status)  # prints the status code
    print(response.json())
    request_context.dispose()
    
    response = request_context.post(f"{BASE_URL}/user", headers={"x-api-key": API_KEY},data={"name":"Karthik","job": "QA Automation Engineer"})


    assert response.status == 201
    print(response.status)  # prints the status code
    print(response.json())
    request_con
    text.dispose()
    '''

def test_update_user(playwright: Playwright):
        request_context = playwright.request.new_context()

        response = request_context.put(
            f"{BASE_URL}/users/108",
            headers={"x-api-key": API_KEY},
            data={"name": "Karthik", "job": "Senior QA Automation Engineer"}
        )

        print(response.status)
        print(response.json())

        request_context.dispose()