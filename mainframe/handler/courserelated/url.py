#coding: utf-8

from handler.courserelated import upload_material

url = [
    (r'/relate/uploadmaterial', upload_material.UploadCourseMaterial)
]
