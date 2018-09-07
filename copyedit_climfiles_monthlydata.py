import datetime
print "module load ncarg"
print "module load cdo"
print "module load nco"

years = range(1979,2017)
#clim 
vars=['u','v','t','z']
#vars=['z']

for var in vars:
 for y in years:
#clim   
   filein="erai_"+var+"_clim_"+str(y)+".nc"
#   filein="erai_"+var+"_mon_"+str(y)+".nc"
   print 'ncatted -a units,time,o,c,"hours since 1899-12-15 00:00:00" '+filein
