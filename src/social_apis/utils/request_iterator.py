from urllib.parse import parse_qsl, urlsplit

from social_apis.exceptions.social_api_error import *


def iterator(api_method, return_pages=False, **params):
    r"""Returns a generator for results of specific supported method.
    Usage::
      >>> from social_apis.networks.facebook import Facebook
      >>> facebook = Facebook(access_token="<<access_token>>")

      >>> response = iterator(facebook.search, q='python')
      >>> for item in response:
      >>>     print (item)
    """

    if not callable(api_method):
        raise TypeError('iterator() takes a Network function as its first argument.')

    if not hasattr(api_method, 'iter_key') or not hasattr(api_method, 'iter_field'):
        raise IteratorError(f'Unable to create generator for method "{api_method.__name__}"')

    iter_key = api_method.iter_key
    iter_field = api_method.iter_field
    iter_next = api_method.iter_next if hasattr(api_method, 'iter_next') else iter_field
    iter_mode = api_method.iter_mode if hasattr(api_method, 'iter_mode') else 'cursor'

    while True:
        content = api_method(**params)

        if not content:
            return
        results = get_field(content, iter_key)

        if return_pages:
            yield results
        else:
            for result in results:
                yield result

        try:
            next_field = get_field(content, iter_next)
            if str(next_field).lower() in ['none', 'null', '0', '[]', '{}', '']:
                return
            if iter_mode == 'cursor':
                params[iter_field] = next_field
            elif iter_mode == 'offset':
                params[iter_field] = int(params[iter_field]) + 10 if iter_field in params else 0
        except (TypeError, ValueError):
            raise IteratorError('Unable to generate next page of search results, `page` is not a number.')
        except (KeyError, AttributeError):
            raise IteratorError('Unable to generate next page of search results, content has unexpected structure.')


def get_field(content, field, raise_error=False):
    r"""
        Returns a 'field' (str) of 'content' (dict).
        Split 'field' by dots and iterate 'content' by them.
        Return None if field not in content. Raise error if raise_error=True
    """
    fields = field.split('.')
    result = content
    for f in fields:
        if f in result:
            result = result.get(f)
        else:
            if raise_error:
                raise KeyError("Content has unexpected structure.")
            else:
                result = None
                break
    return result
