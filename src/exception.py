import sys
import logger

def err_msg_details(err, err_detail:sys):
    _, _, exc_tb = err_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    err_msg = f"Error occurred: Script[{file_name}] | Line[{exc_tb.tb_lineno}] | Error Message:[{str(err)}]"
    
    return err_msg

class MLCustomException(Exception):
    def __init__(self, err_msg, err_detail:sys):
        super().__init__(err_msg)
        self.err_msg = err_msg_details(err_msg, err_detail)
        
    def __str__(self):
        return self.err_msg
    

# if __name__ == "__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         logger.logging.error(MLCustomException(e, sys))
#         raise MLCustomException(e, sys)