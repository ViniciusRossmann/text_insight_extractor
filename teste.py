## api key bUrAhK9PurmTE7xREGqogkEI4
## secrete key JTFZUK0v4VkYHDsQrd2JVQ41kf4QaWdkhyZIfGP25EZfd5C22K
## Access Token 828621726808494080-Ba34pxNYgbWBnqxwJnAqZi3HLxypJPU
## Access Token Secret RRqx3fUzsMiWELfqZcw5p90Rsls7prbA0GjYG8wnE53I9

import tweepy

# Crie um objeto da API do Twitter
auth = tweepy.OAuthHandler("bUrAhK9PurmTE7xREGqogkEI4", "JTFZUK0v4VkYHDsQrd2JVQ41kf4QaWdkhyZIfGP25EZfd5C22K")
auth.set_access_token("828621726808494080-Ba34pxNYgbWBnqxwJnAqZi3HLxypJPU", "RRqx3fUzsMiWELfqZcw5p90Rsls7prbA0GjYG8wnE53I9")
api = tweepy.API(auth)

# Defina as consultas de pesquisa
q = "futebol"

# Recupere os tweets
tweets = api.search(q)

# Imprima o texto dos tweets
for tweet in tweets:
    print(tweet.text)