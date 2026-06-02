"""구구단 핵심 계산 로직 — 입출력과 무관한 순수 도메인 클래스."""


class GugudanEngine:
    """구구단 계산 엔진.

    UI(CLI/Web 등)와 분리된 순수 계산 책임만 담당한다.
    """

    _ROW_TEMPLATE = "{n} x {i} = {result}"

    def generate_table(self, n: int) -> list[str]:
        """n단 구구단 결과를 문자열 리스트로 반환한다."""
        return [
            self._ROW_TEMPLATE.format(n=n, i=i, result=n * i)
            for i in range(1, 10)
        ]

    def generate_range(self, start: int = 2, end: int = 9) -> dict[int, list[str]]:
        """start~end 단 구구단 전체를 {단수: 결과리스트} 딕셔너리로 반환한다."""
        return {n: self.generate_table(n) for n in range(start, end + 1)}
