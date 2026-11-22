app.py
from flask import Flask, render_template_string, request
from candle_analyzer import safe_analyze

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>محلل الشموع اليابانية</title>

<style>
body {
        background: #101827;
            color: white;
                font-family: Arial;
                    text-align: center;
                        padding: 20px;
}
.container {
        max-width: 600px;
            margin: auto;
}
.card {
        background: #1d2b40;
            padding: 20px;
                border-radius: 15px;
                    margin-top: 20px;
}
button {
        background: #16a085;
            color: white;
                border: none;
                    padding: 14px 25px;
                        border-radius: 10px;
                            font-size: 17px;
}
textarea {
        width: 90%;
            height: 130px;
                border-radius: 10px;
                    padding: 10px;
}
</style>
</head>

<body>
<div class="container">
<h1>📊 محلل الشموع اليابانية</h1>
<p>محلل تعليمي للأنماط اليابانية</p>

<div class="card">
<h3>بيانات الشموع</h3>
<p>أدخل بيانات الشموع بصيغة JSON</p>

<form method="POST">
<textarea name="candles" placeholder='[{"open":10,"high":12,"low":8,"close":11}]'></textarea>
<br><br>
<button type="submit">تحليل الشموع</button>
</form>
</div>

{% if result %}
<div class="card">
<h3>نتيجة التحليل</h3>
<pre>{{ result }}</pre>
</div>
{% endif %}

</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

        if request.method == "POST":
                import json
                        try:
                                    candles = json.loads(request.form["candles"])
                                                result = safe_analyze(candles)
                                                        except Exception:
                                                                    result = "تعذر قراءة البيانات"

                                                                        return render_template_string(HTML, result=result)

                                                                        if __name__ == "__main__":
                                                                            app.run(host="0.0.0.0", port=5000)
}