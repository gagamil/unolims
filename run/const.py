import string


RUN_METHOD__SALIVECLEAR = 'RUN_METHOD__SALIVECLEAR'
RUN_METHOD__SALIVADIRECT = 'RUN_METHOD__SALIVADIRECT'
RUN_METHOD_TARGETS__SALIVECLEAR = ['MS2', 'RP', 'SMTHNG']
RUN_METHOD_TARGETS__SALIVADIRECT = ['AAA', 'ABC', 'XYZ']

RUN_REPLICATION__DUPLICATE = 'RUN_REPLICATION__DUPLICATE'
RUN_REPLICATION__TRIPLICATE = 'RUN_REPLICATION__TRIPLICATE'
RUN_REPLICATION__DUPLICATE__PATTERN = [
                                            ['X','X']
                                        ]
RUN_REPLICATION__TRIPLICATE__PATTERN = [
                                            ['X','X'], 
                                            ['', 'X']
                                        ]

# WELL PLATES
ALPHABET = list(string.ascii_uppercase)
# https://www.thermofisher.com/ru/ru/home/brands/thermo-scientific/molecular-biology/thermo-scientific-pcr/thermo-scientific-plastics-consumables/qpcr-white-plates.html
RUN_WELLPLATE__384 = 'RUN_WELLPLATE__384'
RUN_WELLPLATE__384_LAYOUT = {'rows':'A-P', 'cols':'1-24'}

RUN_WELLPLATE__96 = 'RUN_WELLPLATE__384'
RUN_WELLPLATE__96_LAYOUT = {'rows':'A-H', 'cols':'1-12'}