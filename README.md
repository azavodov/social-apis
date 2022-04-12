# Social APIs

`Social APIs` is a Python library providing an easy way to access Social Networks API. 

This library was designed to explore the possibility of a unified integrations with multiple social networks, without an intermediate layer. 

This is an attempt to combine several social networks SDKs into one library and generalize their use.

## Features

- Build flexible requests to following social networks APIs: *Facebook, LinkedId, Twitter v1/v2, VK*
- Use build-in methods with documentation links
- Build your query flexibly with arguments mapping
- Use the basic request method if you do not find the desired function
- OAuth 1/2 support
- Fully Python 3 support (python 2 not support at the moment)

## Installation

Install Social APIs via pip:

```bash
$ pip install social-apis
```

Or, if you want the code that is currently on GitHub:

```bash
git clone https://github.com/azavodov/social-apis
cd social-apis
python setup.py install
```

## Get started

First, you must register the application and get access keys for requests. This is a common step for any social network.

After you register, copy the credentials, we won't need them. This can be an **access_token** in case of Oauth 2 authorization, 

or a combination of **token** and **token secret** in the case of Oauth 1 authorization.

Then, you'll want to import some social networks. Facebook for example:

```python
from social_apis.networks.facebook import Facebook 
```

Next, initialize one of the api classes. To do this, transfer any credentials, supported by this social network. 

The authorization method will be recognized automatically depending on the passed parameters.

```python
access_token = "<< FACEBOOK_ACCESS_TOKEN >>"
facebook_api = Facebook(access_token=access_token) 
```

Cool! Now you can call methods and build requests!

-----------

## Examples

Oauth 1.0 – Twitter authentication
```python
import os
from social_apis.networks.twitter import Twitter

app_key = os.environ.get("TWITTER_APP_KEY")
app_secret = os.environ.get("TWITTER_APP_SECRET")
oauth_token = os.environ.get("TWITTER_TOKEN")
oauth_token_secret = os.environ.get("TWITTER_TOKEN_SECRET")

twitter_api = Twitter(
    app_key=app_key, 
    app_secret=app_secret, 
    oauth_token=oauth_token, 
    oauth_token_secret=oauth_token_secret
)
```

Use the build-in method without arguments

```python
from social_apis.networks.vkontakte import Vkontakte

vk_api = Vkontakte(access_token="<< VK_ACCESS_TOKEN >>")
settings = vk_api.account_get_push_settings()
```

Use the build-in method with arguments mapping

```python
from social_apis.networks.vkontakte import Vkontakte

vk_api = Vkontakte(access_token="<< VK_ACCESS_TOKEN >>")
users = vk_api.users_search(q="Ivan Ivanov", count=7)
```

Use the GET request method with custom endpoint and params

```python
from social_apis.networks.facebook import Facebook

facebook_api = Facebook(access_token="<< FACEBOOK_ACCESS_TOKEN >>")
endpoint = facebook_api.url + "/posts/search"
response = facebook_api.get(endpoint, params={'q': 'github'}) 
```


## Dynamic Function Arguments

Keyword arguments of functions are mapped to the functions available for each endpoint in any APIs docs. 
Doing this allows you to be really flexible in querying the API, so changes to the API aren't held up from you using them by this library.

## Questions, Comments, etc?

If you have any questions, you can contact me through the following social networks:

- Instagram: [@\_zavodov\_](https://instagram.com/_zavodov_)
- Telegram: [@zavodov](https://t.me/zavodov)

## Special Thanks

During the development process, following SDKs and projects were studied and helped me a lot with library features and structure!

[twython](https://github.com/ryanmcgrath/twython), 
[python-facebook-api](https://github.com/sns-sdks/python-facebook), 
[vk_api](https://github.com/python273/vk_api)

Thank you a lot! 

## Want to help?

There are many plans for the development of this library. 

However, if you would like to help or contribute, any pull requests, advices or discussions are most welcome.