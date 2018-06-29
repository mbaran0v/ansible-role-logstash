
logstash_major_version = "6.x"
debian_os = ['debian', 'ubuntu']
rhel_os = ['redhat', 'centos']


def test_distribution(host):
    assert host.system_info.distribution.lower() in debian_os + rhel_os


def test_repo_pinning_file(host):
    if host.system_info.distribution.lower() in rhel_os:
        f = host.file('/etc/yum.repos.d/'
                      'elasticsearch-{}.repo'.format(logstash_major_version))
    if host.system_info.distribution.lower() in debian_os:
        f = host.file('/etc/apt/sources.list.d/'
                      'elasticsearch-{}.list'.format(logstash_major_version))

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_config(host):
    f = host.file('/etc/logstash/logstash.yml')

    assert f.exists


def test_socket(host):
    s = host.socket('tcp://:::5044')
    print(host.socket.get_listening_sockets())

    assert s.is_listening


def test_serice(host):
    s = host.service('logstash')

    assert s.is_enabled
    assert s.is_running
