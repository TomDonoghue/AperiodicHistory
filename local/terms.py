"""Term definitions."""

####################################################################################################
####################################################################################################

# DEFINE TERMS
TERMS = [
    ['aperiodic', 'arrythmic'],
    ['1/f', '1/f-like', 'one-over f'],
]

# Define inclusion terms
INCLUSIONS = [
    'EEG', 'electroencephalography',
    'MEG', 'magnetoencephalography',
    'ECoG', 'electrocorticography',
    'iEEG', 'intracranial EEG',
    'LFP', 'local field potential',
]

# Define exclusion terms
EXCLUSIONS = [
]

# Collect terms together
ALL_TERMS = {
    'terms' : TERMS,
    'inclusions' : [INCLUSIONS] * len(TERMS),
    'exclusions' : [EXCLUSIONS] * len(TERMS),
}