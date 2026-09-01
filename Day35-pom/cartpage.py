from playwright.sync_api import Page

class CartPage:
    def __init__(self,page:Page):
        self.page=page

        self.product_names_locator="#tbodyid tr td:nth-child(2)"

    def check_product_in_cart(self,product_name):
        products=self.page.locator(self.product_names_locator)
        count=products.count()
        print("Cart Count:", count)

        for i in range(count):
            name=products.nth(i).text_content().strip()
            print("Cart Product:", name)
            print("Searching For:", product_name)

            if name == product_name:
                print("Match Found!")
                return products.nth(i)
        print("Product Not Found")
        return None