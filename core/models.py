"""数据模型 - 学生、知识点、技能、事件等核心数据结构"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional


class Subject(Enum):
    MATH = "数学"
    CHINESE = "语文"
    ENGLISH = "英语"
    PHYSICS = "物理"
    CHEMISTRY = "化学"
    BIOLOGY = "生物"
    HISTORY = "历史"
    GEOGRAPHY = "地理"
    POLITICS = "政治"
    CS = "计算机科学"


class Difficulty(Enum):
    EASY = "简单"
    MEDIUM = "中等"
    HARD = "困难"


class LifeStage(Enum):
    KINDERGARTEN = "幼儿园"
    PRIMARY = "小学"
    MIDDLE = "初中"
    HIGH = "高中"
    UNIVERSITY = "大学"
    CAREER = "职业"
    RETIREMENT = "退休"


@dataclass
class KnowledgePoint:
    """知识点"""
    name: str
    subject: Subject
    difficulty: Difficulty
    mastered: bool = False
    practice_count: int = 0
    last_practice: Optional[str] = None

    def to_dict(self):
        return {
            "name": self.name,
            "subject": self.subject.value,
            "difficulty": self.difficulty.value,
            "mastered": self.mastered,
            "practice_count": self.practice_count,
            "last_practice": self.last_practice,
        }

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            name=d["name"],
            subject=Subject(d["subject"]),
            difficulty=Difficulty(d["difficulty"]),
            mastered=d.get("mastered", False),
            practice_count=d.get("practice_count", 0),
            last_practice=d.get("last_practice"),
        )


@dataclass
class Skill:
    """技能"""
    name: str
    level: int = 1
    experience: int = 0
    max_level: int = 10

    def add_exp(self, amount: int):
        self.experience += amount
        while self.experience >= self.level * 100 and self.level < self.max_level:
            self.experience -= self.level * 100
            self.level += 1
            print(f"  ✦ 技能 [{self.name}] 升级到 Lv.{self.level}！")

    def to_dict(self):
        return {"name": self.name, "level": self.level, "exp": self.experience}

    @classmethod
    def from_dict(cls, d: dict):
        return cls(name=d["name"], level=d["level"], experience=d["exp"])


@dataclass
class LifeEvent:
    """人生事件"""
    title: str
    description: str
    choices: list
    effects: dict


@dataclass
class Student:
    """学生模型"""
    name: str
    age: int
    stage: LifeStage = LifeStage.PRIMARY
    knowledge_points: list = field(default_factory=list)
    skills: list = field(default_factory=list)
    homework_history: list = field(default_factory=list)
    total_study_hours: float = 0.0
    motivation: float = 80.0
    confidence: float = 50.0

    def add_knowledge(self, kp: KnowledgePoint):
        self.knowledge_points.append(kp)

    def add_skill(self, skill: Skill):
        self.skills.append(skill)

    def get_mastery_rate(self, subject: Optional[Subject] = None) -> float:
        points = self.knowledge_points
        if subject:
            points = [k for k in points if k.subject == subject]
        if not points:
            return 0.0
        return sum(1 for k in points if k.mastered) / len(points) * 100

    def get_status(self) -> dict:
        return {
            "name": self.name,
            "age": self.age,
            "stage": self.stage.value,
            "knowledge_count": len(self.knowledge_points),
            "mastery_rate": round(self.get_mastery_rate(), 1),
            "motivation": round(self.motivation, 1),
            "confidence": round(self.confidence, 1),
            "study_hours": round(self.total_study_hours, 1),
            "skills": [s.to_dict() for s in self.skills],
        }
