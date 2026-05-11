"""教育Agent - 教学规划、知识讲解、学习指导"""

import random
from datetime import datetime

from .curriculum import STAGE_CURRICULUM, EXPLANATIONS
from .models import Difficulty, LifeStage, KnowledgePoint, Student, Subject
from .question_bank import QuestionBank


class EduAgent:
    """教育Agent"""

    def __init__(self, student: Student, question_bank: QuestionBank = None):
        self.student = student
        self.question_bank = question_bank or QuestionBank()

    def introduce(self) -> str:
        return f"""
╔══════════════════════════════════════╗
║   🎓 EduAgent 教育系统 v1.0          ║
║   你好, {self.student.name}! 我是你的     ║
║   AI 私人教师，随时为你提供帮助。      ║
║   当前阶段: {self.student.stage.value}                      ║
╚══════════════════════════════════════╝
"""

    def get_curriculum(self) -> list:
        """当前阶段课程表"""
        subjects = STAGE_CURRICULUM.get(self.student.stage, [])
        return [s.value for s in subjects]

    def teach(self, subject: Subject, topic: str) -> str:
        """知识点讲解"""
        kp = next((k for k in self.student.knowledge_points
                    if k.name == topic and k.subject == subject), None)
        if not kp:
            diff = self._guess_difficulty(subject)
            kp = KnowledgePoint(name=topic, subject=subject, difficulty=diff)
            self.student.add_knowledge(kp)

        kp.practice_count += 1
        kp.last_practice = datetime.now().strftime("%Y-%m-%d %H:%M")

        explanations = EXPLANATIONS.get(subject, [
            f"好的，我们来学习 {topic}。这是一个重要的知识点。",
        ])
        explanation = random.choice(explanations)

        if kp.mastered:
            advice = "这个知识点你已经掌握了，我们来挑战一些更高难度的内容吧！"
            self.student.confidence = min(100, self.student.confidence + 2)
        elif kp.practice_count > 3:
            advice = f"你已经学习这个知识点 {kp.practice_count} 次了，再坚持一下！"
            self.student.motivation = max(0, self.student.motivation - 5)
        else:
            advice = "加油，学习新知识点总是需要时间的！"
            self.student.motivation = min(100, self.student.motivation + 3)

        self.student.total_study_hours += 0.5

        return f"""
📚 [{subject.value}] {topic}
━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 {explanation}

📝 已学习次数: {kp.practice_count}
💪 {advice}
━━━━━━━━━━━━━━━━━━━━━━━━━━
        """

    def generate_quiz(self, subject: Subject, count: int = 5,
                      difficulty: Difficulty = Difficulty.MEDIUM) -> list:
        """生成测验题"""
        return self.question_bank.generate_quiz(subject, count, difficulty)

    def study_plan(self) -> str:
        """生成学习计划"""
        curriculum = self.get_curriculum()
        weak_points = [k for k in self.student.knowledge_points if not k.mastered]
        strong_points = [k for k in self.student.knowledge_points if k.mastered]

        plan = f"""
📋 [{self.student.name}] 的学习计划
━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 当前阶段: {self.student.stage.value}
📖 当前课程: {', '.join(curriculum)}

📊 学习统计:
  • 总知识点: {len(self.student.knowledge_points)}
  • 已掌握: {len(strong_points)}
  • 待学习: {len(weak_points)}
  • 总学习时长: {self.student.total_study_hours:.1f}小时
  • 学习动力: {self.student.motivation:.0f}/100
  • 自信度: {self.student.confidence:.0f}/100
"""
        if weak_points:
            plan += "\n⚡ 推荐优先学习:\n"
            for kp in weak_points[:5]:
                plan += f"  → [{kp.subject.value}] {kp.name} ({kp.difficulty.value})\n"
        else:
            plan += "\n✨ 所有知识点已掌握！可以挑战更高难度。"

        plan += "━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        return plan

    def _guess_difficulty(self, subject: Subject) -> Difficulty:
        if self.student.stage in (LifeStage.KINDERGARTEN, LifeStage.PRIMARY):
            return Difficulty.EASY
        elif self.student.stage in (LifeStage.MIDDLE, LifeStage.HIGH):
            return Difficulty.MEDIUM
        return Difficulty.HARD
