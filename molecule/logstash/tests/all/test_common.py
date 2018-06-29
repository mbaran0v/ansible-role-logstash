
debian_os = ['debian', 'ubuntu']
rhel_os = ['redhat', 'centos']


def test_distribution(host):
    assert host.system_info.distribution.lower() in debian_os + rhel_os


def test_repo_pinning_file(host):
    if host.system_info.distribution.lower() in debian_os:
        f = host.file('/etc/yum.repos.d/elasticsearch-{{ logstash_major_version }}.repo')
    if host.system_info.distribution.lower() in rhel_os:
        f = host.file('/etc/yum.repos.d/elasticsearch-6.x.repo')
        
        assert f.exists
        assert f.user == 'root'
        assert f.group == 'root'


def test_logstash_config(host):
    f = host.file('/etc/logstash/logstash.yml')

    assert f.exists


def test_logstash_socket(host):
    s = host.socket('tcp://:::5044')

    assert s.is_listening


def test_logstash_serice(host):
    s = host.service('logstash')

    assert s.is_enabled
    assert s.is_running
