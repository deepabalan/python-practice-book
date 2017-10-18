# Write a function make_slug that takes a name converts it into slug.
# A slug is a string where spaces and special characters are replaced
# by a hyphen, typically used to create blog post URL from post titlie.
# It should also make sure there are no more then one hyphen in any
# place and there are no hypehens at teh beginning and end of the slug.

import re


def make_slug(s):
    return '-'.join(re.findall('\w+', s))

print make_slug("hello world")
print make_slug("hello world!")
print make_slug("--hello- world--")
