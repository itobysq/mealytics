from twill.commands import *
import time
go('http://www.myfitnesspal.com/#fancy_login')

fv("1", "email-email", "blabla.com")
fv("1", "password-clear", "testpass")

submit('0')
time.sleep(3)
showforms()