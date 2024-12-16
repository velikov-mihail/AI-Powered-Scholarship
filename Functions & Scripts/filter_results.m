%%

clear
clc

load results
 
clc

stockFilter = 30;
t_cutoff = 1.96;
cmonth_cutoff = 360;
emonth_cutoff = 202312;


% Step 1: Quintile, NYSE-breaks, EW
res = results(results.stockFilter == stockFilter & ...
               results.nPtfs==5 & ...
               ismember(results.breaks, {'NYSE'}) & ...
               ismember(results.weighting, 'equal'),{'numer','denom','signal','rdndntFlag','txret','tnetret'});

% Step 2: Decile, NYSE-breaks, VW
step2 = results(results.stockFilter == stockFilter & ...
               results.nPtfs==10 & ...
               ismember(results.breaks, {'NYSE'}) & ...
               ismember(results.weighting, 'value'),{'numer','denom','signal','txret','tnetret','endDate','consecutiveDates'});
step2.Properties.VariableNames = {'numer','denom','signal','txret2','tnetret2','endDate2','consecutiveDates2'};
res = outerjoin(res, step2, 'Type','Left','MergeKeys', 1);

% Step 3: Quintile, name-breaks, VW
step3 = results(results.stockFilter == stockFilter & ...
               results.nPtfs==5 & ...
               ismember(results.breaks, {'name'}) & ...
               ismember(results.weighting, 'value'),{'numer','denom','signal','txret','tnetret','endDate','consecutiveDates'});
step3.Properties.VariableNames = {'numer','denom','signal','txret3','tnetret3','endDate','consecutiveDates'};
res = outerjoin(res, step3, 'Type','Left','MergeKeys', 1);


% Step 4: Quintile, NYSE-breaks, VW
step4 = results(results.stockFilter == stockFilter & ...
               results.nPtfs==5 & ...
               ismember(results.breaks, {'NYSE'}) & ...
               ismember(results.weighting, 'value'),{'numer','denom','signal','txret','talpha','tnetret','tnetalpha'});
step4.Properties.VariableNames = {'numer','denom','signal','txret4','talpha4','tnetret4','tnetalpha4'};
res = outerjoin(res, step4, 'Type','Left','MergeKeys', 1);

ind = (res.rdndntFlag==false & res.endDate==emonth_cutoff & res.endDate2==emonth_cutoff & res.consecutiveDates>cmonth_cutoff & res.consecutiveDates2>cmonth_cutoff & abs(res.txret)>t_cutoff & abs(res.txret2)>t_cutoff & abs(res.txret3)>t_cutoff & abs(res.txret4)>t_cutoff & abs(res.talpha4)>t_cutoff);
printRes = res(ind,:);

save Res\printRes printRes
