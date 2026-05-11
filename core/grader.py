"""智能批改器 - 测验批改、作文批改、批量统计"""

import random


class Grader:
    """智能批改器"""

    def __init__(self):
        self.grading_records = []

    def grade_quiz(self, student, quiz: list, user_answers: list) -> dict:
        """批改测验"""
        correct = 0
        total = len(quiz)
        details = []

        for i, q in enumerate(quiz):
            if i >= len(user_answers):
                details.append({
                    "index": q["index"], "question": q["question"],
                    "user_answer": "未作答", "correct_answer": q["answer"],
                    "is_correct": False,
                })
                continue

            user_ans = str(user_answers[i]).strip()
            correct_ans = str(q["answer"]).strip()
            is_correct = user_ans == correct_ans
            if is_correct:
                correct += 1
            details.append({
                "index": q["index"], "question": q["question"],
                "user_answer": user_ans, "correct_answer": correct_ans,
                "is_correct": is_correct,
            })

        score = round(correct / total * 100, 1) if total > 0 else 0
        grade = self._get_grade(score)

        student.motivation = min(100, student.motivation + (score - 60) * 0.2)
        student.confidence = min(100, student.confidence + (score - 50) * 0.15)

        result = {
            "student": student.name, "score": score, "grade": grade,
            "correct": correct, "total": total, "details": details,
        }
        self.grading_records.append(result)
        return result

    def grade_essay(self, student, title: str, content: str,
                    criteria: dict = None) -> dict:
        """智能批改作文"""
        criteria = criteria or {
            "structure": 25, "content": 25, "language": 25,
            "logic": 15, "creativity": 10,
        }

        content_len = len(content)
        paragraphs = content.count('\n') + 1

        scores = {
            "structure": min(25, int(paragraphs * 5 + random.randint(-3, 3))),
            "content": min(25, int(content_len / 10 + random.randint(-3, 3))),
            "language": min(25, int(content_len / 15 + random.randint(-5, 5))),
            "logic": min(15, int(paragraphs * 3 + random.randint(-2, 2))),
            "creativity": random.randint(3, 10),
        }

        total = sum(scores.values())
        max_total = sum(criteria.values())
        percentage = round(total / max_total * 100, 1)
        feedback = self._generate_essay_feedback(scores, criteria, percentage)

        return {
            "title": title, "student": student.name,
            "scores": scores, "total": total, "max_score": max_total,
            "percentage": percentage, "grade": self._get_grade(percentage),
            "feedback": feedback,
        }

    def batch_grade(self, records: list) -> dict:
        """批量批改统计"""
        if not records:
            return {}

        scores = [r.get("score", 0) or 0 for r in records]
        grade_count = {}
        for r in records:
            g = r.get("grade", "D")
            grade_count[g] = grade_count.get(g, 0) + 1

        return {
            "count": len(records),
            "average": round(sum(scores) / len(scores), 1),
            "highest": max(scores),
            "lowest": min(scores),
            "grade_distribution": grade_count,
        }

    def _get_grade(self, score: float) -> str:
        if score >= 95:
            return "S (卓越)"
        elif score >= 85:
            return "A (优秀)"
        elif score >= 75:
            return "B (良好)"
        elif score >= 60:
            return "C (及格)"
        return "D (需努力)"

    def _generate_essay_feedback(self, scores: dict, criteria: dict,
                                  percentage: float) -> str:
        strengths = [k for k, v in scores.items() if v / criteria.get(k, 25) >= 0.8]
        weaknesses = [k for k, v in scores.items() if v / criteria.get(k, 25) < 0.5]

        feedback = f"\n📝 批改结果: {percentage}%\n"
        feedback += "━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        if strengths:
            feedback += "✅ 优点: " + ", ".join(strengths) + "\n"
        if weaknesses:
            feedback += "⚠️  需改进: " + ", ".join(weaknesses) + "\n"

        if percentage >= 90:
            feedback += "🌟 非常出色的作品！"
        elif percentage >= 70:
            feedback += "👍 写得不错，继续保持！"
        else:
            feedback += "💪 还需要多练习，加油！"

        feedback += "\n━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        return feedback
