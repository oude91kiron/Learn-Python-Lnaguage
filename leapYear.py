
def leapYear(year):
	if year % 4 == 0 :
		return True
		if year % 100 == 0 :
			return False
			if year % 400 == 0 :
				return True
	return False


def allYear(year):
	x = "please ask me about year less than 2018"
	while year < 2018 :	
		print year , leapYear(year)
		year += 1
        return x



print allYear()


# 22-04-571 