"""구구단 앱의 추상 기반 클래스 — 다양한 인터페이스 확장의 공통 계약."""

from abc import ABC, abstractmethod

from gugudan.engine import GugudanEngine


class GugudanApp(ABC):
    """CLI, Web 등 모든 구구단 앱이 상속해야 하는 추상 기반 클래스.

    Attributes:
        engine: 구구단 계산을 담당하는 GugudanEngine 인스턴스.
    """

    def __init__(self) -> None:
        self.engine = GugudanEngine()

    @abstractmethod
    def run(self) -> None:
        """앱을 실행한다. 하위 클래스에서 반드시 구현해야 한다."""
        ...
