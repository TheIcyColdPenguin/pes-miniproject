from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sqlite3 import connect
from backend.construct_query import get_query

from backend.base_model_types import Filter


app = FastAPI()
connection = connect('database')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173', 'http://localhost:4173'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fields = [
    'id',
    'manufacturer',
    'model_name',
    'category',
    'screen_diag',
    'screen_res',
    'screen_type',
    'screen_touch',
    'cpu_vendor',
    'cpu',
    'ram',
    'storage',
    'storage_type',
    'gpu_vendor',
    'gpu',
    'os',
    'os_version',
    'mass',
    'price',
]


@app.get('/filters')
async def filters():
    distinct_checkboxes = [
        'manufacturer',
        'category',
        'screen_res',
        'screen_touch',
        'cpu_vendor',
        'storage_type',
        'os'
    ]

    checkboxes = {
        field: [
            i[0] for i in
            connection.execute(
                f'select distinct {field} from laptop'
            ).fetchall()
        ]
        for field in distinct_checkboxes
    }

    distinct_ranges = [
        'screen_diag', 'ram', 'storage', 'mass', 'price'
    ]

    ranges = {
        field: connection.execute(
            f'select  min({field}), max({field}) from laptop'
        ).fetchone()
        for field in distinct_ranges
    }

    return {'checkboxes': checkboxes, 'ranges': ranges}


@app.post("/laptops")
async def laptops(data: Filter):
    query = get_query(data)
    data = connection.execute(query).fetchall()

    new_data = [
        {
            field: v[i] for i, field in enumerate(fields)
        } for v in data
    ]

    return new_data
