from IPy import IP
IP_version1=IP('10.0.0.0/8')
IP_version2=IP("::1").version()
# print(IP_version1,IP_version2)
print( IP('192.168.1.0').make_net('255.255.255.0'))
contain='192.168.1.10' in IP('192.168.1.0/24')
print(contain)
over_laps=IP('192.168.0.0/23').overlaps('192.168.1.0/24')
print(over_laps)

print('net： %s' % IP_version1.net() ) #输出网络地址
print('netmask： %s' % IP_version1.netmask() ) #输出网络掩码地址
print('broadcast： %s' % IP_version1.broadcast() )