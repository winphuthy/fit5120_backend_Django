# 基于Python 3.11.2镜像构建
FROM python:3.9

# 设置工作目录
WORKDIR /Django

# 将requirements.txt复制到容器中
COPY requirements.txt .

# 安装依赖
RUN pip install -r requirements.txt

# 将当前目录下的所有文件复制到容器中
COPY . .

ENV WATCHPACK_POLLING=true

# 开放端口
EXPOSE 8000

# 运行命令
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
#CMD [ "nohup", "python", "manage.py", "runserver", "0.0.0.0:8000", ">", "/dev/null", "2>&1", "&" ]