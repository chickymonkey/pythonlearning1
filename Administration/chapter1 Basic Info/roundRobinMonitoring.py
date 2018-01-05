#! /usr/bin/python
import dns.resolver as dr
import os
import http.client
import binascii
#test
iplist=[]
appdomain="163.com"
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
#preh5 first 14 characters are <!DOCTYPE html , h5 first 6 characters are <html>, we will read once, then test twice.
#if we get either one, means the webserver is alive
        getcontent_preh5=r.read(14)
        getcontent_preh5txt=getcontent_preh5.decode("utf-8")
#       print(getcontent_preh5txt)
#get the first 6 characters for h5 testing
        getcontent_h5_txt=getcontent_preh5txt[:6]
#        print(getcontent_h5_txt)
    finally:
        if ((getcontent_h5_txt=="<html>")or(getcontent_preh5txt=="<!DOCTYPE html")):
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
