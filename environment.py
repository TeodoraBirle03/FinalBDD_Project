from pages.login_page import Login_page
from pages.forgot_password_page import Forgot_password_page
from pages.home_page import Home_page
from pages.signin_page import Sign_in_page
from browser import Browser

def before_all(context):
    context.browser = Browser()
    context.login_page = Login_page()
    context.forgot_pass_page = Forgot_password_page()
    context.home_page = Home_page()
    context.signin_page = Sign_in_page()

def after_all(context):
    context.browser.close()

    # contextul este o cutiuta care contine cate un obiect de tipul fiecarei clase de pagini
    # before all = BDD
    # after all = BDD
    # de fiecare data cand adaugam o pagina noua in proiect o vom adauga in context/un obiect de tipul paginii noi