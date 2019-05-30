# Ansible role: Logstash

[![Build Status](https://travis-ci.org/mbaran0v/ansible-role-logstash.svg?branch=master)](https://travis-ci.org/mbaran0v/ansible-role-logstash) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![GitHub tag](https://img.shields.io/github/tag/mbaran0v/ansible-role-logstash.svg)](https://github.com/mbaran0v/ansible-role-logstash/tags/) [![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

**THIS ROLE IS FOR 7.x, 6.x, 5.x.**

Ansible role for 7.x/6.x/5.x [Logstash](https://www.elastic.co/products/logstash). Currently this works on Debian and RedHat based linux systems. Tested platforms are:

* Ubuntu 16.04
* CentOS 7

Requirements
------------

Requires Java; recommended role for Java installation: [geerlingguy.java](https://github.com/geerlingguy/ansible-role-java)


Role Variables
--------------

The variables that can be passed to this role and a brief description about them are as follows. (For all variables, take a look at defaults/main.yml)

```yaml
# logstash version
logstash_major_version: "6.x"
logstash_version: "6.3.0"

# input configuration
logstash_inputs: |
  beats {
    port => 5044
  }

# filter configuration
logstash_filters: |
  mutate {
    rename => { "version" => "service_version" }
    gsub => ["data", "=>", ":"]
    gsub => ["data", "nil", "None"]
  }

# output configuration
logstash_outputs: |
  if "nginx" in [tags] {
    elasticsearch {
      hosts => "127.0.0.1:9200"
      index => "nginx-%{+YYYY.MM.dd}"
    }
  }
  stdout { codec => rubydebug }

```

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- hosts: logstash
  roles:
      - role: mbaran0v.logstash
```

License
-------

MIT / BSD

Author Information
------------------

This role was created in 2018 by Maxim Baranov.
