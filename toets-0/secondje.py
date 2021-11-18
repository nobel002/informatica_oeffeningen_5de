seconden = int(input("Seconden = "))

dagen = seconden // 86400  # Seconds in a day
seconden %= 86400
uren = seconden // 3600
seconden %= 3600
minuten = seconden // 60
seconden %= 60

print("{:d}d {:d}:{:d}:{:d}".format(dagen, uren, minuten, seconden))
