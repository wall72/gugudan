# 구구단 앱

터미널(CLI)과 웹(Flask) 인터페이스를 모두 지원하는 구구단 출력 앱입니다.

---

## 개요

- 단수를 입력하면 해당 구구단(1~9)을 출력합니다.
- CLI와 Web 두 가지 모드를 `--mode` 옵션으로 선택할 수 있습니다.
- `GugudanEngine`(순수 계산) → `GugudanApp`(추상 기반) → `GugudanCLI` / `GugudanWeb` 구조로 설계되어 새로운 인터페이스를 쉽게 추가할 수 있습니다.

---

## 아키텍처

```
gugudan/
  engine.py   — GugudanEngine: 순수 계산 로직 (UI 독립)
  base.py     — GugudanApp (ABC): 모든 앱의 공통 계약
  cli.py      — GugudanCLI: 터미널 대화형 인터페이스
  web.py      — GugudanWeb: Flask 기반 웹 인터페이스
  __init__.py — 하위 호환 함수 노출
main.py       — 실행 진입점 (--mode 옵션으로 인터페이스 선택)
tests/
  test_gugudan.py — pytest 단위 테스트
```

---

## 빌드 / 환경 설정

Python 3.12 이상이 필요합니다.

```bash
# 가상환경 생성 및 활성화
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS / Linux

# 런타임 의존성 설치
pip install -r requirements.txt

# 개발 의존성 설치 (테스트 도구 포함)
pip install -r requirements-dev.txt

# (동일 의미) pyproject.toml 기준 직접 설치
pip install .
pip install .[dev]
```

의존성의 단일 소스는 [pyproject.toml](pyproject.toml)이며, requirements 파일은 이를 참조하는 호환용 엔트리입니다.

---

## 실행

### CLI 모드 (기본)

```bash
python main.py
# 또는
python main.py --mode cli
```

실행 후 단수를 입력하면 구구단을 출력합니다. `q` / `quit` / `exit` 입력 또는 `Ctrl+C`로 종료합니다.

### 웹 모드

```bash
python main.py --mode web
```

브라우저에서 http://127.0.0.1:5000 에 접속합니다.

포트 및 호스트 변경:

```bash
python main.py --mode web --host 0.0.0.0 --port 8080
```

---

## 테스트

```bash
pytest
```

pytest 설정은 [pyproject.toml](pyproject.toml)의 `[tool.pytest.ini_options]`에서 관리합니다.

---

## 배포

웹 모드는 Flask 내장 서버를 사용하므로 **프로덕션 환경에서는 Gunicorn 등 WSGI 서버를 사용**해야 합니다.

```bash
pip install gunicorn
gunicorn "gugudan.web:create_app()"
```

또는 `GugudanWeb()._flask` 애플리케이션 객체를 직접 WSGI 서버에 전달하세요.

---

## 트러블슈팅

| 증상 | 원인 | 해결 |
|---|---|---|
| `ModuleNotFoundError: flask` | Flask 미설치 | `pip install -r requirements.txt` |
| 포트 충돌 | 5000번 포트 사용 중 | `--port` 옵션으로 변경 |
| `정수를 입력해 주세요.` (CLI) | 숫자가 아닌 값 입력 | 정수 입력 |
| 웹 페이지 400 응답 | 숫자가 아닌 값 입력 | 정수 입력 |
