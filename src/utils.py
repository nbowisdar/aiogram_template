from multiprocessing import Process
import shutil
import os

def execute_in_background(func, *args, **kwargs) -> Process:
    p = Process(target=func, args=args, kwargs=kwargs)
    p.start()
    return p

