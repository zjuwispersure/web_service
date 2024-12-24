# 删除旧的构建缓存
docker-compose down
docker system prune -f

# 重新构建和启动
sudo docker-compose up -d --build
