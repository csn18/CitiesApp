request_args = {"countries_id": "1", "page": "d"}
try:
    page_id = int(request_args.get('page', 1))
except ValueError:
    page_id = 1

pseudo_limit = page_id + 1
print(pseudo_limit)
