import phonenumbers

phonenumber = input("Enter Phone Number with country code, eg. +263712345678 :")

from phonenumbers import geocoder
country = phonenumbers.parse(phonenumber, "CH")
print("Country :", geocoder.description_for_number(country,"en"))

from phonenumbers import carrier
service_provider = phonenumbers.parse(phonenumber, "RO")
print("Service Provider :", carrier.name_for_number(service_provider, "en"))

#add a tkinder gui