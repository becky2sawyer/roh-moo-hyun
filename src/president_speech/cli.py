from president_speech.db.search import title, speech
import argparse


def search():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-t", "--title", action="store_true", help="Search speech title like")
    group.add_argument("-s", "--speech", action="store_true", help="Search speech title speech")
    parser.add_argument("keyword", type=str, help="Search word")

    args = parser.parse_args()

    if args.title:
        title(args.keyword)

    elif args.speech:
        speech(args.keyword)
    else:
        print("An undefined functional call has occurred.")
