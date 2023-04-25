# 基于Python 3.11.2镜像构建
FROM python:3.9

# 设置工作目录
WORKDIR /Django

# 将requirements.txt复制到容器中
COPY requirements.txt .

# 安装依赖
RUN pip install -r requirements.txt

# 将models目录复制到容器中
COPY model .

# 将当前目录下的所有文件复制到容器中
COPY fit5120Django fit5120Django
COPY fit5120backend fit5120backend
COPY model model
COPY . .

ENV WATCHPACK_POLLING=true

# 开放端口
EXPOSE 8000
EXPOSE 8889

# 运行命令
CMD ["sh", "/Django/startup.sh"]
CMD [ "sh", "/Django/test.sh" ]
