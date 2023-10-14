# Amanuma

https://yugo-harago.github.io/Amanuma/proto

run api
```
/> docker-compose build
/> docker-compose up
```

Run front
```
cd front
npm run dev
```

Run office
```
cd office
npm run dev
```

production
```
docker-compose --file docker-compose.prod.yaml up --build
```

To reset:
delete db.sqlite3 in /api
docker-compose exec api ./manage.py migrate
