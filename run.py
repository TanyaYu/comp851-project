import data_source
from filter import filter


data = data_source.download_leads()
filter(data)
