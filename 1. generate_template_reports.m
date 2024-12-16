clear
clc

% Start with the default path
restoredefaultpath; 

% Path to the MATLAB asset pricing package
matlabPackagePath = '/scratch/mjv5465/GPT-Anoms/'; 
paperPackagePath = '/scratch/mjv5465/GPT-Anoms/Scratch/'; 

% Add the relevant folders (with subfolders) to the path
addpath(genpath([matlabPackagePath, 'Data']))
addpath(genpath([matlabPackagePath, 'Functions']))
addpath(genpath([matlabPackagePath, 'Library Update']))
addpath(genpath(paperPackagePath));

% Navigate to the paper folder
cd(paperPackagePath)

%% Download COMPUSTAT variables

run('download_compustat_variables.m');

%% Make me_datadate

run('make_me_datadate.m');

%% Run 30K univariate sorts

run('run_30k_sorts.m');

%% Store results (results.mat)

run('store_results.m');

%% Filter the results (printRes.mat & fullRes.mat)

run('filter_results.m');

%% Run protocol on signals

run('run_protocol.m');