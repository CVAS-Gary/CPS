# 查詢電腦名稱
$computerName = $env:COMPUTERNAME
Write-Host "電腦名稱: $computerName"

# 或使用更詳細的方式
$computerInfo = Get-ComputerInfo | Select-Object CsName, CsDNSHostName, CsDomain
Write-Host "`n詳細資訊:"
Write-Host "電腦名稱: $($computerInfo.CsName)"
Write-Host "完整 DNS 主機名稱: $($computerInfo.CsDNSHostName)"
Write-Host "網域: $($computerInfo.CsDomain)"