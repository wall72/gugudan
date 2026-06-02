import pytest

from gugudan import multiplication_table, parse_input, print_multiplication_table
from gugudan.web import GugudanWeb


def test_multiplication_table_length():
    assert len(multiplication_table(3)) == 9


def test_multiplication_table_values():
    rows = multiplication_table(7)
    assert rows[0] == "7 x 1 = 7"
    assert rows[8] == "7 x 9 = 63"


def test_multiplication_table_zero():
    rows = multiplication_table(0)
    assert all(row.endswith("= 0") for row in rows)


def test_multiplication_table_negative():
    rows = multiplication_table(-2)
    assert rows[2] == "-2 x 3 = -6"


def test_print_multiplication_table_output(capsys):
    print_multiplication_table(2)
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured[0] == "2 x 1 = 2"
    assert captured[-1] == "2 x 9 = 18"


@pytest.mark.parametrize("raw", ["q", "Q", "quit", "exit", "  q  "])
def test_parse_input_quit(raw):
    assert parse_input(raw) is None


@pytest.mark.parametrize("raw,expected", [("5", 5), (" 9 ", 9), ("-3", -3)])
def test_parse_input_number(raw, expected):
    assert parse_input(raw) == expected


def test_parse_input_invalid_raises():
    with pytest.raises(ValueError):
        parse_input("abc")


def test_web_index_get_ok():
    app = GugudanWeb()._flask
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert "구구단" in response.get_data(as_text=True)


def test_web_calculate_post_ok():
    app = GugudanWeb()._flask
    client = app.test_client()

    response = client.post("/", data={"n": "7"})
    body = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "7단" in body
    assert "7 x 9 = 63" in body


def test_web_calculate_post_invalid_returns_400():
    app = GugudanWeb()._flask
    client = app.test_client()

    response = client.post("/", data={"n": "abc"})
    body = response.get_data(as_text=True)

    assert response.status_code == 400
    assert "정수를 입력해 주세요." in body
