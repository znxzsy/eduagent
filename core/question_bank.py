"""题库管理 - 题目存储、按学科/难度查询、随机出题"""

import random
from typing import Optional

from .models import Difficulty, Subject


# 题库数据: {Subject: {Difficulty: [questions]}}
_QUESTION_BANK = {
    Subject.MATH: {
        Difficulty.EASY: [
            {"question": "1 + 1 = ?", "options": ["1", "2", "3", "4"], "answer": "2"},
            {"question": "3 × 4 = ?", "options": ["7", "12", "10", "14"], "answer": "12"},
            {"question": "10 - 7 = ?", "options": ["2", "3", "4", "5"], "answer": "3"},
            {"question": "8 / 2 = ?", "options": ["2", "3", "4", "6"], "answer": "4"},
            {"question": "5 + 6 = ?", "options": ["10", "11", "12", "9"], "answer": "11"},
            {"question": "9 × 3 = ?", "options": ["21", "27", "24", "30"], "answer": "27"},
        ],
        Difficulty.MEDIUM: [
            {"question": "x² - 4 = 0, x = ?", "options": ["±2", "±4", "2", "4"], "answer": "±2"},
            {"question": "sin(90°) = ?", "options": ["0", "1", "-1", "0.5"], "answer": "1"},
            {"question": "log₂(8) = ?", "options": ["2", "3", "4", "6"], "answer": "3"},
            {"question": "C(5,2) = ?", "options": ["10", "20", "5", "15"], "answer": "10"},
            {"question": "π ≈ ? (保留一位小数)", "options": ["3.1", "3.14", "3.2", "3.0"], "answer": "3.1"},
        ],
        Difficulty.HARD: [
            {"question": "∫2x dx = ?", "options": ["x²+C", "2x²+C", "x+C", "2+C"], "answer": "x²+C"},
            {"question": "lim(x→0) sin(x)/x = ?", "options": ["0", "1", "∞", "-1"], "answer": "1"},
            {"question": "det[[1,2],[3,4]] = ?", "options": ["-2", "2", "-1", "1"], "answer": "-2"},
            {"question": "e^(iπ) + 1 = ?", "options": ["0", "2", "1", "e"], "answer": "0"},
        ],
    },
    Subject.PHYSICS: {
        Difficulty.EASY: [
            {"question": "光速约为?", "options": ["3×10⁸ m/s", "3×10⁶ m/s", "340 m/s", "3×10¹⁰ m/s"], "answer": "3×10⁸ m/s"},
            {"question": "1个标准大气压约为?", "options": ["101325 Pa", "1000 Pa", "1 Pa", "10 Pa"], "answer": "101325 Pa"},
            {"question": "水的沸点是?", "options": ["100°C", "90°C", "110°C", "80°C"], "answer": "100°C"},
        ],
        Difficulty.MEDIUM: [
            {"question": "F=ma 中, m=2kg, a=3m/s², F=?", "options": ["6N", "5N", "8N", "1.5N"], "answer": "6N"},
            {"question": "动能公式是?", "options": ["½mv²", "mv", "mgh", "ma"], "answer": "½mv²"},
            {"question": "波长λ, 频率f, 波速v的关系?", "options": ["v=λf", "v=λ/f", "v=f/λ", "v=λ+f"], "answer": "v=λf"},
        ],
        Difficulty.HARD: [
            {"question": "E=mc² 中 c 的值?", "options": ["3×10⁸ m/s", "3×10⁶ m/s", "9.8 m/s²", "6.67×10⁻¹¹"], "answer": "3×10⁸ m/s"},
            {"question": "普朗克常量约为?", "options": ["6.63×10⁻³⁴ J·s", "6.63×10³⁴", "9.1×10⁻³¹", "1.6×10⁻¹⁹"], "answer": "6.63×10⁻³⁴ J·s"},
        ],
    },
    Subject.CS: {
        Difficulty.MEDIUM: [
            {"question": "二分查找的时间复杂度?", "options": ["O(log n)", "O(n)", "O(n²)", "O(1)"], "answer": "O(log n)"},
            {"question": "下列哪个不是排序算法?", "options": ["Dijkstra", "快速排序", "归并排序", "冒泡排序"], "answer": "Dijkstra"},
            {"question": "栈的特点是?", "options": ["先进后出", "先进先出", "随机访问", "无序"], "answer": "先进后出"},
            {"question": "HTTP状态码200表示?", "options": ["成功", "重定向", "客户端错误", "服务器错误"], "answer": "成功"},
        ],
        Difficulty.HARD: [
            {"question": "P vs NP 问题属于哪个领域?", "options": ["计算复杂性理论", "数值分析", "图论", "密码学"], "answer": "计算复杂性理论"},
            {"question": "红黑树的最坏查找复杂度?", "options": ["O(log n)", "O(n)", "O(√n)", "O(n log n)"], "answer": "O(log n)"},
        ],
    },
}


class QuestionBank:
    """题库管理"""

    def __init__(self, bank: dict = None):
        self._bank = bank or _QUESTION_BANK

    def get_questions(self, subject: Subject, difficulty: Difficulty) -> list:
        """获取指定学科和难度的题目"""
        return self._bank.get(subject, {}).get(difficulty, [])

    def generate_quiz(self, subject: Subject, count: int = 5,
                      difficulty: Difficulty = Difficulty.MEDIUM) -> list:
        """随机生成测验题"""
        questions = self.get_questions(subject, difficulty)
        if not questions:
            return []
        selected = random.sample(questions, min(count, len(questions)))
        return [
            {"index": i + 1, "question": q["question"],
             "options": q["options"], "answer": q["answer"]}
            for i, q in enumerate(selected, 1)
        ]

    def get_all_subjects(self) -> list:
        """获取所有有题的学科"""
        return list(self._bank.keys())

    def get_available_difficulties(self, subject: Subject) -> list:
        """获取某学科可用的难度等级"""
        if subject not in self._bank:
            return []
        return list(self._bank[subject].keys())

    def question_count(self, subject: Optional[Subject] = None,
                       difficulty: Optional[Difficulty] = None) -> int:
        """统计题目数量"""
        if subject:
            d = self._bank.get(subject, {})
            if difficulty:
                return len(d.get(difficulty, []))
            return sum(len(qs) for qs in d.values())
        return sum(
            len(qs)
            for subject_dict in self._bank.values()
            for qs in subject_dict.values()
        )
