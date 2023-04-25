class BaseTranscriptorError(Exception):
    """Base class for all error for transcript process"""


class TranscriptDataMismatchLenError(BaseTranscriptorError):
    """Raised when len of data list for transcript data not match to original alphabet len"""


class WrongLangKeyForTranscriptor(BaseTranscriptorError):
    """Raised when key for transcription language does not exist for work map"""
