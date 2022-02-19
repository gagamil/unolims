import string

# https://www.agilent.com/cs/library/brochures/Brochure_Guide%20to%20QPCR_IN70200C.pdf
# https://portlandpress.com/biochemist/article/42/3/48/225280/A-beginner-s-guide-to-RT-PCR-qPCR-and-RT-qPCR
# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5129434/
# https://www.gene-quantification.de/national-measurement-system-qpcr-guide.pdf
# https://tools.thermofisher.com/content/sfs/manuals/MAN0010409_QuantStudio_CLA_UG.pdf

RUN_METHOD__SALIVECLEAR = 'RUN_METHOD__SALIVECLEAR'
RUN_METHOD__SALIVADIRECT = 'RUN_METHOD__SALIVADIRECT'
RUN_TARGET_MS2 = 'MS2'
RUN_TARGET_N = 'N gene'
RUN_TARGET_RP = 'RP'
RUN_TARGET_ORF1AB = 'ORF1ab'
RUN_METHOD_TARGETS__SALIVECLEAR = [RUN_TARGET_MS2, RUN_TARGET_N, RUN_TARGET_RP]
RUN_METHOD_TARGETS__SALIVADIRECT = [RUN_TARGET_MS2, RUN_TARGET_ORF1AB, RUN_TARGET_RP]
RUN_PROBE__HEX = 'HEX'
RUN_PROBE__CY5 = 'Cy5'
RUN_PROBE__FAM = 'FAM'
RUN_PROBE__ROX = 'ROX'

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
RUN_WELLPLATE__384_LAYOUT = {'rows':['A','P'], 'cols':'1-24', 'well_count':384}

RUN_WELLPLATE__96 = 'RUN_WELLPLATE__384'
RUN_WELLPLATE__96_LAYOUT = {'rows':['A','H'], 'cols':'1-12', 'well_count':96}

RUN_WELLPLATE__CONFIGS = [
                            {'name':RUN_WELLPLATE__384, 'layout':RUN_WELLPLATE__384_LAYOUT}, 
                            {'name':RUN_WELLPLATE__96, 'layout':RUN_WELLPLATE__96_LAYOUT}
                        ]