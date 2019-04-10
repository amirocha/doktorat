Function loglev,minl=minl,maxl=maxl,nlev=nlev

if not(keyword_set(nlev)) then nlev=60

loglev=(10.^((alog10(maxl)-alog10(minl))*(findgen(nlev)/(nlev-1))))*minl

return,loglev

END
