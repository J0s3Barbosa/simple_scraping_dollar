from dataclasses import dataclass
import os

class FileUtils:
   def get_file(file_name):
      full_path = os.path.realpath(__file__)
      path, filename = os.path.split(full_path)
      path_file_name = fr"{path}/{file_name}"
      return path_file_name



