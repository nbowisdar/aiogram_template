## Installation

Run python command to install all packages

```bash
python install_requirements.py
```

## Alembic (Migrations)

If you want to use alembic that is highly recommended
Firstly delete these from .gitignore
_alembic.ini
alembic/_

Then initialize alembic

```bash
alembic init alembic
```

Now you need to update config files

env.py -> Add these lines (or similar)

```
from app.structure.models import Base
target_metadata = Base.metadata
```

alembic.init -> update url to database

```
# sqlalchemy.url = driver://user:pass@localhost/dbname
sqlalchemy.url = sqlite:///db.sqlite3
```

Create first migration, and applied it

```bash
alembic revision --autogenerate -m "Create users table"
alembic upgrade head
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
