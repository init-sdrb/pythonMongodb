db = db.getSiblingDB("mydb");
db.content_tb.drop();

db.content_tb.insertMany([
    {
        "id": 1,
        "name": "Hari Bahadur",
        "address": "Koteshwor"
    },
    {
        "id": 2,
        "name": "Tanka Bahadur",
        "address": "Baneshwor"
    },
    {
        "id": 3,
        "name": "Ram Bahadur",
        "address": "Maitighar"
    },
]);
