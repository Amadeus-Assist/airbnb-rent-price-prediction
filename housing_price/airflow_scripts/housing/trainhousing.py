import sys
sys.path.append('housing_price/.')
from housing.trainhousingmodel import trainhousing

# trainhousing('nyc')
trainhousing('la')
# trainhousing('chicago')