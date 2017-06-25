def BMI(waga,wzrost):
	BMI=waga/(wzrost**2)
	print("Twoje BMI wynosi:", BMI)
waga=input("podaj wage")
wzrost=input("podaj wzrost")
BMI(int(waga),float(wzrost))