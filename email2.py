# coding: utf-8

name = "Stefan Löven"
domain = "riksdagen.se"
email = name.lower().replace("ö","o").replace(" ",".") + "@" + domain

print(email)


#LEOS LÖSNING

name = "Stefan Löven"
domain = "riksdagen.se"
email = ""

email_prefix = name.lower()
email_prefix = email_prefix.replace("ö", "o").replace(" ", ".")

email = email_prefix + "@" + domain


print(email)