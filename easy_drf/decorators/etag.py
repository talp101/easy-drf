import functools
import hashlib
from rest_framework import status
from rest_framework.response import Response

def etag(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        response = f(*args, **kwargs)
        etag_value = hashlib.sha1(unicode(response.data)).hexdigest()
        if_none_match_header = args[1].META.get('HTTP_IF_NONE_MATCH', None)
        if if_none_match_header:
            if_none_match_header = if_none_match_header.replace('"', '')
            if if_none_match_header == etag_value:
                return Response(status=status.HTTP_304_NOT_MODIFIED)
        return Response(data=response.data, status=status.HTTP_200_OK, headers={'ETag': etag_value})
    return wrapped
