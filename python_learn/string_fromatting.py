import datetime

date = datetime.datetime(2023, 10, 17, 12, 00, 00)

sentence = "{:%B %d %Y}".format(date)
print(sentence)