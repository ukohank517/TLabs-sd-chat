FROM python:3.6
ARG work_dir=/work/flask_script

WORKDIR $work_dir/

COPY conf/ $work_dir/conf/
COPY flask_script/ $work_dir/
COPY requirements.txt $work_dir

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# CMD ["python", "/work/mysql_flask/app.py"]