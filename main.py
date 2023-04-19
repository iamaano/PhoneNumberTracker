import phonenumbers
phonenumber = "+263774780783"

from phonenumbers import geocoder
country = phonenumbers.parse(phonenumber, "CH")
print("Country :", geocoder.description_for_number(country,"en"))

from phonenumbers import carrier
service_provider = phonenumbers.parse(phonenumber, "RO")
print("service Provider :", carrier.name_for_number(service_provider, "en"))