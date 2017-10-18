# Write a regular expression to validate a phone number.

import re


def contact_info(d):
    match = re.search(r'^\d{10}$', d)
    if match:
        print 'valid mobile number'
    else:
        print 'invalid mobile number'

contact_info('9034561290')
contact_info('11')
