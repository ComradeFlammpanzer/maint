#!/usr/bin/env python2
import bcrypt, sys

userpassfile="/tmp/user.pass"

if len(sys.argv)!=3:
        print("Return 0 errorcode, if auth success, else 1")
        print("usage: %s user password" % sys.argv[0])
        sys.exit(3)

givenuser,givenpassword=sys.argv[1],sys.argv[2]

userpassfileD=open(userpassfile,"r")

for userpass in userpassfileD:
        username,password=userpass.split("~")
        if givenuser==username:
                import bcrypt
                if bcrypt.hashpw(givenpassword, password) == password.rstrip():
                        print("Password correct.")
                        sys.exit(0)
                else:
                        print("Password INcorrect.")
                        sys.exit(1)
                break

print("Password INcorrect.")
sys.exit(1)
