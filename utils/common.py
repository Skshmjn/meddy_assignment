import os


def get_error_traceback(sys, e):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    function_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    return "%s || %s || %s || %s" % (exc_type, function_name, exc_tb.tb_lineno, e)
