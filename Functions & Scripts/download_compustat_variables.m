%%

clear
clc

% Get numerators 
opts = detectImportOptions('Mining_Variable_List.xlsx', 'Sheet', 'Numerators');
numer = readtable('Mining_Variable_List.xlsx', opts);

% And denominators
opts = detectImportOptions('Mining_Variable_List.xlsx', 'Sheet', 'Denominators');
denom = readtable('Mining_Variable_List.xlsx', opts);

% WRDS username and password
username = usernameUI();
pass = passwordUI();

% Find the ones we need to download
nNumer = height(numer); 
nDenom = height(denom);

dataPath = '../Data/COMPUSTAT/'; 

numerToDwnld = false(nNumer, 1);
denomToDwnld = false(nDenom, 1);

% Numerators
for i =1:nNumer
    if ~exist([dataPath,char(numer.acronym(i)),'.mat']) & ~strcmp(char(numer.acronym(i)), 'me_datadate')
        numerToDwnld(i) = true;
    end
end

% Denominators
for i =1:nDenom
    if ~exist([dataPath,char(denom.acronym(i)),'.mat']) & ~strcmp(char(denom.acronym(i)), 'me_datadate')
        denomToDwnld(i) = true;
    end
end

% Download if any
dataToDwnld = unique([numer.acronym(numerToDwnld) denom.acronym(denomToDwnld)]');
if ~isempty(dataToDwnld)
    getCOMPUSTATAdditionalData(username, pass, dataToDwnld, 'annual');
end
