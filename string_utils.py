class StringUtils:
    @staticmethod
    def is_empty(s):
        return s is None or s == ''

    @staticmethod
    def is_blank(s):
        return s is None or s.strip() == ''

    @staticmethod
    def reverse(s):
        if s is None:
            return None
            return s[::-1]

    @staticmethod
    def to_upper(s):
        if s is None:
            return None
            return s.upper()

    @staticmethod
    def join_strings(strings, sep=','):
        if not strings:
            return None
            return sep.join(strings)
