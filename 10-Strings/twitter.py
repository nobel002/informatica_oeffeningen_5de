tweet = input("Your tweet: ")
index = tweet.find('#')
while index > -1:
    index = tweet.find('#')
    tweet = tweet[index:]
    index_spatie = tweet.find(" ")
    print(tweet[0:index_spatie+1])
    tweet = tweet[index_spatie+1:]

