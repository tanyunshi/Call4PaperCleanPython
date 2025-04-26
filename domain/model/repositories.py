# Repository interfaces

from abc import ABC, abstractmethod
from typing import List
from .models import CallForPaper, Talk, Conference, Speaker, TalkDraft, Slot, Trace


class CallForPaperRepository(ABC):
    @abstractmethod
    def find_submissions(self, call_for_paper_id: int) -> List[Talk]:
        """Find all submissions for a specific call for papers."""
        pass

    @abstractmethod
    def find_all(self, conference_id: int) -> List[CallForPaper]:
        """Find all papers for a specific conference."""
        pass

    @abstractmethod
    def create(self, conference_id: int, call_for_paper: CallForPaper) -> CallForPaper:
        """Create a new call for papers."""
        pass

    @abstractmethod
    def update(self, call_for_paper: CallForPaper) -> CallForPaper:
        """Update an existing call for papers."""
        pass

    @abstractmethod
    def delete(self, call_for_paper_id: int) -> None:
        """Delete a call for papers."""
        pass

    @abstractmethod
    def find_by_id(self, call_for_paper_id: int) -> CallForPaper:
        """Find a call for papers by its ID."""
        pass

    
class ConferenceRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[Conference]:
        """Find all conferences."""
        pass

    @abstractmethod
    def find_by_id(self, conference_id: int) -> Conference:
        """Find a conference by its ID."""
        pass

    @abstractmethod
    def create(self, call_for_paper: CallForPaper) -> Conference:
        """Create a new conference."""
        pass

    @abstractmethod
    def update(self, call_for_paper: CallForPaper) -> Conference:
        """Update an existing conference."""
        pass

    @abstractmethod
    def delete(self, conference_id: int) -> None:
        """Delete a conference."""
        pass


class SlotRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[Slot]:
        """Find all slots."""
        pass

    @abstractmethod
    def find_by_id(self, slot_id: int) -> Slot:
        """Find a slot by its ID."""
        pass

    @abstractmethod
    def create(self, trace_id: int, slot: Slot) -> Slot:
        """Create a new slot."""
        pass

    @abstractmethod
    def update(self, slot: Slot) -> Slot:
        """Update an existing slot."""
        pass

    @abstractmethod
    def delete(self, slot_id: int) -> None:
        """Delete a slot."""
        pass


class SpeakerRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[Speaker]:
        """Find all speakers."""
        pass

    @abstractmethod
    def find_by_id(self, speaker_id: int) -> Speaker:
        """Find a speaker by its ID."""
        pass

    @abstractmethod
    def create(self, speaker: Speaker) -> Speaker:
        """Create a new speaker."""
        pass

    @abstractmethod
    def update(self, speaker: Speaker) -> Speaker:
        """Update an existing speaker."""
        pass

    @abstractmethod
    def delete(self, speaker_id: int) -> None:
        """Delete a speaker."""
        pass


class TalkDraftRepository(ABC):
    @abstractmethod
    def find_all(self, speaker_id: int) -> List[TalkDraft]:
        """Find all talks."""
        pass

    @abstractmethod
    def find_by_id(self, talk_id: int) -> TalkDraft:
        """Find a talk by its ID."""
        pass

    @abstractmethod
    def create(self, talk: TalkDraft) -> TalkDraft:
        """Create a new talk."""
        pass

    @abstractmethod
    def update(self, talk: TalkDraft) -> TalkDraft:
        """Update an existing talk."""
        pass

    @abstractmethod
    def delete(self, talk_id: int) -> None:
        """Delete a talk."""
        pass


class TalkRepository(ABC):
    @abstractmethod
    def find_all(self, speaker_id: int) -> List[Talk]:
        """Find all talks."""
        pass

    @abstractmethod
    def find_by_id(self, talk_id: int) -> Talk:
        """Find a talk by its ID."""
        pass

    @abstractmethod
    def create(self, talk: Talk) -> Talk:
        """Create a new talk."""
        pass

    @abstractmethod
    def update(self, talk: Talk) -> Talk:
        """Update an existing talk."""
        pass

    @abstractmethod
    def delete(self, talk_id: int) -> None:
        """Delete a talk."""
        pass


class TraceRepository(ABC):
    @abstractmethod
    def find_all(self, conference_id: int) -> List[Trace]:
        """Find all traces."""
        pass

    @abstractmethod
    def find_by_id(self, trace_id: int) -> Trace:
        """Find a trace by its ID."""
        pass

    @abstractmethod
    def create(self, conference_id: int, trace: Trace) -> Trace:
        """Create a new trace."""
        pass

    @abstractmethod
    def update(self, trace: Trace) -> Trace:
        """Update an existing trace."""
        pass

    @abstractmethod
    def delete(self, trace_id: int) -> None:
        """Delete a trace."""
        pass
    