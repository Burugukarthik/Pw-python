from playwright.sync_api import Playwright


def test_create_booking(playwright: Playwright):
    request_context=playwright.request.new_context()
    base_url="https://restful-booker.herokuapp.com"
    request_body={

            "firstname": "James",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid":True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }



    response=request_context.post(f"{base_url}/booking",data=request_body)
    

    assert response.ok
    assert response.status==200

    response_body = response.json()
    assert response_body["bookingid"] is not None
    assert response_body["booking"]["firstname"] == "James"
    assert response_body["booking"]["lastname"] == "Brown"