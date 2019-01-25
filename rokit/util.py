def pass_tag(str):
    return '[\033[32mPASS\033[0m]%s' % str


def fail_tag(str):
    return '[\033[31mFAIL\033[0m]%s' % str


def highlight(str):
    return '\033[32m[%s]\033[0m' % str
