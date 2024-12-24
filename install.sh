# 删除旧的构建缓存
sudo docker-compose down
sudo docker system prune -f

# 重新构建和启动
sudo docker-compose up -d --build
