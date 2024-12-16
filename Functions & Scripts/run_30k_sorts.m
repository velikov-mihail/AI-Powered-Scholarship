%%

clear
clc

folderPath = 'Res';
if ~exist(folderPath, 'dir')
    mkdir(folderPath);
end
addpath(genpath([folderPath]))

% Get numerators 
opts = detectImportOptions('Mining_Variable_List.xlsx', 'Sheet', 'Numerators');
numer = readtable('Mining_Variable_List.xlsx', opts);

% And denominators
opts = detectImportOptions('Mining_Variable_List.xlsx', 'Sheet', 'Denominators');
denom = readtable('Mining_Variable_List.xlsx', opts);

nNumer = height(numer);
nDenom = height(denom);

load ret
load me
load dates
load NYSE
load tcosts

s = find(dates==196307);

parpool(40);

fprintf('%s\n',char(datetime('now')));

for i = 1:nNumer

    res = struct;

    numerVar = load([char(numer.acronym(i)),'.mat']);
    numerVar = numerVar.(char(numer.acronym(i)));
    numerAcronym =(numer.acronym(i));

    parfor j = 1:nDenom

        denomAcronym = denom.acronym(j);

        denomVar = load([char(denomAcronym),'.mat']);
        denomVar = denomVar.(char(denomAcronym));        
        denomVar(denomVar == 0) = nan;

        for k = 1:2
            if k==1
                var = (numerVar - lag(numerVar, 12, nan))./lag(denomVar, 12, nan);
            elseif k==2 & ~strcmp(denom.acronym(j), numerAcronym)
                var = (numerVar)./denomVar;
            else
                continue;
            end

            for l=1:2
                if l==1
                    nPtfs = 5;
                else 
                    nPtfs = 10;
                end


                for m=1:2
                    if m==1
                        ind = makeUnivSortInd(var, nPtfs);
                    else
                        ind = makeUnivSortInd(var, nPtfs, NYSE);
                    end
                    ind = 1*(ind==1) + 2*(ind==nPtfs);

                    for w = 1:2
                        if w==1
                            weight = 'e';
                        else
                            weight = 'v';
                        end

                        try
                            tempRes = runUnivSort(ret, ind, dates, me, 'timePeriod', 196307, ...
                                                                       'weighting', weight, ...
                                                                       'factorModel', 6, ...
                                                                       'tcosts', tcosts, ...
                                                                       'printResults', 0, ...
                                                                       'plotFigure', 0);
                            res(j, k, l, m, w).res = tempRes;

                        catch
                          fprintf('Error with (%s, %s).\n', char(numerAcronym), char(denomAcronym));
                        end
                    end
                end
            end
        end
    end

    
    save(['Res/res_',char(numer.acronym(i)),'.mat'],'res');
    clear res
    fprintf('Done with %s, which is %d out of %d @ %s.\n', char(numer.acronym(i)), i, nNumer, char(datetime('now')));   
end
