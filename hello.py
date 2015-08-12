#coding: utf-8

first_name = "Peter"
age = 42


text = "Hej jag heter %s och är %s år gammal." % (first_name, age)

#print(text)

first_name = "Gustaf"
last_name = "Fridolin"
domain = "riksdagen.se"
email2 = "%s.%s@%s" % (first_name, last_name, domain)

email = first_name + "." + last_name + "@" + domain
print(email2)

