from dataclasses import dataclass

#data ingestion artifacts

@dataclass
class DataIngestionArtifacts:
    imbalance_data_file_path : str
    raw_data_file_path : str
    