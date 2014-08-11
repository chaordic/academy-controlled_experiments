#!/usr/bin/env python -u
# coding:utf-8

import re

log_file = open('/var/log/apache2/access_log', 'r')

# matches uuid format *at the end* of the log
log_re = re.compile(r'.*web-ab-example/(signup\.html)?\?group=([a-zA-Z]).* ([a-f0-9]*-[a-f0-9]*-[a-f0-9]*-[a-f0-9]*-[a-f0-9]*)$')

for line in log_file:
    match = log_re.match(line)
    if match:
        print match.groups()
