#! /usr/bin/python
import dns.resolver as dr
import os
import http.client
import binascii

iplist=[]
appdomain="yeeyi.com"
def get_iplist (domain=""):
    try:
        A = dr.query(domain, 'A')
    except Exception as e:
        print("dns resolver error:" + str(e))
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)
#            print(j.address)
    return True

def checkip(ip):
    checkurl=ip+":80"
    getcontent=""
    conn=http.client.HTTPConnection(checkurl, timeout=5)
#the data type is byte, needs converting to string
    try:
        conn.request ("GET", "/", headers = {"Host": appdomain})
        r=conn.getresponse()
#h5 first 6 characters are <html>
        getcontent_h5=r.read(6)
        getcontent_h5_txt=getcontent_h5.decode("utf-8")
        print(getcontent_h5_txt)
#pre H5 first 15 characters are <! doctype html>
        getcontent_pre=r.read(15)
        getcontent_pre_txt=getcontent_pre.decode("utf-8")
        print(getcontent_pre_txt)
    finally:
        if ((getcontent_h5_txt=="<html>")or(getcontent_pre_txt=="YPE html PUBLIC")):
            print(ip + "[OK!]")
        else:
            print(ip + "[Error!]")
#    if __name__=="__main__":
#        if get_iplist(appdomain) and len (iplist) > 0:
#            for ip in iplist:
#                checkip(ip)
#                else:
#            print("DNS resolver error!")
get_iplist(appdomain)            
for ip in iplist:
#    print(ip)
    checkip(ip)