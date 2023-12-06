from pymongo import MongoClient
import sqlite3


def get_mongodb():
    uri = "mongodb+srv://artemF_web16:wubmyw-bysroK-0fuwnu@cluster0.94vozhi.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    try:
        db = client.web16_hw10
    except Exception as e:
        print(e)

    return db


# def conn_sqlite():
#     count_list_data = 10
#     tag_list = []
#     count_list = []
#     db_path = '../db.sqlite3'
#     conn = sqlite3.connect(db_path)
#     cur = conn.cursor()
#     result = cur.execute("select tag.name, count(*) from quotes_quote_tags left join quotes_tag as tag on tag.id = tag_id group by tag_id order by count(*) desc")
#     for res in result.fetchmany(size=count_list_data):
#         tag_list.append(res[0])
#         count_list.append(res[1])
#     return tag_list, count_list

# def conn_sqlite():
#
#     print(r)
#          # .group_by('tags').order_by().values()
#     return r
#
#
# if __name__ == '__main__':
#     result = conn_sqlite()
#     print(result)
