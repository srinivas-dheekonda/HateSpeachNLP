from HateSpeech.logger import logging
from HateSpeech.exception import CustomException
import sys
from HateSpeech.configuration.GCP_syncer import GCloudSync

obj = GCloudSync()
obj.sync_folder_from_gcloud("hate-speech2024","")
