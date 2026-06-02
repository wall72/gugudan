"""터미널(CLI) 기반 구구단 앱."""

from gugudan.base import GugudanApp

QUIT_TOKENS: frozenset[str] = frozenset({"q", "quit", "exit"})


class GugudanCLI(GugudanApp):
    """표준 입출력(stdin/stdout)을 사용하는 대화형 구구단 앱."""

    def parse_input(self, raw: str) -> int | None:
        """사용자 입력 문자열을 파싱한다.

        Returns:
            종료 토큰이면 None, 그 외에는 정수. 정수 변환 불가 시 ValueError.
        """
        token = raw.strip()
        if token.lower() in QUIT_TOKENS:
            return None
        return int(token)

    def read_number(self) -> int | None:
        """유효한 입력이 들어올 때까지 사용자 입력을 반복 요청한다."""
        while True:
            raw = input("구구단 숫자를 입력하세요 (종료: q): ")
            try:
                return self.parse_input(raw)
            except ValueError:
                print("정수를 입력해 주세요.")

    def run(self) -> None:
        print("=== 구구단 출력 앱 ===")
        while True:
            number = self.read_number()
            if number is None:
                print("종료합니다.")
                break
            for line in self.engine.generate_table(number):
                print(line)
            print()
