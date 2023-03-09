import requests as res
import os
import sys
def admin():
    logo()
    target=input("\033[0;31mEnter Target Link =>: ")
    f=open('admin.txt','r')
    b=''
    for r in f:
        
        a=target+'/'+r
        sta=res.get(a)
        if sta.status_code==200:
                print("\033[0;32mMay Be Panel =>",a)
                b=a
        else:
            print("\033[0;31m May not be panel =>",a)
    os.system('clear')
    print("\033[0;32mMay Be Panel =>",a)
def logo():
    print("""
█████╗ CODER
██╔══██╗
███████║
██╔══██║
██║  ██║
╚═╝  ╚═╝
        
                             
                                                
    """)
admin()