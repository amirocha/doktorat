;***************************************************************************************
; Program for calculating Tbol and Lbol with 2 methods:
; 1) Trapezodial sumation of all the data collected
; 2) Linear interpolation and trapezodial sumation of these new
; generated data. For the interpolation we use the program: "loglev.pro"
;
; The program generates the SEDs plots (saved in teh folder: "plots")
;
; Modification;10-May-2011
;***************************************************************************************


pro tbol_lbol

 ; TEK_COLOR, 0, 32
 ; device,retain=2
 ; device,true=24
 ; device,decomposed=0
  
  
  obj='CMa 58'
  file='cma58.inp'   
  file2='cma58_cont.txt'
  
  fname=strcompress('sed_'+obj+'.eps',/remove_all)
  fname2=strcompress('view_'+obj+'.eps',/remove_all)
  fname3=strcompress('values_'+obj+'.txt',/remove_all)
  
  dist=900. ;300 ;429.; Ced178.0 ; L483 200.0; RNO91 125. ;L723 300.;HH46 450. ;IRAS15 130.  ; Ced 178.0
   
 
 ;-------------------------------------------------------
  sou=obj  ;strpos(file,"-frec_fl_1.1.txt")
  ;sou=strpos(file,"-frec_fl.txt")
;  source=strmid(file, 0, sou)

  minii=1.0                     ;for the interpolation, keep it always 1
  mini=1.0

  temp=string(mini)
  tm=strpos(temp, ".0000")
  mimm=STRTRIM(strmid(temp, 0, tm),2)
  print, mimm

;  file_out='values'+mimm+'.txt'
 ; print, ;file_out

;-------------------------------------------------------


  readcol, file, wl, fl
  readcol, file2, wpacs, fpacs1,fpacs2
  
 ; print, fpacs2
  

; wl = wavelength in microns
; fl = flux in mJy  ;;; in Jy? AK


  w=0 & s=0
  w=wl
  s=fl/1000.
  num=n_elements(w)
  integral=tsum(2.9979d14/w[(num-1)-findgen(num)],s[(num-1)-findgen(num)]*1.0d-26)

  
  tbol=1.25e-11*tsum(2.9979d14/w[(num-1)-findgen(num)],s[(num-1)-findgen(num)]*1.0d-26 * (2.9979d14/w[(num-1)-findgen(num)]))/integral

  lum=integral*4.0*!Pi*(dist*3.0857d16)^2/3.86d26
  help, tbol, lum
  
 
  

;------interpolation-----------------------------------
  fl=1000.*fl ;Because in the previous program the fl is in Jy, not mJy
  w=0 & s=0

; You need to interpolate the SED. Depending on the sample - either a regular interpolation or spline is preferable
; Also check that the min/max value over which you interpolate is ok 

  w=loglev(minl=minii,maxl=4.0e3,nlev=200)
  s=10.0^interpol(alog10(fl/1.0e3),alog10(wl),alog10(w)) ;,/spline)
  
  num=n_elements(w)
  integral=tsum(2.9979d14/w[(num-1)-findgen(num)],s[(num-1)-findgen(num)]*1.0d-26)


  tbolin=1.25e-11*tsum(2.9979d14/w[(num-1)-findgen(num)],s[(num-1)-findgen(num)]*1.0d-26 * (2.9979d14/w[(num-1)-findgen(num)]))/integral

  lumin=integral*4.0*!Pi*(dist*3.0857d16)^2/3.86d26
  help, tbolin, lumin

  cgplot, w, s, /xlog, /ylog, xtit='!4k!3 (!4l!3m)', ytit='Flux (Jy)' ;, xrange=[]
  cgplot, wl, fl/1000., psym=1,/overplot

;------calculate Lsubmm-----------------------------------
;  w=loglev(minl=350,maxl=3.0e3,nlev=200)
;  s=10.0^interpol(alog10(fl/1.0e3),alog10(wl),alog10(w)) ;,/spline)
  
;  num=n_elements(w)
;  integral=tsum(2.9979d14/w[(num-1)-findgen(num)],s[(num-1)-findgen(num)]*1.0d-26);

;  lumsub=integral*4.0*!Pi*(dist*3.0857d16)^2/3.86d26
;  print, 'Lsubmm', lumsub
  
;  lumlum=100*lumsub/lum
;  print, 'Lsubmm/Lbol', lumlum
; print, 'Lsubmm/Lbol in %', lumlum
;---------------------------------


;-------------------------------------------------------
  openw, 2, fname3
  printf, 2, dist,lum,  tbol, lumin,  tbolin, format='(i4, 2x,f8.3, 2x, f6.2, 2x,f8.3,2x, f6.2)'
  close, 2
 ;------------------------------------------------------- 
  
!x.thick=6.0
!y.thick=6.0
nth=3
!P.THICK=nth
!P.CHARTHICK=4
!P.CHARSIZE=2.0
!P.TICKLEN=0.03
  
  xname=['!17 10!U0!N','10!U1!N','10!U2!N','10!U3!N','!17 10!U4!N']
  yname=['!17 10!U-4!N','!17 10!U-2!N','!17 10!U0!N','!17 10!U2!N']
  

;;  lumi=strmid(STRTRIM(string(lum),1), 0, 4)
 ;; tbolo=strmid(STRTRIM(string(tbol),1), 0, 2)

  lumi=string(round(lum),format='(f4.1)')
  tbolo=string(round(tbol),format='(i3)')
  
   
  ;lumlumi=string(round(lumlum2*10.)/10.,format='(f3.1)')+'%'
  
  set_plot,'ps'
  device,filename=fname, /encapsulated, /color,$
        /landscape, xsize=25.5, ysize=18.3, xoffset=1.0, yoffset=27.0 & $
  
  cgplot, wl, fl/1000., /xlog, /ylog, xtit='!17 !4k!3 !17(!4l!3m!17)', ytit='!18F!D!4k!3!N!17 (Jy)',$
  	position=[0.2,0.2,0.9,0.9],/xst,/yst,xminor=10,yminor=10,thick=4,symsize=2.0,$
  	xr=[0.6,1000],yr=[1d-2,1d5],psym=cgsymcat(3),xtickname=xname;,ytickname=yname
  
  cgplot,wl, fl/1000.,symsize=2.0,psym=cgsymcat(16),color='orange red',/overplot
  cgplot,wl, fl/1000.,symsize=2.0,psym=cgsymcat(9),color='black',/overplot
  
;  cgplot,wpacs,fpacs2,symsize=2.0,psym=cgsymcat(16),color='royal blue',/overplot
;  cgplot,wpacs,fpacs2,symsize=2.0,psym=cgsymcat(9),color='black',/overplot
  
  
;  cgplot,  w, s, psym=1,/overplot

  cgtext,1,7d1,obj,charthick=5,charsize=2.5

  cgtext, 1d2, 1d-2, '!18L!17!Dbol!N='+lumi, charsize=2;
  cgtext, 1d2, 1d-3, '!18T!17!Dbol!N='+tbolo, charsize=2;, 
 ; cgtext, 1d2, 1d-4, '!18L!17!Dsubm!N/!18L!17!Dbol!N='+lumlumi, charsize=2

  device,/close
  set_plot,'x'

  set_plot,'ps'
  device,filename=fname2, /encapsulated, /color
  cgplot, wl, fl/1000.*1.0d-26*2.9979d14/wl, /xlog, /ylog, xtit='!17 !4k!3 !17(!4l!3m!17)', ytit='!17 !4k!3 !18F!D!4k!3!N!17 (W m!u-2!n)',$
     position=[0.2,0.2,0.9,0.9],/xst,/yst,xminor=10,yminor=10,thick=4,symsize=2.0,$
  	xr=[0.6,1000],yr=[1d-14,1d-09],psym=cgsymcat(3),xtickname=xname
  	
  cgplot,wl, fl/1000.*1.0d-26*2.9979d14/wl,symsize=2.0,psym=cgsymcat(16),color='orange red',/overplot
  cgplot,wl, fl/1000.*1.0d-26*2.9979d14/wl,symsize=2.0,psym=cgsymcat(9),color='black',/overplot
  
;  cgplot,wpacs,fpacs2*1.0d-26*2.9979d14/wpacs,symsize=2.0,psym=cgsymcat(16),color='royal blue',/overplot
;  cgplot,wpacs,fpacs2*1.0d-26*2.9979d14/wpacs,symsize=2.0,psym=cgsymcat(9),color='black',/overplot

  cgtext,1,2d-13,obj,charthick=5,charsize=2.5

  cgtext, 4d1, 8d-13, '!18L!17!Dbol!N='+lumi, charsize=2;, format='(f5.1)'
  cgtext, 4d1, 2d-13, '!18T!17!Dbol!N='+tbolo, charsize=2;, format='(I4)'
 ; cgtext, 4d1, 6d-16, '!18L!17!Dsubm!N/!18L!17!Dbol!N='+lumlumi, charsize=2

     
  ;oplot, wl, fl/1000.*1.0d-26*2.9979d14/wl, psym=1
  
  
  device,/close
  set_plot,'x'
  
  
 
 ; stop
END
