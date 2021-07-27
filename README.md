# 基于django+celery内部导航页面

### 效果图
--- 
![](img/demo.jpg)

### 运行
- 开发环境
```shell
export ENV=dev
```

### docker运行
- 构建镜像
  ```shell
    docker build -t pages:v1 .
    docker run -d -p 8000:80 pages:v1
  ```