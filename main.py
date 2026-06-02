"""구구단 앱 실행 진입점.

--mode 옵션으로 실행 인터페이스를 선택한다.
지원 모드: cli, web
"""

import argparse

from gugudan.cli import GugudanCLI
from gugudan.web import GugudanWeb

_APP_REGISTRY: dict[str, type] = {
    "cli": GugudanCLI,
    "web": GugudanWeb,
}


def main() -> None:
    parser = argparse.ArgumentParser(description="구구단 앱")
    parser.add_argument(
        "--mode",
        choices=list(_APP_REGISTRY.keys()),
        default="cli",
        help="실행 모드 (기본값: cli)",
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="웹 서버 호스트 (web 모드 전용, 기본값: 127.0.0.1)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=5000,
        help="웹 서버 포트 (web 모드 전용, 기본값: 5000)",
    )
    args = parser.parse_args()

    if args.mode == "web":
        app = GugudanWeb(host=args.host, port=args.port)
    else:
        app = _APP_REGISTRY[args.mode]()

    try:
        app.run()
    except (KeyboardInterrupt, EOFError):
        print("\n종료합니다.")


if __name__ == "__main__":
    main()
