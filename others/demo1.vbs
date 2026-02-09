Private Sub Form_Load()
    Me.Caption = "學生資料管理系統"
    Command1.Caption = "新增"
    Command2.Caption = "刪除"
    Command3.Caption = "查詢"
    Command4.Caption = "統計"
    Command5.Caption = "清除"
    Command6.Caption = "離開"
    Option1.Caption = "男"
    Option2.Caption = "女"
    Combo1.Clear
    Combo1.AddItem "A班"
    Combo1.AddItem "B班"
    Combo1.AddItem "C班"
    Combo1.ListIndex = 0
    List1.Clear
    Text1.Text = ""
    Text2.Text = ""
    Option1.Value = True
End Sub

Private Sub Command1_Click()
    Dim 姓名 As String, 年齡 As Integer, 性別 As String, 班級 As String, 訊息 As String

    姓名 = Trim(Text1.Text)
    If 姓名 = "" Then
        MsgBox "請輸入姓名！", vbExclamation, "錯誤"
        Text1.SetFocus
        Exit Sub
    End If

    If Not IsNumeric(Text2.Text) Then
        MsgBox "年齡必須為數字！", vbExclamation, "錯誤"
        Text2.SetFocus
        Exit Sub
    End If

    年齡 = Val(Text2.Text)
    If 年齡 <= 0 Or 年齡 > 120 Then
        MsgBox "請輸入合理的年齡！", vbExclamation, "錯誤"
        Text2.SetFocus
        Exit Sub
    End If

    If Option1.Value = True Then
        性別 = "男"
    Else
        性別 = "女"
    End If

    班級 = Combo1.Text
    訊息 = 姓名 & " | " & 年齡 & "歲 | " & 性別 & " | " & 班級
    List1.AddItem 訊息

    MsgBox "學生資料已新增！", vbInformation, "成功"
End Sub

Private Sub Command2_Click()
    If List1.ListIndex >= 0 Then
        List1.RemoveItem List1.ListIndex
        MsgBox "已刪除選取的學生資料。", vbInformation, "刪除"
    Else
        MsgBox "請先選取要刪除的學生資料。", vbExclamation, "提示"
    End If
End Sub

Private Sub Command3_Click()
    Dim 關鍵字 As String, i As Integer, 找到 As Boolean
    關鍵字 = InputBox("請輸入要查詢的姓名關鍵字：", "查詢")
    找到 = False
    For i = 0 To List1.ListCount - 1
        If InStr(List1.List(i), 關鍵字) > 0 Then
            List1.Selected(i) = True
            找到 = True
        Else
            List1.Selected(i) = False
        End If
    Next
    If 找到 Then
        MsgBox "查詢完成，已標示符合條件的學生。", vbInformation, "查詢"
    Else
        MsgBox "查無符合條件的學生。", vbExclamation, "查詢"
    End If
End Sub

Private Sub Command4_Click()
    Dim 男生 As Integer, 女生 As Integer, i As Integer
    男生 = 0: 女生 = 0
    For i = 0 To List1.ListCount - 1
        If InStr(List1.List(i), "男") > 0 Then
            男生 = 男生 + 1
        ElseIf InStr(List1.List(i), "女") > 0 Then
            女生 = 女生 + 1
        End If
    Next
    MsgBox "目前學生總數：" & List1.ListCount & vbCrLf & _
           "男生：" & 男生 & " 人" & vbCrLf & _
           "女生：" & 女生 & " 人", vbInformation, "統計"
End Sub

Private Sub Command5_Click()
    Text1.Text = ""
    Text2.Text = ""
    Combo1.ListIndex = 0
    Option1.Value = True
    List1.Clear
    Text1.SetFocus
End Sub

Private Sub Command6_Click()
    If MsgBox("確定要離開程式嗎？", vbYesNo + vbQuestion, "離開") = vbYes Then
        End
    End If
End Sub

Private Sub List1_DblClick()
    If List1.ListIndex >= 0 Then
        MsgBox "學生資料：" & vbCrLf & List1.List(List1.ListIndex), vbInformation, "詳細資料"
    End If
End Sub