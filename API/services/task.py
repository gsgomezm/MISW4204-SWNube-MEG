import json
from flask import app, jsonify, request
from flask_jwt_extended import create_access_token, current_user, decode_token, jwt_required
from flask_restful import Resource
from sqlalchemy import and_, asc, desc
from models.model import VideoSchema, db_session,  Video
import datetime
from celery import Celery

celery_app = Celery('task', broker='redis://localhost:6379/0')

class Task(Resource):
    @jwt_required()
    def get(self):
        # Get query parameters
        max_results = request.json["max"]
        order = request.json["order"]
      
        user_id =current_user.id
       
       
        if order ==1:
            tasks = db_session.query(Video).filter(Video.user_id == user_id).order_by(desc(Video.id))[:max_results]
        else:
            tasks = db_session.query(Video).filter(Video.user_id == user_id).order_by(asc(Video.id))[:max_results]

        # Return tasks as JSON
        video_schema = VideoSchema()
        return video_schema.dump(tasks, many=True)

    @jwt_required()
    def post(self):
        file_name = request.json["filename"]
        # Create a variable with the current date and time
        timestamp = datetime.datetime.now()
        user_id =current_user.id
        video = Video(name="video_dron",time_stamp=timestamp,path_folder=file_name,status="uploaded",user_id=user_id)
        db_session.add(video)
        db_session.commit()
        #logica cola
        celery_app.send_task('process_video.process_video', args=[video.id, video.path_folder])
        return  {"message": "Task created successfully"}