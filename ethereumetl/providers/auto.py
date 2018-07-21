# MIT License
#
# Copyright (c) 2018 Evgeny Medvedev, evge.medvedev@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from urllib.parse import urlparse

from web3 import IPCProvider, HTTPProvider

from ethereumetl.providers.ipc import BatchIPCProvider
from ethereumetl.providers.rpc import BatchHTTPProvider

DEFAULT_IPC_TIMEOUT = 60
DEFAULT_HTTP_REQUEST_KWARGS = {'timeout': 60}


def get_provider_from_uri(uri_string, batch=False):
    uri = urlparse(uri_string)
    if uri.scheme == 'file':
        if batch:
            return BatchIPCProvider(uri.path, timeout=DEFAULT_IPC_TIMEOUT)
        else:
            return IPCProvider(uri.path, timeout=DEFAULT_IPC_TIMEOUT)
    elif uri.scheme == 'http' or uri.scheme == 'https':
        if batch:
            return BatchHTTPProvider(uri_string, DEFAULT_HTTP_REQUEST_KWARGS)
        else:
            return HTTPProvider(uri_string, request_kwargs=DEFAULT_HTTP_REQUEST_KWARGS)
    else:
        raise ValueError('Unknown uri scheme {}'.format(uri_string))

