# coding: utf-8

name = "Stefan Löven"
domain = "riksdagen.se"
email = ""

def emailify(name,domain):
	email_prefix = name.lower()
	email_prefix = email_prefix.replace("ö", "o")
	email_prefix = email_prefix.replace("Ö", "o")
	email_prefix = email_prefix.replace("é", "e")
	email_prefix = email_prefix.replace("å", "a")
	email_prefix = email_prefix.replace("ä", "a")
	email_prefix = email_prefix.replace(" ", ".")
	email = email_prefix + "@" + domain
	print(email)

emailify("John Henry", "livet.se")

