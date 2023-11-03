#!/usr/bin/python3


class LockedClass:
    keys = list(dict(LockedClass.__dict__).keys())
    if keys:
        if keys[-1] != "first_name":
            raise AttributeError('\'LockedClass\' has no attribute {}'.format(keys[-1]))
