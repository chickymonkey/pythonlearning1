#！ /usr/bin/env python
import dns.resolver
domain = input('Please input an domain： ') #输入域名地址
# show the A records
A = dns.resolver.query( domain,'A') #指定查询类型为A记录
for i in A.response.answer: #通过response.answer方法获取查询回应信息
    for j in i.items: #遍历回应信息
        print(j.address)
# show the MX records        
MX = dns.resolver.query(domain,'MX')
for i in MX:
    print('MX preference=', i.preference, 'mail exchanger=', i.exchange)
    
# Show the NS RECORDSIZE
ns = dns.resolver.query(domain,'NS')
for i in ns.response.answer:
    for j in i.items:
        print(j.to_text())