from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>محلل الشموع اليابانية</title>
<style>
* { box-sizing: border-box; }
body {
    margin: 0;
    padding: 20px;
    background: #101827;
    color: white;
    font-family: Arial, sans-serif;
    text-align: center;
}
.container {
    max-width: 500px;
    margin: 25px auto;
    padding: 24px;
    background: #1c293b;
    border-radius: 18px;
}
h1 { color: #45d6b5; }
p { color: #c4d0df; }
.upload {
    display: block;
    padding: 18px;
    margin: 25px 0;
    background: #263b52;
    border: 2px dashed #45d6b5;
    border-radius: 12px;
}
button {
    width: 100%;
    padding: 15px;
    background: #45d6b5;
    border: none;
    border-radius: 10px;
    font-size: 18px;
    font-weight: bold;
}
#preview {
    max-width: 100%;
    margin-top: 20px;
    border-radius: 12px;
    display: none;
}
.result {
    margin-top: 22px;
    padding: 15px;
    background: #263b52;
    border-radius: 12px;
}
footer { margin-top: 25px; color: #91a0b3; }
</style>
</head>
<body>
<div class="container">
<h1>📊 محلل الشموع اليابانية</h1>
<p>ارفع صورة الشموع لعرضها والاستعداد لتحليل أنماطها</p>

<label class="upload">
📷 اختر صورة الشموع
<input type="file" id="image" accept="image/*" hidden>
</label>

<img id="preview">

<div class="result" id="result">
بانتظار اختيار صورة
</div>

<footer>محلل تعليمي للتعرف على أنماط الشموع</footer>
</div>

<script>
const input = document.getElementById("image");
const preview = document.getElementById("preview");
const result = document.getElementById("result");

input.addEventListener("change", function() {
    const file = this.files[0];
    if (!file) return;

    preview.src = URL.createObjectURL(file);
    preview.style.display = "block";
    result.textContent = "تم اختيار الصورة بنجاح. التحليل الآلي لم يُفعّل بعد.";
});
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
