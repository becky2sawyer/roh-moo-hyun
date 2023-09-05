from president_speech.db.search import title, speech


def test_title():
    title(keyword="일본")


def test_speech():
    speech(keyword="일본")
