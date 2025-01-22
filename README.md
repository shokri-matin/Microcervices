### To build project
```bash
# To build authservice
build -t authservice:latest -f Powder/auth_service/Dockerfile.build Powder/auth_service/.
# To build logservice
build -t logservice:latest -f Powder/log_service/Dockerfile.build Powder/log_service/.
# To Build and Run Services
cd Powder
docker-compose build
docker-compose up -d
```