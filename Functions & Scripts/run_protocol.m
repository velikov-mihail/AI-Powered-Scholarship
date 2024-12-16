%% Run assay tool on the remaining signals

clear
clc

load printRes.mat

opts = detectImportOptions('Mining_Variable_List.xlsx', 'Sheet', 'Numerators');
numerTable = readtable('Mining_Variable_List.xlsx', opts);

% parfor  i = 1:height(printRes)
%     i
%     if strcmp(char(printRes.signal(i)), 'diff')
%         numer = ['d_',char(printRes.numer(i))];
%     else
%         numer = char(printRes.numer(i));
%     end
%     denom = char(printRes.denom(i));
% 
%     [signalInfo(i,1)] = makeSignalInfo(numer, denom, numerTable);
% end
% save signalInfo signalInfo
load signalInfo

% Get the anomalies
[anoms, labelsCZ, anomaly_summary] = getChenZimmermanAnomalies();
labels.short = labelsCZ;
labels.long = anomaly_summary.LongDescription';


% Add some noise to anoms and run univariate sorts
load ret
load dates
load me
load tcosts
load NYSE
[anoms, resAnoms] = makeAnomStratResults(anoms, ret, dates, me, tcosts, NYSE);

for i = 1:length(signalInfo)
    try
       % Run the test signals
        runTestSignal(signalInfo(i), anoms, labels, resAnoms);
    catch e %e is an MException struct
        fprintf('Signal %s produced an error.\n', signalInfo(i).SignalAcronym);    
        fprintf('The identifier was:\n%s\n',e.identifier);
        fprintf('There was an error! The message was:\n%s\n',e.message);
    end
       
end

