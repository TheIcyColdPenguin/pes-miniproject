from backend.base_model_types import Filter


def get_query(filters: Filter):
    criteria = []

    for column, ticked in filters.checkboxes.dict().items():
        if ticked:
            if len(ticked) > 1:
                criteria.append(f'{column} in {tuple(ticked)}')
            else:
                criteria.append(f'{column} == "{ticked[0]}"')

    for column, range in filters.ranges.dict().items():
        criteria.append(f'{column} between {range[0]} and {range[1]+1}')

    words = [char for i in filters.words.strip().split() for char in i.strip()]

    if words:
        criteria.append(f'model_name like "%{"%".join(words)}%"')

    if not criteria:
        return 'select * from laptop order by price desc limit 20'

    query = (
        'select * from laptop where ' +
        ' and '.join(criteria) +
        ' order by price desc limit 20'
    )

    print('\n'.join(criteria))

    print(query)

    return query
