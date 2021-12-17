import sys
sys.path.append('housing_price/.')
from covid.traincovidmodel import predictcovid

predictcovid('nyc')
predictcovid('la')
predictcovid('chicago')