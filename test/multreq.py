import testlib

addresses = [
    'tcp://127.0.0.1:8000',
]

with testlib.Servers(addresses) as servers:
    testlib.Client(['--push=asdf:qwer', '--push=zxcv:uiop'], addresses)
    testlib.Client(['--request=asdf', '--request=zxcv'], addresses)
