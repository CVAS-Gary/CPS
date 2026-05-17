using System.Globalization;
using System.Text;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => Results.Content(RenderPage(), "text/html; charset=utf-8"));

app.MapPost("/", async (HttpRequest request) =>
{
    var form = await request.ReadFormAsync();
    var heightInput = form["heightCm"].ToString();
    var weightInput = form["weightKg"].ToString();

    if (!double.TryParse(heightInput, NumberStyles.Float, CultureInfo.InvariantCulture, out var heightCm) ||
        !double.TryParse(weightInput, NumberStyles.Float, CultureInfo.InvariantCulture, out var weightKg))
    {
        return Results.Content(RenderPage(heightInput, weightInput, errorMessage: "請輸入有效的數字。"), "text/html; charset=utf-8");
    }

    if (heightCm <= 0 || weightKg <= 0)
    {
        return Results.Content(RenderPage(heightInput, weightInput, errorMessage: "身高與體重都必須大於 0。"), "text/html; charset=utf-8");
    }

    var bmi = Math.Round(weightKg / Math.Pow(heightCm / 100.0, 2), 2);
    var category = bmi switch
    {
        < 18.5 => "過輕",
        < 24 => "正常",
        < 27 => "過重",
        < 30 => "輕度肥胖",
        < 35 => "中度肥胖",
        _ => "重度肥胖"
    };

    return Results.Content(RenderPage(heightInput, weightInput, bmi, category), "text/html; charset=utf-8");
});

app.Run();

static string RenderPage(string heightValue = "", string weightValue = "", double? bmi = null, string? category = null, string? errorMessage = null)
{
    var builder = new StringBuilder();
    var safeHeight = System.Net.WebUtility.HtmlEncode(heightValue);
    var safeWeight = System.Net.WebUtility.HtmlEncode(weightValue);
    builder.AppendLine("""
<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>BMI 計算器</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; max-width: 720px; margin: 32px auto; padding: 0 16px; }
    form { display: grid; gap: 12px; }
    input { padding: 8px; font-size: 16px; }
    button { width: 120px; padding: 10px; font-size: 16px; cursor: pointer; }
    .message { margin-top: 16px; padding: 12px; border-radius: 8px; }
    .ok { background: #eaf7ea; color: #1e5f2f; }
    .error { background: #fdeaea; color: #8c1d1d; }
  </style>
</head>
<body>
  <h1>BMI 計算器</h1>
  <p>請輸入身高（公分）與體重（公斤）後按下計算。</p>
  <form method="post">
    <label for="heightCm">身高（cm）</label>
""");
    builder.AppendLine($"""    <input id="heightCm" name="heightCm" type="number" min="0.1" step="0.1" required value="{safeHeight}" />""");
    builder.AppendLine("""
    <label for="weightKg">體重（kg）</label>
""");
    builder.AppendLine($"""    <input id="weightKg" name="weightKg" type="number" min="0.1" step="0.1" required value="{safeWeight}" />""");
    builder.AppendLine("""
    <button type="submit">計算 BMI</button>
  </form>
""");

    if (!string.IsNullOrEmpty(errorMessage))
    {
        builder.AppendLine($"""  <div class="message error">{System.Net.WebUtility.HtmlEncode(errorMessage)}</div>""");
    }
    else if (bmi.HasValue)
    {
        builder.AppendLine($"""  <div class="message ok">BMI：<strong>{bmi.Value:0.00}</strong>（{System.Net.WebUtility.HtmlEncode(category)}）</div>""");
    }

    builder.AppendLine("""
</body>
</html>
""");

    return builder.ToString();
}
