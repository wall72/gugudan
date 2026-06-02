"""Flask 기반 웹 구구단 앱."""

from flask import Flask, render_template_string, request

from gugudan.base import GugudanApp

_HTML = """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>구구단</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; }
    body {
      font-family: 'Segoe UI', sans-serif;
      background: #f0f2f5;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 2rem 1rem;
      min-height: 100vh;
      margin: 0;
    }
    h1 { margin-bottom: 1.5rem; color: #333; }
    form {
      display: flex;
      gap: .5rem;
      margin-bottom: 2rem;
    }
    input[type=number] {
      padding: .5rem .75rem;
      font-size: 1rem;
      border: 1px solid #ccc;
      border-radius: 6px;
      width: 6rem;
    }
    button {
      padding: .5rem 1.25rem;
      font-size: 1rem;
      background: #4a90e2;
      color: #fff;
      border: none;
      border-radius: 6px;
      cursor: pointer;
    }
    button:hover { background: #357abd; }
    .table-wrap {
      background: #fff;
      border-radius: 10px;
      padding: 1.25rem 2rem;
      box-shadow: 0 2px 8px rgba(0,0,0,.1);
      min-width: 200px;
    }
    .table-wrap h2 { margin: 0 0 .75rem; color: #555; }
    ul { list-style: none; margin: 0; padding: 0; }
    li { padding: .2rem 0; font-size: 1.05rem; color: #222; }
    .error { color: #c0392b; }
  </style>
</head>
<body>
  <h1>🔢 구구단</h1>
  <form method="post">
    <input type="number" name="n" value="{{ n }}" placeholder="단수" required autofocus>
    <button type="submit">계산</button>
  </form>
  {% if error %}
    <p class="error">{{ error }}</p>
  {% elif rows %}
    <div class="table-wrap">
      <h2>{{ n }}단</h2>
      <ul>
        {% for row in rows %}<li>{{ row }}</li>{% endfor %}
      </ul>
    </div>
  {% endif %}
</body>
</html>"""


class GugudanWeb(GugudanApp):
    """Flask 기반 구구단 웹 앱."""

    def __init__(self, host: str = "127.0.0.1", port: int = 5000, debug: bool = False) -> None:
        super().__init__()
        self.host = host
        self.port = port
        self.debug = debug
        self._flask = Flask(__name__)
        self._register_routes()

    def _register_routes(self) -> None:
        engine = self.engine

        @self._flask.get("/")
        def index():
            return render_template_string(_HTML, n="", rows=None, error=None)

        @self._flask.post("/")
        def calculate():
            raw = request.form.get("n", "").strip()
            try:
                n = int(raw)
                rows = engine.generate_table(n)
                return render_template_string(_HTML, n=n, rows=rows, error=None)
            except ValueError:
                return render_template_string(_HTML, n=raw, rows=None, error="정수를 입력해 주세요."), 400

    def run(self) -> None:
        print(f"웹 서버 시작: http://{self.host}:{self.port}")
        self._flask.run(host=self.host, port=self.port, debug=self.debug)


def create_app() -> Flask:
    """WSGI 서버에서 사용할 Flask 앱 객체를 반환한다."""
    return GugudanWeb()._flask
