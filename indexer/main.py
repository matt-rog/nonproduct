import argparse
import preprocessing.entity_resolution
import search


def process(query):
    entities = preprocessing.entity_resolution.resolve(query)

def main():

    parser = argparse.ArgumentParser("indexer")
    parser.add_argument('-m', '--mode', choices=["adhoc", "poll"])
    parser.add_argument('-q', '--query')
    args = parser.parse_args()

    if args.mode == "adhoc" and args.query:
        process(args.query)

if __name__ == "__main__":
    main()
