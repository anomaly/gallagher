# Define variables
$serviceName = "MSSQLSERVER" # Change this to your SQL Server service name
$serverInstance = "localhost" # Change this as necessary
$databaseName = "YourDatabaseName"
$dbFilesPath = "C:\Path\To\Database\Files"
$backupPath = "C:\Path\To\Backup\Location"

# Import SQL Server module
Import-Module "SqlServer"

# Stop SQL Server Service
Stop-Service -Name $serviceName -Force
Write-Host "Service stopped."

# Detach the database
Invoke-Sqlcmd -ServerInstance $serverInstance -Query "EXEC sp_detach_db '$databaseName'"
Write-Host "Database detached."

# Copy database files
$mdfFile = "$dbFilesPath\$databaseName.mdf"
$ldfFile = "$dbFilesPath\$databaseName_Log.ldf"
Copy-Item -Path $mdfFile -Destination $backupPath -Force
Copy-Item -Path $ldfFile -Destination $backupPath -Force
Write-Host "Database files copied."

# Reattach the database
$mdfFileBackup = "$backupPath\$databaseName.mdf"
$ldfFileBackup = "$backupPath\$databaseName_Log.ldf"
Invoke-Sqlcmd -ServerInstance $serverInstance -Query "CREATE DATABASE $databaseName ON (FILENAME = '$mdfFileBackup'), (FILENAME = '$ldfFileBackup') FOR ATTACH"
Write-Host "Database reattached."

# Start SQL Server Service
Start-Service -Name $serviceName
Write-Host "Service started."

Write-Host "Operation completed successfully."