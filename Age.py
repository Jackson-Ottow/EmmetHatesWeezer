
from base64 import encode


question = int(input("Whats your age in years?"))
print("You have been alive for",(question*365), "days")
print("You have been alive for",(question/10), "decades")
print("You have been alive for",(question*52), "weeks")
print("You have been alive for",(question*365*24*60), "minutes")
