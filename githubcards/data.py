from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from urllib.parse import quote_plus


@dataclass(init=True)
class SearchData(object):
    ratelimit_remaining: int  # data/rateLimit
    ratelimit_limit: int
    ratelimit_cost: int
    total: int  # data/search/issueCount
    results: list  # data/search/nodes
    query: str

    @property
    def escaped_query(self):
        return quote_plus(self.query)


@dataclass(init=True)
class IssueData(object):
    ratelimit_remaining: int  # data/rateLimit
    ratelimit_limit: int
    ratelimit_cost: int
    author_name: str  # data/issue/author
    author_url: str
    author_avatar_url: str
    issue_type: str
    number: int  # data/issue
    title: str
    url: str
    body_text: str
    state: str
    created_at: datetime
    is_draft: Optional[bool] = None
    mergeable_state: Optional[str] = None
    milestone: Optional[str] = None


@dataclass(init=True)
class IssueStatecolour(object):
    OPEN: 0x6cc644
    CLOSED: 0xbd2c00
    MERGED: 0x6e5494
