from pydantic import BaseModel

#Pydantic is a data validation and parsing library

'''
here the InputData class is defined using Pydantic's BaseModel.
This class has two attributes: age and cholesterol, both of which are integers.
It is not just any random class; it is specifically designed to validate and parse input data for the FastAPI application.
'''
class InputData(BaseModel):
    age: int
    cholesterol: int
