from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class TalkKind(Enum):
    QUICKIE = "QUICKIE"
    CONFERENCE = "CONFERENCE"
    DEEP_DRIVE = "DEEP_DRIVE"


class TalkState(Enum):
    PROPOSED = "PROPOSED"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    PUBLISHED = "PUBLISHED"
    WITHDRAWN = "WITHDRAWN"


class TalkLevel(Enum):
    BEGINNER = "BEGINNER"
    INTERMEDIATE = "INTERMEDIATE"
    ADVANCED = "ADVANCED"


@dataclass
class CallForPaper:
    id: int
    end_date: datetime


@dataclass
class Conference:
    id: int
    name: str
    call_for_papers: CallForPaper


@dataclass
class Speaker:
    id: int
    first_name: str
    last_name: str


@dataclass
class Talk:
    id: int
    cfp_id: int
    title: str
    summary: str
    speakers: list[Speaker]
    talk_state: TalkState
    talk_level: TalkLevel
    talk_state: TalkState = TalkState.PROPOSED


@dataclass
class TalkDraft:
    id: int
    title: str
    summary: str
    speakers: list[Speaker]


@dataclass
class Slot:
    id: int
    start_date: datetime
    end_date: datetime
    location: str
    talk_kind: TalkKind
    talk: Talk


@dataclass
class Trace:
    id: int
    name: str
    slots: list[Slot]
