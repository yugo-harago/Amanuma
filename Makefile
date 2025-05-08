# Start Docker Compose services
django:
	docker-compose -f docker-compose.yaml up -d

# Stop Docker Compose services
stop:
	docker-compose -f docker-compose.yaml down

# Start Vite projects
view:
	nohup sh -c "cd front && npm run dev" >/dev/null 2>&1 &
	nohup sh -c "cd office && npm run dev" >/dev/null 2>&1 &

# Run the complete setup
init: django view