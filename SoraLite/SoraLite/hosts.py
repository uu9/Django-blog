from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'api', 'SoraApi.urls', name='api'),
    host(r'', 'SoraMain.urls', name='main'),
)