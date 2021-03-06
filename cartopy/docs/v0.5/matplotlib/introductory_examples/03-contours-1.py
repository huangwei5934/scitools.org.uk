import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.examples.waves import sample_data

ax = plt.axes(projection=ccrs.Robinson())

ax.set_global()

lons, lats, data = sample_data(shape=(20, 40))

plt.contourf(lons, lats, data, transform=ccrs.PlateCarree())

ax.coastlines()
ax.gridlines()

plt.show()