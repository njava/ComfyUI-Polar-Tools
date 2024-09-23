NAMESPACE = 'polar'


def get_name(name):
    return '{}🐻‍❄️'.format(name)


def get_category(sub_dirs=None):
    if sub_dirs is None:
        return NAMESPACE
    else:
        return "{}/utils".format(NAMESPACE)
