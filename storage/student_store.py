"""学生数据持久化 - JSON 文件存储"""

import json
import os

from core.models import Difficulty, KnowledgePoint, LifeStage, Skill, Student


class StudentStore:
    """学生数据持久化存储"""

    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)

    def save(self, student: Student) -> str:
        """保存学生数据到 JSON 文件"""
        data = {
            "name": student.name,
            "age": student.age,
            "stage": student.stage.value,
            "knowledge_points": [kp.to_dict() for kp in student.knowledge_points],
            "skills": [s.to_dict() for s in student.skills],
            "total_study_hours": student.total_study_hours,
            "motivation": student.motivation,
            "confidence": student.confidence,
        }
        filepath = os.path.join(self.data_dir, f"{student.name}.json")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return filepath

    def load(self, name: str) -> Student:
        """从 JSON 文件加载学生数据"""
        filepath = os.path.join(self.data_dir, f"{name}.json")
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        student = Student(
            name=data["name"],
            age=data["age"],
            stage=LifeStage(data["stage"]),
            total_study_hours=data.get("total_study_hours", 0),
            motivation=data.get("motivation", 80),
            confidence=data.get("confidence", 50),
        )
        student.knowledge_points = [
            KnowledgePoint.from_dict(kp) for kp in data.get("knowledge_points", [])
        ]
        student.skills = [
            Skill.from_dict(s) for s in data.get("skills", [])
        ]
        return student

    def list_students(self) -> list:
        """列出所有已保存的学生"""
        if not os.path.exists(self.data_dir):
            return []
        return [f[:-5] for f in os.listdir(self.data_dir) if f.endswith(".json")]
