line_length_blacklist = ['.am', '.at', 'etc', '.in', '.m4', '.mk', '.patch',
                         '.py']
leading_whitespace_blacklist = ['.mk', '.am', '.at']
     'match_name':
     lambda x: not any([fmt in x for fmt in line_length_blacklist]),
     'check': lambda x: line_length_check(x),
     'print': lambda: print_warning("Line length is >79-characters long")},
     'match_name':
     lambda x: not any([fmt in x for fmt in leading_whitespace_blacklist]),
    return lambda x: regex.search(x) is not None
    [re.escape(op) for op in ['/', '%', '<<', '>>', '<=', '>=', '==', '!=',
       '[^" +(]\+[^"+;]', '[^" -(]-[^"->;]', '[^" <>=!^|+\-*/%&]=[^"=]']
            check['print']()
            parse = 2
        if parse == 1:
                parse = parse + 1
        elif parse == 0:
                parse = parse + 1
        elif parse == 2:
        optlist, args = getopt.getopt(args, 'bhlstf',
                                       "skip-trailing-whitespace"])