
debian_os = ['debian', 'ubuntu']
rhel_os = ['redhat', 'centos']


def test_distribution(host):
    assert host.system_info.distribution.lower() in debian_os + rhel_os


def test_conf_dir(host):
    f = host.file('/etc/logstash/conf.d')

    assert f.exists
    assert f.is_directory


def test_data_dir(host):
    f = host.file('/var/lib/logstash')

    assert f.exists
    assert f.is_directory


def test_log_dir(host):
    f = host.file('/var/log/logstash')

    assert f.exists
    assert f.is_directory


def test_service(host):
    s = host.service('logstash')

    assert s.is_enabled
    assert s.is_running


def test_user(host):
    u = host.user('logstash')

    assert u.exists
    assert u.shell == '/usr/sbin/nologin'


def test_group(host):
    g = host.user('logstash')

    assert g.exists
