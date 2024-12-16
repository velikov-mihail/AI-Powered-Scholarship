%% Create me_datadate

clear
clc

if ~exist('Data', 'dir')
    mkdir('Data'); % Create the folder if it doesn't exist
end


load me
load dates

me_datadate = lag(me, 6, nan);

juneInd = dates - 100*floor(dates/100) == 6;

me_datadate(~juneInd,:) = nan;

% Save the variable in the 'Data' subfolder
save(fullfile('Data', 'me_datadate.mat'), 'me_datadate');
