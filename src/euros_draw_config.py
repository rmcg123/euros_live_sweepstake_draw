"""Configuration file for making euros sweepstake draw"""

# EURO 2024 qualified countries, ordered by odds from shortest to longest.
QUALIFIED_COUNTRIES = [
    'England',
    'France',
    'Germany',
    'Portugal',
    'Spain',
    'Italy',
    'Netherlands',
    'Belgium',
    'Croatia',
    'Denmark',
    'Switzerland',
    'Austria',
    'Turkey',
    'Serbia',
    'Ukraine',
    'Hungary',
    'Czech Republic',
    'Scotland',
    'Poland',
    'Romania',
    'Slovakia',
    'Slovenia',
    'Georgia',
    'Albania'
]

N_SWEEP_ENTRANTS = 12
SWEEP_ENTRANTS = list(range(N_SWEEP_ENTRANTS))

POT_1_TEAMS = QUALIFIED_COUNTRIES[:N_SWEEP_ENTRANTS]
POT_2_TEAMS = QUALIFIED_COUNTRIES[N_SWEEP_ENTRANTS:]
