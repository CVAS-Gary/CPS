'計算機程式
Dim num1, num2, operator, result
'輸入第一個數字
num1 = InputBox("請輸入第一個數字：")
'輸入運算符號
operator = InputBox("請輸入運算符號（+、-、*、/）：")
'輸入第二個數字
num2 = InputBox("請輸入第二個數字：")
'進行運算Select Case operator
    Case "+"
        result = CDbl(num1) + CDbl(num2)
    Case "-"
        result = CDbl(num1) - CDbl(num2)
    Case "*"
        result = CDbl(num1) * CDbl(num2)
    Case "/"
        If CDbl(num2) <> 0 Then
            result = CDbl(num1) / CDbl(num2)
        Else
            MsgBox "除數不能為零！"
            WScript.Quit
        End If
    Case Else
        MsgBox "無效的運算符號！"
        WScript.Quit
End Select
'顯示結果
MsgBox "計算結果為：" & result