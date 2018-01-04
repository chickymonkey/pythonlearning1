import dns.resolver
domain=input("please type a domain name: ")
ns=dns.resolver.query(domain,'NS')
for i in ns.response.answer:
    for j in i.items:
        print (j.to_text())
        