; pro species_file;; procedure pour creer un fichier pour chaque espece contenant; l'abondance a chaque temps pour chaque tirage a partir ; du resultat de OSU;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;aa=' 'n1=fltarr(10)ntirage=1999nspecies=474ntime=124n=dblarr(ntime)species=strarr(nspecies)s=strarr(10)tyr=dblarr(ntime)ab=dblarr(ntirage,nspecies,ntime)n2=dblarr(ntirage)densities=dblarr(ntirage)aa=' '; lire les fichiers plotxxxx.dat	for i=0,ntirage-1 do begin	char1=string(i+1,format='(i4)')	char2=strcompress('MCUP/plot'+char1+'.dat', /remove_all)		openr,1,char2	print,char2	readf,1,aa	readf,1,aa	readf,1,aa	readf,1,tyr	for k=0,nspecies-1 do begin		readf,1,format='(a10,124(d16.8))',aa,n		species(k)=strcompress(aa, /remove_all)		ab(i,k,*)=n	endfor	close,1endfor			istart=0for i=istart,nspecies-1 do begin	char3=strcompress('ab_spec/'+species(i)+'.dat', /remove_all)	;	char3='SO.dat'	print,char3	openw,1,char3	for k=0,ntime-1 do begin		n=tyr(k)		n2=ab(*,i,k)		printf,1,format='(e10.3,2499(e10.3))',n,n2	endfor	close,1endfor			end		