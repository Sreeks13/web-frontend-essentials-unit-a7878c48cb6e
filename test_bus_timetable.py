from pathlib import Path
from html.parser import HTMLParser


class HTMLChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)

    def handle_data(self, data):
        self.text.append(data)


def load_html():
    return Path("bus_timetable.html").read_text(encoding="utf-8")


def test_route_42_timetable():
    html = load_html()

    assert "<table" in html
    assert "</table>" in html
    assert "Route 42" in html


def test_timetable_has_caption():
    html = load_html()

    assert "<caption" in html
    assert "Route 42" in html


def test_bus_stop_image():
    html = load_html()

    assert "<img" in html
    assert "alt=" in html


def test_audio_announcement():
    html = load_html()

    assert "<audio" in html
    assert "controls" in html


def test_video_player():
    html = load_html()

    assert "<video" in html
    assert "controls" in html


def test_public_transport_footer():
    html = load_html()

    assert "<footer" in html