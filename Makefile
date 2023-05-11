# Start Docker Compose services
django:
	docker-compose -f docker-compose.yml up -d

# Stop Docker Compose services
stop:
	docker-compose -f docker-compose.yaml down

# Start Vite projects
view:
	powershell -ExecutionPolicy ByPass -File start-view.ps1

# Run the complete setup
init: django view
