# From stephen.sharma@wa.yh.oh Sat Jan 5 09:04:2026 2008
#iss email mei find kro ki mail kya hai aur mail ka host kon hai

data='From stephen.sharma@wa.yh.oh Sat Jan 5 09:04:2026 2008'
# atpos=data.find('@')
# print(atpos)

# aa=data.find(' ',atpos)
# print(aa)

word = data.split()
email = word[1]
print(email)