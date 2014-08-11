#!/usr/bin/env python -u
# coding:utf-8

import re

try:
    import simplejson as json
except:
    import json

log_file = open('/var/log/apache2/access_log', 'r')

# matches uuid format *at the end* of the log
log_re = re.compile(r'.*web-ab-example/(signup\.html)?\?group=([a-zA-Z]).* ([a-f0-9]*-[a-f0-9]*-[a-f0-9]*-[a-f0-9]*-[a-f0-9]*)$')

# The information is stored in dicts so we can consider only one fail/success per userid
# in a SQL database that would be equivalent of GROUP BY userid selecting COUNT(click) > 1
groupA = {}
groupB = {}

for line in log_file:
    match = log_re.match(line)
    if match:
        click = match.group(1) is not None
        userid = match.group(3)

        if match.group(2) == "A":
            group = groupA
        else:
            group = groupB

        if click:
            group[userid] = 1
        elif userid not in group:
            group[userid] = 0


print "The following input can be used in the stats functions that we in the stats/ directory"
print "Group A:", json.dumps(groupA.values())
print "Group B:", json.dumps(groupB.values())
