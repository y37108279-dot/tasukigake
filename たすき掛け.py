import random

NUM_PROBLEMS = 60


def generate_problem():
    while True:
        a = random.randint(2, 9)
        c = random.randint(1, 9)
        b = random.randint(-9, 9)
        d = random.randint(-9, 9)

        if b == 0 or d == 0:
            continue

        A = a * c
        B = a * d + b * c
        C = b * d

        if A > 1 and B != 0 and C != 0:
            return {
                "A": A,
                "B": B,
                "C": C,
                "factor": (a, b, c, d)
            }


problems = []
seen = set()

while len(problems) < NUM_PROBLEMS:
    p = generate_problem()

    key = (p["A"], p["B"], p["C"])

    if key not in seen:
        seen.add(key)
        problems.append(p)


html = """
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>たすき掛け練習問題</title>

<style>
body{
    font-family: sans-serif;
    max-width:900px;
    margin:auto;
    padding:30px;
}

h1,h2{
    text-align:center;
}

.problem{
    font-size:20px;
    margin:10px 0;
}

.page-break{
    page-break-before:always;
}

@media print{
    .page-break{
        page-break-before:always;
    }
}
</style>
</head>
<body>

<h1>因数分解（たすき掛け）練習問題</h1>

"""
for i, p in enumerate(problems, start=1):

    Bsign = "+" if p["B"] > 0 else "-"
    Csign = "+" if p["C"] > 0 else "-"

    html += (
        f'<div class="problem">'
        f'{i}. '
        f'{p["A"]}x² '
        f'{Bsign} {abs(p["B"])}x '
        f'{Csign} {abs(p["C"])}'
        f'</div>\n'
    )

html += """
<div class="page-break"></div>

<h2>解答</h2>
"""

for i, p in enumerate(problems, start=1):

    a, b, c, d = p["factor"]

    bsign = "+" if b > 0 else "-"
    dsign = "+" if d > 0 else "-"

    html += (
        f'<div class="problem">'
        f'{i}. '
        f'({a}x {bsign} {abs(b)})'
        f'({c}x {dsign} {abs(d)})'
        f'</div>\n'
    )

html += """
</body>
</html>
"""

with open("worksheet.html", "w", encoding="utf-8") as f:
    f.write(html)

print("worksheet.html を作成しました")