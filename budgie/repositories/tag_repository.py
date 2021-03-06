from budgie.db.run_sql import run_sql

from budgie.models.tag import Tag
from budgie.models.transaction import Transaction
from budgie.models.merchant import Merchant


# save
def save(tag):
    sql = "INSERT INTO tags (category) VALUES (%s) RETURNING id"
    values = [tag.category]
    results = run_sql(sql, values)
    tag.id = results[0]['id']
    return tag

# edit 
def update(tag):
    sql = "UPDATE tags SET (category) = (%s) WHERE id = %s"
    values = [tag.category, tag.id]
    run_sql(sql, values)

# select_all
def select_all():
    tags = []

    sql = "SELECT * FROM tags"
    results = run_sql(sql)
    for row in results:
        tag = Tag(row['category'], row['id'])
        tags.append(tag)
    return tags 


# select(id)
def select(id):
    tag = None
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag = Tag(result['category'], result['id'])
    return tag


# delete_all
def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)

# delete(id)
def delete(id):
    sql = "DELETE FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# show all merchants assigned to a tag
def merchants(tag):
    merchants = []

    sql = "SELECT merchants.* FROM merchants INNER JOIN transactions ON transactions.merchant_id = merchants.id WHERE tag_id = %s"
    values = [tag.id]
    results = run_sql(sql, values)

    for row in results:
        merchant = Merchant(row['name'], row['id'])
        merchants.append(merchant)

    return merchants