from playwright.sync_api import Playwright,Page


class Homepage:
    def __init__(self,page:Page):
        self.page=page
        self.product_list_locator="div#tbodyid div.card h4.card-title a"

        self.add_to_cart_button=page.locator("a:has-text('Add to cart')")

        self.cart_link=page.locator("#cartur")

    def add_product_to_cart(self, product_name):
        products = self.page.locator(self.product_list_locator)
        count = products.count()

        print("Total Products:", count)

        for i in range(count):
            name = products.nth(i).text_content().strip()
            print("Found Product:", name)

            if name == product_name:
                print("Clicked Product:", name)
                products.nth(i).click()

                # Wait until product page is loaded
                self.page.wait_for_load_state("load")

                print("Current URL:", self.page.url)
                break

        # Register dialog handler BEFORE clicking Add to Cart
        self.page.on("dialog", lambda dialog: dialog.accept())

        # 👇 Add these lines here
        print("Add To Cart Visible:", self.add_to_cart_button.is_visible())

        self.add_to_cart_button.click()

        print("Clicked Add To Cart")

        print("After Add To Cart URL:", self.page.url)
    def click_cart_link(self):
        self.cart_link.click()