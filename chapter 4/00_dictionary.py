#syntax:
marks={
    "sneha":100,
    "sneh":90,
    "sne":80
}
print(type(marks))
print(marks["sneh"])


# agar yha pr bina 3 ke print kre toh dono 100 denge
# but agr rakhe toh get wala none print krega nd dusre wala error show krega
print(marks.get("sneha"))
print(marks["sneha"])

# dict methods

# Consider the following dictionary. 
# a={"name":"harry" 
# "from":"india" 
# "marks":[92,98,96]} 


# • a.items(): Returns a list of (key,value)tuples. 

# • a.keys(): Returns a list containing dictionary's keys. 

# • a.update({"friends":}): Updates the dictionary with supplied key-value pairs. 

# • a.get("name"): Returns the value of the specified keys (and value is returned 

# eg.
# "harry" is returned here). 
