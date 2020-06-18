@echo off


set source1="C:\Users\Utilisateur\Downloads\google_reports"
set source2="C:\Users\Utilisateur\Downloads\apple_reports"

set destination="C:\Data_Apple_Google"


robocopy "%source1%" "%destination%" /mov 
robocopy "%source2%" "%destination%" /mov 
exit /b