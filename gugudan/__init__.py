"""gugudan 패키지.

하위 호환성을 위해 기존 모듈 수준 함수와 상수를 그대로 노출한다.
새 코드에서는 GugudanEngine / GugudanCLI 등 클래스를 직접 사용하도록 한다.
"""

from gugudan.engine import GugudanEngine
from gugudan.base import GugudanApp
from gugudan.cli import GugudanCLI, QUIT_TOKENS

__all__ = [
    "GugudanEngine",
    "GugudanApp",
    "GugudanCLI",
    "QUIT_TOKENS",
    # 하위 호환 함수
    "multiplication_table",
    "print_multiplication_table",
    "parse_input",
]

_engine = GugudanEngine()


def multiplication_table(n: int) -> list[str]:
    """n단 구구단 결과 리스트 반환 (하위 호환용)."""
    return _engine.generate_table(n)


def print_multiplication_table(n: int) -> None:
    """n단 구구단을 stdout에 출력 (하위 호환용)."""
    for line in multiplication_table(n):
        print(line)


def parse_input(raw: str) -> int | None:
    """사용자 입력 문자열 파싱 (하위 호환용)."""
    token = raw.strip()
    if token.lower() in QUIT_TOKENS:
        return None
    return int(token)
