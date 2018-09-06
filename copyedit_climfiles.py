import datetime
print "module load ncarg"
print "module load cdo"

years = range(1979,2017)
vars=['u','v','t','z']

for var in vars:
 for y in years:
  for m in range(1,13):
   mm=str(m).zfill(2)
   d=31
   if (m==4) | (m==6) | (m==9) | (m==11):
    d=30
   elif (y%4==0) & (m==2):
    d=29
   elif (m==2):
    d=28
   hh1=(datetime.date(y,m,d)-datetime.date(1900,1,1)).days*24+21
   filein="erai_"+var+"_clim.nc"
   print "cdo -O selsmon,"+mm+" "+filein+" rub.nc"
   fileout="erai_"+var+"_clim_"+str(y)+".nc"
   print "ncl 'timed="+str(hh1)+"'"+" "+"'"+"file_in="+'"'+"rub.nc"+'"'+"' edit_time.ncl"
   print "mv rub.nc "+mm+".nc"
  print "cdo -O mergetime ??.nc "+fileout
  print "rm -f ??.nc"
#  print "ncpdq -O -U rub.nc "+mm+".nc"
# print "ncrcat ??.nc air_mon_"+str(y)+".nc"
