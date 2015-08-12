# coding: utf-8

def write_konkurstext(konkurs_2013, konkurs_2014):
	diff = konkurs_2014 - konkurs_2013
	if diff < 100:
		print("Förra året gjordes %s företagskonkurser. Det var ingen nämnvärd skillnad mot året före (%s st)." % (konkurs_2014, konkurs_2013))
	elif diff < 500:
		print("En betydande ökning jämfört med föregående år, %s respektive %s konkurser") % (konkurs_2014, konkurs_2013)
	elif diff > 500:
		print("Vilket sjukt stor diff. Kolla dina siffror en gång till.")	

write_konkurstext(6563, 6960)


# if pop2013 > pop2012:
#	print("Befolkningen i vårt land växte ifjol")
# else:
#	print("Oj, vad få vi har blivit")