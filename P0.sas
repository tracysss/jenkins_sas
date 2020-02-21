libname  inlib 'C:\Users\trsong\Documents\SGF2020\Programs\input';
libname  outlib 'C:\Users\trsong\Documents\SGF2020\Programs\output';

data outlib.output;
	informat date $10. number 8. value1 8. value2 8.;
	INPUT date number value1 value2;
	total = value1 + value2;
	datalines;
01/01/2020       1     100     110
01/02/2020       2     100     150
01/03/2020       3     120      80
;
    
run;
