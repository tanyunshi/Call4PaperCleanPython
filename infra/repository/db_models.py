from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass



class SpeakerModel(Base):
    __tablename__ = "speakers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)


class ConferenceModel(Base):
    __tablename__ = "conferences"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    
    call_for_paper_id: Mapped[int] = mapped_column(ForeignKey("call_for_papers.id"), nullable=False)
    call_for_paper = relationship("CallForPaperModel", back_populates="conference")


class CallForPaperModel(Base):
    __tablename__ = "call_for_papers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    end_date: Mapped[DateTime] = mapped_column(nullable=False)
    conference = relationship("ConferenceModel", back_populates="call_for_paper") 


association_speaker_talk = Table(
    "association_speaker_talk",
    Base.metadata,
    Column("speaker_id", ForeignKey("speakers.id")),
    Column("talk_id", ForeignKey("talks.id")),
)


association_talk_cfp = Table(
    "association_talk_cfp",
    Base.metadata,
    Column("talk_id", ForeignKey("talks.id")),
    Column("cfp_id", ForeignKey("call_for_papers.id")),
)


class TalkModel(Base):
    __tablename__ = "talks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    talk_state: Mapped[str] = mapped_column(String(50), nullable=False)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    summary: Mapped[str] = mapped_column(String(500), nullable=False)

    speakers: Mapped[list[SpeakerModel]] = relationship(
        "SpeakerModel",
        secondary=association_speaker_talk,
        back_populates="talks",
    )

    submissions: Mapped[list[CallForPaperModel]] = relationship(
        "CallForPaperModel",
        secondary=association_talk_cfp,
        back_populates="talks",
    )


class TraceModel(Base):
    __tablename__ = "traces"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    
    conference_id: Mapped[int] = mapped_column(ForeignKey("conferences.id"), nullable=False)
    conference = relationship("ConferenceModel", back_populates="traces")

    slots: Mapped[list["SlotModel"]] = relationship("SlotModel", back_populates="trace")



class SlotModel(Base):
    __tablename__ = "slots"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    start_date: Mapped[DateTime] = mapped_column(nullable=False)
    end_date: Mapped[DateTime] = mapped_column(nullable=False)

    talk_id: Mapped[int] = mapped_column(ForeignKey("talks.id"), nullable=False)
    talk = relationship("TalkModel", back_populates="slots")

    trace_id: Mapped[int] = mapped_column(ForeignKey("traces.id"), nullable=False)
    trace = relationship("TraceModel", back_populates="slots")