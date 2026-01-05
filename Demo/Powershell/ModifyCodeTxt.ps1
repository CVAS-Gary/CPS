# 讀取 code.txt，尋找包含 aaa 或 bbb 的行，並在其下兩行的首字元加上 #
$inputFile = "code.txt"
$outputFile = "code_out.txt"

# 讀取所有行
$lines = Get-Content $inputFile

for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match 'aaa|bbb') {
        $targetIndex = $i + 2
        if ($targetIndex -lt $lines.Count) {
            # 若該行非空，則在首字元加上 #
            if ($lines[$targetIndex].Length -gt 0) {
                $lines[$targetIndex] = "#" + $lines[$targetIndex]
            } else {
                $lines[$targetIndex] = "#"
            }
        }
    }
}

# 輸出到新檔案
$lines | Set-Content $outputFile
Write-Host "處理完成，結果已輸出至 $outputFile"