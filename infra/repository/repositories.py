from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session

from domain.model.models import CallForPaper
from domain.model.repositories import CallForPaperRepository


class CallForPaperRepositoryImpl(CallForPaperRepository):
    def __init__(self, session: Session):
        self.db_session = session

    def get_all(self) -> List[CallForPaper]:
        stmt = select(CallForPaper).order_by(CallForPaper.end_date)
        return self.db_session.execute(stmt).scalars().all()

