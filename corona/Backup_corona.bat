SET JOUR=%date:~-10,2% 
SET ANNEE=%date:~-4% 
SET MOIS=%date:~-7,2% 
SET HEURE=%time:~0,2%
SET MINUTE=%time:~3,2%
SET REPERTOIR=C:\Users\Utilisateur\Desktop\sql
SET FICHIER=%REPERTOIR%\Sauvegarde_corona_%JOUR%_%MOIS%_%ANNEE%_%HEURE%_%MINUTE%.sql
IF NOT exist "%REPERTOIR%" md "%REPERTOIR%"

mysqldump --login-path=local corona > "%FICHIER%"
 