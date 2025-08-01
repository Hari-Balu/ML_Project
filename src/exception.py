import sys
from src.logger import logging


def error_message_detail(error, error_detail:sys):

    """
    This function is used to format the error message with details.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in script: [{file_name}] at line number: [{exc_tb.tb_lineno}] with message: [{str(error)}]"
    return error_message


class CustomException(Exception):
    
    """
    Custom Exception class to handle exceptions with detailed error messages.
    """

    def __init__(self, error, error_detail:sys):
        super().__init__(error)
        self.error_message = error_message_detail(error, error_detail)

    def __str__(self):
        return self.error_message
    


