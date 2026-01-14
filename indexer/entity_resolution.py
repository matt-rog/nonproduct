import search

# ER determines if the query is a product or a company. 
# If it is a product, it searches for and fills out any missing company information.
# The new product entity, and any new company entities, are then queued for claim resolution.
def resolve(term):
    init_context = search.search(term)
