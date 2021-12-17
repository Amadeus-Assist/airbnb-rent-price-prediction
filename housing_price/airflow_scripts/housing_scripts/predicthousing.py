import sys
sys.path.append('housing_price/.')
from housing.trainhousingmodel import predicthousing

# predicthousing('nyc')
predicthousing('la')
# predicthousing('chicago')