def post_to_base(prompt, collection):
    try:
        collection.update_one({'title': prompt['table']},
                              {'$set': prompt['body']}, upsert=True)
        return "ОК"
    except Exception as exc:
        return f"Error {exc}"
