function [signalInfo] = makeSignalInfo(numer, denom, numerTable)


signalInfo.Authors       = 'Robert Novy-Marx and Mihail Velikov';
signalInfo.email         = 'velikov@psu.edu';
signalInfo.PaperTitle    = 'Assaying Anomalies';

load NYSE
load me
load ret
load dates
load permno

[nMonths, nStocks] = size(ret);
nObs = nMonths*nStocks;

if ~contains(numer, 'd_')
    changeInd = false;
    numerVar = load([char(numer),'.mat']);
    numerVar = numerVar.(char(numer));

    denomVar = load([char(denom),'.mat']);
    denomVar = denomVar.(char(denom));
    denomVar(denomVar==0) = nan;

    var = (numerVar)./denomVar;
    
    und_numer = numer;
else
    changeInd = true;
    und_numer = regexprep(numer, 'd_', '');

    undNumerVar = load([char(und_numer),'.mat']);
    undNumerVar = undNumerVar.(char(und_numer));
    numerVar = undNumerVar - lag(undNumerVar, 12, nan);
    
    denomVar = load([char(denom),'.mat']);
    denomVar = denomVar.(char(denom));
    denomVar(denomVar==0) = nan;
    
    var = (numerVar)./lag(denomVar, 12, nan);

end

ind = makeUnivSortInd(var, 5, NYSE);
res = runUnivSort(ret, ind, dates, me, 'printResults', 0, ...
    'plotFigure', 0);

ptfNumStocks = res.ptfNumStocks(:,[1 end-1]);
s = find(~all(ptfNumStocks > 30, 2), 1, 'last')+1;
var(1:s-1,:) = nan;

if res.xret(end)<0
    var = - var;
    numer = ['neg_', numer];
end


varName = [numer,'_',char(denom)];
exportData = array2table([reshape(repmat(permno', nMonths, 1), nObs, 1) ...
                          reshape(repmat(dates, 1, nStocks), nObs, 1) ...
                          reshape(var, nObs, 1)], 'VariableNames', {'permno','dates',varName});
exportData(exportData.dates<=196305 | isnan(exportData.(varName)), :) = [];
writetable(exportData, ['Data/', varName,'.csv']);

numerInd = find(strcmp(numerTable.acronym, und_numer));
denomInd = find(strcmp(numerTable.acronym, denom));

numerDesc = char(numerTable.shortername(numerInd));
denomDesc = char(numerTable.shortername(denomInd));

if changeInd
    signalInfo.SignalName = ['Changes in ', numerDesc, ' to ', denomDesc];
else
    signalInfo.SignalName = [numerDesc, ' to ', denomDesc];
end
signalInfo.SignalAcronym = varName;
signalInfo.fileLink      = ['Data/', varName,'.csv'];

signalInfo.SignalName    = (erase(signalInfo.SignalName, {'<','>','\','/',':','*','|','_','&'}));
signalInfo.SignalAcronym = upper(erase(signalInfo.SignalAcronym, {'<','>','\','/',':','*','|','_',' ','&'}));


