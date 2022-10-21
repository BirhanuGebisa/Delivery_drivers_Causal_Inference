import sys
import os
import pandas as pd
import dvc.api
from file_log import logger


sys.path.append(os.path.abspath(os.path.join("../scripts/")))

class ReadData():
    def dvc_get_data(self, path, version='v-1') :
        try:
            repo = "/home/sucess/10-academy/week-9/Delivery_drivers_Causal_Inference"
            data_url = dvc.api.get_url(path=path, repo=repo, rev=version)
            data_url = str(data_url)[6:]
            df = pd.read_csv(data_url, sep=",", low_memory=False)
            logger.info("Data read")
        except Exception as e:
            df = None
            logger.error(e)
        return df