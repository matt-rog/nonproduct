import argparse
import search

# ER determines if the query is a product or a company. 
# If it is a product, it searches for and fills out any missing company information.
# The new product entity, and any new company entities, are then queued for claim resolution.
def entity_resolution(query):
    search.search(query)

def process(query):
    entities = entity_resolution(query)
   
def main():

    parser = argparse.ArgumentParser("indexer")
    parser.add_argument('-m', '--mode', choices=["adhoc", "poll"])
    parser.add_argument('-q', '--query')
    args = parser.parse_args()

    if args.mode == "adhoc" and args.query:
        process(args.query)

if __name__ == "__main__":
    main()
