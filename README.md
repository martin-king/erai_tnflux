# erai_tnflux

General steps.
1. Download 6 hourly nc data for u, v, t, z.
2. Create monthly means of u, v, t, z with cdo_monmean.py, cdo mergetime them to single files. (eg. erai_u_mon_1979.nc, erai_u_mon_1979_2015.nc)
3. Create climatologies of u, v, t, z with, e.g.,
cdo ymonmean erai_u_mon_1979_2015.nc erai_u_clim.nc.
4. Copy these climatologies files to other years with proper dates using copyedit_climfiles.py. (eg. erai_u_clim_1979.nc)
note: 16 Oct 2017 Did until step 4, because only to do on monthly data.
5. Create daily means of z with cdo_daymean.py. (eg. erai_z_day_1979.nc)
6. Create the daily px, py, pz, div, psiaa files with calc_tnflux.gs, use RUN_GRADS.sh to submit to batch.
7. Use cdo_mergeday.py to merge the files from step 6 to erai_tnflux_day_????.nc.
8. Use cdo_monmean2.py to create erain_tnflux_mon_????.nc, then cdo mergetime to merge the resulting files to erai_tnflux_mon_1979_2015.nc
