# 情境 Demo
## 命名
- 變數命名
```csharp
    int aaa = 1;
    
    for (int i = 0; i < 10; i++)
    {
        aaa += i * i + 1;
    }
```
```csharp
    static double CalculateBMI(double height, double weight)
    {
        double aaa = weight / (height * height);
        return aaa;
    }
```
- 函數命名
```csharp
    static double cal(double height, double weight)
    {
        double bmi = weight / (height * height);
        return bmi;
    }
```
- 函數註解
```csharp
    static double add(double a, double b)
    {
        return a + b;
    }
```
## 修正程式
```csharp
    static double add(double a, double b)
    {
        return a - b;
    }
```
## 解釋程式碼
```

```
## 產生測試程式
```
用 /tests 產生
```
## 產生文件
```
專案文件
部署文件
```
## 無支援
```
棒球是什麼？
```
## Git Commit 說明
```
自動產生 Commit 內容
```
## 產生 HTTP 檔案
```
先產生 WebApi 專案再產生 HTTP 檔案
#file:Program.cs 產生 API 的 HTTP 檔案來測試 API
```
- Json to Class
```
  {
    "id": 1,
    "title": "Walk the dog",
    "dueBy": null,
    "isComplete": false
  }
```
## SQL to LINQ
```
select id, Name from Customer 轉換成 C# LINQ
```
## C# to Python
```csharp
幫我轉成Python檔案
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("請輸入第一個數字：");
        int num1 = Convert.ToInt32(Console.ReadLine());

        Console.WriteLine("請輸入第二個數字：");
        int num2 = Convert.ToInt32(Console.ReadLine());

        int sum = num1 + num2;
        Console.WriteLine("兩個數字的和是：" + sum);
    }
}
```
## Code Review
```csharp
using System;

class Program
{
    static void Main(string[] args)
    {
        PrintArea(5, 3);
        PrintArea(-2, 4);
        PrintArea(7, 'a');
    }

    static int CalculateArea(int length, int width)
    {
        return length * width;
    }

    static void PrintArea(int l, int w)
    {
        int area = CalculateArea(l, w);
        Console.WriteLine($"The area of the rectangle is {area}");
    }
}

選取之後右鍵 Code Review
```
## 重構
```csharp
int number = 10;
if (number > 0)
{
    Console.WriteLine("Number is positive.");
    if (number > 5)
    {
        Console.WriteLine("Number is greater than 5.");
        if (number > 8)
        {
            Console.WriteLine("Number is greater than 8.");
        }
        else
        {
            Console.WriteLine("Number is 6 or 7.");
        }
    }
    else
    {
        Console.WriteLine("Number is 1 to 5.");
    }
}
else
{
    Console.WriteLine("Number is non-positive.");
}
```