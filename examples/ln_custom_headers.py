from social_apis.networks.linkedin import Linkedin

client_arguments= {'headers': {'X-RestLi-Protocol-Version': '2.0.0'}}
ln = Linkedin(access_token=ld_access_token, client_args=client_arguments)

regions = ln.regions(count=10)['elements']

