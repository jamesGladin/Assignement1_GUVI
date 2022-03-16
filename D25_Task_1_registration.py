# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 14:33:25 2022

@author: JamesGladin
@email : gladinjames49@gmail.com
"""

import re
import json

regex = r'\b[A-Za-z.0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
 
 
def check(email):
 
    if(re.fullmatch(regex, email)):
        return 0
    else:
        return 1

def validate_password(password):
    if len(password) > 16 or len(password) <5:
        print("make sure password has atleast 5 and makimun of 16 letter")
        print("Invalid Password")
    elif re.search('[0-9]',password) is None:
        print("make sure password has atleast one digit")
        print("Invalid Password")
    elif re.search('[a-z]',password) is None:
        print("make sure password has atleast one small case alphabet")
        print("Invalid Password")
    elif re.search('[A-Z]',password) is None:
        print("make sure password has atleast one upper case alphabet")
        print("Invalid Password")
    else :
        print("valid password")
        return 0

 
# Driver Code
if __name__ == '__main__':
    
    Userinput = int(input('if you want to login enter 1 or if you want to register enter 2 or if you forget password enter 3:'))
   
    
    if Userinput == 2:
        email = input('Enter your email id :')
        
       
        a = check(email)
        if a == 0 :
            password = input(' Enter your password :')
            print("Valid Email")
            b = validate_password(password)
            if b == 0 : 
               with open('LoginSystemData.json', 'a') as f:      
                    f.write("\n" + email + "," + password)
                    print('Credentials Saved')
            
        else:
            print("Invalid Email")
    elif Userinput == 1:
        User = input("Enter your email id :") 
        PW = input("Password:")
        with open('LoginSystemData.json', 'r') as f: 
            readable = f.read()
            lines = readable.splitlines()
            user = list(filter(lambda l:l.split(',')[0] == User and l.split(',')[1] == PW,lines))
            if user:
                   print(user)
                   print("Login successful")
            else:
                   print("Login failed. Please register.")     
            f.close()
    elif Userinput == 3:
        User = input("Enter your email id :")
        with open('LoginSystemData.json', 'r') as f: 
            readable = f.read()
            lines = readable.splitlines() # --> ['name,pw','name,pw','name,pw']
            user = list(filter(lambda l:l.split(',')[0] == User,lines)) 
            if user:
                   print(user)
                   print("Above is your Email id and Password")
            else:
                   print("Email id not found, please register")
            
           
           
