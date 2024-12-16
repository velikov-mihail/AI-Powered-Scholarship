%%

clear
clc

% Get numerators 
opts = detectImportOptions('Mining_Variable_List.xlsx', 'Sheet', 'Numerators');
numer = readtable('Mining_Variable_List.xlsx', opts);

% And denominators
opts = detectImportOptions('Mining_Variable_List.xlsx', 'Sheet', 'Denominators');
denom = readtable('Mining_Variable_List.xlsx', opts);

nNumer = height(numer);
nDenom = height(denom);


fullRes = struct;

parpool(40);

parfor i = 1:nNumer
    i
    res = load(['res_',char(numer.acronym(i)),'.mat']);
    fullRes(i,1).res = res.res;
end

load ff
load dates
load ff_tc
s = find(dates==196307);
e = find(dates==202312);
ff6 = ff6(s:e, :);
ff6_tc = ff6_tc(s:e, :);

results=table;
count = 1;
tic

nRows = nNumer*nDenom*3*2^4;
results.numer = cell(nRows,1);
results.denom = cell(nRows,1);
results.signal = cell(nRows,1);
results.nPtfs = nan(nRows,1);
results.breaks = cell(nRows,1);
results.weighting = cell(nRows,1);
results.xret = nan(nRows,1);
results.txret = nan(nRows,1);
results.netret = nan(nRows, 1);
results.tnetret = nan(nRows, 1);
results.alpha = nan(nRows,1);
results.talpha = nan(nRows,1);
results.netalpha = nan(nRows, 1);
results.tnetalpha = nan(nRows, 1);
results.startDate = nan(nRows,1);
results.endDate = nan(nRows,1);
results.consecutiveDates = nan(nRows,1);
results.stockFilter = nan(nRows, 1);

warning('off','all');
for i=1:nNumer  
    i
    toc
    tic
    for j=1:nDenom
        for k=1:2
            for l=1:2
                for m=1:2
                    for w=1:2
                        for f=1:3
                            tempRes = fullRes(i).res(j, k, l, m, w).res;
                            results.numer(count) = numer.acronym(i);
                            results.denom(count) = denom.acronym(j);
                            if k ==1
                                results.signal(count) = {'diff'};
                            else
                                results.signal(count) = {'ratio'};
                            end
                            if l==1
                                results.nPtfs(count) = 5;
                            else
                                results.nPtfs(count) = 10;
                            end
                            if m==1
                                results.breaks(count) = {'name'};
                            else
                                results.breaks(count) = {'NYSE'};
                            end
                            if w==1
                                results.weighting(count) = {'equal'};
                            else
                                results.weighting(count) = {'value'};
                            end
                            if f==1
                                results.stockFilter(count) = 10;
                            elseif f==2
                                results.stockFilter(count) = 20;
                            else
                                results.stockFilter(count) = 30;
                            end
    
                            if ~isempty(tempRes)
                                ptfNumStocks = tempRes.ptfNumStocks(:,[1 end-1]);
                                
                                % Find the last month where both portfolios had more than 30 stocks
                                e = (find(all(ptfNumStocks > results.stockFilter(count), 2), 1, 'last'));
                                
    
                                % Find the number of consecutive months up to and including the last one where both portfolios had more than 30 stocks
                                s = find(~all(ptfNumStocks(1:e, :) > results.stockFilter(count), 2), 1, 'last')+1;
                                
    
                                if isfinite(s+e) & e>s
                                    pret = tempRes.pret(s:e,end);
                                    ptfCosts = tempRes.ptfCosts(s:e,1) + tempRes.ptfCosts(s:e,2);
                                    netpret = (pret)*sign(mean(pret)) - ptfCosts;
                                   
                                    
                                    % Gross returns
                                    tmpRes = ols(pret, const(s:e));
                                    results.xret(count) = tmpRes.beta;
                                    results.txret(count) = tmpRes.tstat;
    
                                    % Gross alphas                                    
                                    tmpRes = ols(pret, ff6(s:e,:));                                    
                                    results.alpha(count) = tmpRes.beta(1);
                                    results.talpha(count) = tmpRes.tstat(1);

                                    % Net returns
                                    tmpRes = ols(netpret, const(s:e));
                                    results.netret(count) = tmpRes.beta;
                                    results.tnetret(count) = tmpRes.tstat;
                                   

                                    % Net alpha
                                    [tmpRes] = calcGenAlpha(pret, ptfCosts, ...
                                                             ff6(s:e, 2:end), ff6_tc(s:e, :), 0);
                                    results.netalpha(count) = tmpRes.beta(1);
                                    results.tnetalpha(count) = tmpRes.tstat(1);
                                    
                                    % Other stuff
                                    results.startDate(count) = tempRes.dates(s);
                                    results.endDate(count) = tempRes.dates(e);
                                    results.consecutiveDates(count) = e-s+1;
                                else
                                    results.xret(count) = nan;
                                    results.txret(count) = nan;
                                    results.alpha(count) = nan;
                                    results.talpha(count) = nan;
                                    results.netret(count) = nan;
                                    results.tnetret(count) = nan;
                                    results.netalpha(count) = nan;
                                    results.tnetalpha(count) = nan;
                                    results.startDate(count) = nan;
                                    results.endDate(count) = nan;
                                    results.consecutiveDates(count) = nan;   
                                end
                            else
                                results.xret(count) = nan;
                                results.txret(count) = nan;
                                results.alpha(count) = nan;
                                results.talpha(count) = nan;
                                results.talpha(count) = nan;
                                results.netret(count) = nan;
                                results.tnetret(count) = nan;
                                results.netalpha(count) = nan;
                                results.startDate(count) = nan;
                                results.endDate(count) = nan;
                                results.consecutiveDates(count) = nan;
                            end
                            count = count+1;
                        end
                    end
                end
            end
        end
    end
end

results.rdndntFlag = false(nRows,1);

for i=1:nDenom
    for j=1:i
        ind = ismember(results.numer, denom.acronym(i)) & ismember(results.denom, denom.acronym(j)) & ismember(results.signal, {'ratio'});
        results.rdndntFlag(ind) = true;
    end
end

save Res\results results
