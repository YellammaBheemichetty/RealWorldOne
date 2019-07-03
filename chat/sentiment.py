from aylienapiclient import textapi

client = textapi.Client("6d16141f", "4a5b60ce5640876e044221e8b9aa629e")
text = input()
sentiment = client.Sentiment({'text': text})
if sentiment['polarity'] == 'negative':
    print(":(")
elif sentiment['polarity'] == 'positive':
    print(":)")
else:
    print(":|")

