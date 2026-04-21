import json
import requests
from socket import timeout
import logging
def hit_endpoint (url ):
    list =[]
    if (url !="null"):
        data =requests .get (url )
        dump =data .json ()
        print (dump ["count"])
        for link in dump ["entries"]:
            print (link ['Link'])
            try :
                data2 =requests .get (link ['Link'],timeout =10 )
                if (data2 .status_code ==200 ):
                    list .append (link ['Link'])
                    print (list )
                else :
                    print ("Код состояния не 200")
            except requests .exceptions .Timeout :
                logging .error ("timeout")
    else :
        print ("Ошибка загрузки URL")
hit_endpoint ("https://api.publicapis.org/entries")