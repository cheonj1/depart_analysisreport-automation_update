# scripts/db_connector.py 예시
from sqlalchemy import create_engine

# def get_engine():
#     db_url = "postgresql://violet:violetarasterized@deplan-analysis.cpmiuu620ld9.ap-northeast-2.rds.amazonaws.com:5432/depart_data"
#     return create_engine(db_url)

def get_engine():
    # 임시 staging DB
    db_url = "postgresql://violet:violetarasterized@deplan-analysis.cpmiuu620ld9.ap-northeast-2.rds.amazonaws.com:5432/depart_data_staging"
    return create_engine(db_url)