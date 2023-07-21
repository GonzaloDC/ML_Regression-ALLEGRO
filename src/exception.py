
import sys 

def error_detail(error,details:sys):
    _,_,exc_tb = details.exc_info()
    error_msg = "An error has occurred in the file [{0}], line number [{1}] with the next error: [{2}]".format(exc_tb.tb_frame.f_code.co_filename,exc_tb.tb_lineno,str(error))

    return error_msg


class CustomException(Exception):
    def __init__(self, error_msg, details:sys):
        super().__init__(error_msg)
        self.error_msg=error_detail(error_msg,details=details)


    def __str__(self) -> str:
        return self.error_msg


#test

if __name__=="__main__":
    try:
        x=1/0
    except Exception as e:
        raise CustomException(e,sys)