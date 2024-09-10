import sys


# why we need to create custom exception class?
# we want to know more about the exception that occurred
# we are not satisfied only with message, we want every detail about the exception(such as type of exception, line number, etc)
class customException(Exception):  # inheriting predefined Exception class

    def __init__(self, error_message, error_details: sys):

        # error_details is an object of sys module
        # toh error_details.exc_info() == sys.exc_info()

        self.error_message = error_message
        _, _, execution_traceback = (
            error_details.exc_info()
        )  # exc_info() returns a tuple of 3 elements (type of exception, exception object, traceback object)

        # tb_lineno is an attribute of traceback object which returns the line number where the exception occurred
        self.line_number = execution_traceback.tb_lineno

        # tb_frame is an attribute of traceback object which returns the frame object or file of the traceback object
        self.file_name = execution_traceback.tb_frame.f_code.co_filename

    def __str__(self):
        return "\n\nERROR OCCURED IN PYTHON SCRIPT NAME : [{0}] \n\nIN LINE NUMBER : [{1}]\n\nERROR MESSAGE :[{2}]\n\n".format(
            self.file_name, self.line_number, str(self.error_message)
        )


# to execute this module in standalone mode
if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:  # e is an object of Exception class
        raise customException(e, sys)
        # print(e)


# NEECHE WALA CODE SIRF HUME MESSAGE HI DE RHA THA BUT HUME SAB KUCH CHAHIYE THA TOH HUMNE CUSTOM EXCEPTION CLASS BANAYA JISME HUMNE SAB KUCH PRINT KARWAYA
# try:
#     a=1/0
# except Exception as e: # e is an object of Exception class
#     print(e)
