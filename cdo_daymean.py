print "module load cdo"

years = range(1979,2016)
vars=['z']

for var in vars:
 for y in years:
   print "cdo -O daymean erai_"+var+"_6hr_"+str(y)+".nc erai_"+var+"_day_"+str(y)+".nc"
