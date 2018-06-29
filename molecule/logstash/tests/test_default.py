import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


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
