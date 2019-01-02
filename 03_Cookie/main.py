import cookie

c1 = cookie.Cookie(True,3,2,0.5)
c2 = cookie.Cookie(False,4,0,1)
print("\ncookie 1=\n"+c1.print_cookie())
print("cookie 2=\n"+c2.print_cookie())

c1.sugar=5
print("\ncookie 1=\n"+c1.print_cookie())
print("cookie 2=\n"+c2.print_cookie())

c2=c1
print("\ncookie 1=\n"+c1.print_cookie())
print("cookie 2=\n"+c2.print_cookie())

c2.eggs=6
print("\ncookie 1=\n"+c1.print_cookie())
print("cookie 2=\n"+c2.print_cookie())
