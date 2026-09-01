from playwright.sync_api import Playwright,Page

class LoginPage:
    def __init__(self,page:Page):  #self - it is represnting the class
        # inside the constructor will create all the locators which are related to login page
        self.page=page# assianing page to a class variable self.page,when ever we want to refer a page ,refer with self.page
        self.login_link=self.page.locator("#login2")#Give meaningfull name
        self.username_input=self.page.locator("#loginusername")
        self.password_input=self.page.locator("#loginpassword")
        self.login_button=self.page.locator("button[onclick='logIn()']")
    #     varibale Should also belong to same class so we use self.login_link,self.user,self.pass

    # ActionMethods
    # 1.login_link we do click action

    def click_login_link(self):
        self.login_link.click()

    def enter_username(self,username): #Username will pass from testcase
        self.username_input.fill("") #clears the input box
        self.username_input.fill(username)

    def enter_password(self,password):
        self.password_input.fill("") 
        self.password_input.fill(password)

    def click_login_button(self):
        self.login_button.click()



