"""Typed contracts shared across the router and specialist agents."""

from enum import Enum
from typing import Literal, Optional

from pydantic import BaseModel, EmailStr, Field


class Route(str, Enum):
    BACKGROUND = "background"
    FRAMEWORK = "framework"
    USE_CASE = "use_case"
    GENERAL = "general"


class RouteDecision(BaseModel):
    route: Route
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: str


class FrameworkAnswer(BaseModel):
    answer_markdown: str
    related_stage: Optional[Literal["Discover", "POC", "Build", "Embed"]] = None
    related_artefacts: list[str] = Field(default_factory=list)
    follow_up_prompt: Optional[str] = None


class BackgroundAnswer(BaseModel):
    answer_markdown: str
    themes: list[str] = Field(default_factory=list)
    follow_up_prompt: Optional[str] = None


class EngagementStage(str, Enum):
    DISCOVER = "Discover"
    POC = "POC"
    BUILD = "Build"
    EMBED = "Embed"


class EngagementType(str, Enum):
    QUICK_ASSESSMENT = "quick-assessment"
    PILOT_POC = "pilot-poc"
    FULL_DELIVERY = "full-delivery"
    ADVISORY_RETAINER = "advisory-retainer"


class UseCaseDiagnostic(BaseModel):
    business_area: str
    pain_point_summary: str
    matched_entry_point: Optional[str] = None
    recommended_stage: EngagementStage
    recommended_artefacts: list[str] = Field(default_factory=list)
    engagement_type: EngagementType
    reasoning: str
    confidence: float = Field(ge=0.0, le=1.0)


class Urgency(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class LeadCapture(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    company: Optional[str] = None
    use_case_summary: str
    urgency: Urgency = Urgency.MEDIUM
    source_agent: Literal["use_case", "framework", "background", "general"] = "use_case"


class UnansweredQuestion(BaseModel):
    question: str
    route_attempted: Route
    notes: Optional[str] = None
