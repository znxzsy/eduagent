"""人生学习沙盒 - 模拟人生不同阶段的学习与成长"""

import random

from .curriculum import STAGE_AGES
from .models import LifeStage, LifeEvent, Skill, Student


# 各阶段事件库
_STAGE_EVENTS = {
    LifeStage.PRIMARY: [
        LifeEvent("数学竞赛选拔", "学校要举办数学竞赛，你决定参加吗？",
                  ["参加", "不参加"], {"逻辑思维": 15, "数学能力": 10}),
        LifeEvent("加入阅读俱乐部", "班级有个阅读俱乐部在招人，要加入吗？",
                  ["加入", "不加入"], {"阅读能力": 15, "写作能力": 10}),
        LifeEvent("体育课选项目", "体育课可以自选一个项目学习，选什么？",
                  ["足球", "篮球", "游泳", "跑步"], {"体能": 10, "团队协作": 5}),
    ],
    LifeStage.MIDDLE: [
        LifeEvent("分科兴趣调查", "学校开始调查分科意向，你更倾向于？",
                  ["理科", "文科", "不确定"], {"学科方向": 0, "自我认知": 10}),
        LifeEvent("社团招新", "各种社团开始招新了，你感兴趣的是？",
                  ["科技社", "文学社", "体育社", "都不参加"], {"社交能力": 10, "兴趣技能": 15}),
        LifeEvent("期中考试", "即将到来的期中考试，你打算怎么准备？",
                  ["全力以赴", "正常复习", "随缘"], {"学习成绩": 20, "压力管理": 5}),
    ],
    LifeStage.HIGH: [
        LifeEvent("高考志愿方向", "需要考虑高考志愿了，你的目标是？",
                  ["理工科", "医学", "文科", "艺术"], {"专业方向": 0, "目标感": 15}),
        LifeEvent("自主招生机会", "有自主招生的机会，要试试吗？",
                  ["准备材料", "放弃"], {"综合素质": 15, "竞争力": 20}),
        LifeEvent("高三压力很大", "学习压力越来越大，你选择怎么应对？",
                  ["运动减压", "找人倾诉", "自己消化"], {"心理健康": 15, "抗压能力": 10}),
    ],
    LifeStage.UNIVERSITY: [
        LifeEvent("实习机会", "一家知名公司有实习机会，要申请吗？",
                  ["申请", "继续学习"], {"实践经验": 20, "职场技能": 15}),
        LifeEvent("科研项目", "教授邀请你参加科研项目，参加吗？",
                  ["参加", "不参加"], {"研究能力": 20, "学术素养": 15}),
        LifeEvent("创业想法", "你和同学有个创业想法，要试试吗？",
                  ["开始创业", "先完成学业"], {"创业能力": 25, "风险意识": 10}),
    ],
    LifeStage.CAREER: [
        LifeEvent("职业选择", "有两个工作机会，选哪个？",
                  ["高薪工作", "感兴趣的方向"], {"职业满意度": 15, "经济基础": 10}),
        LifeEvent("终身学习", "工作之余要持续学习吗？",
                  ["学习新技能", "休息"], {"专业技能": 20, "学习能力": 10}),
        LifeEvent("带新人", "有新人想拜你为师，要带吗？",
                  ["接受", "婉拒"], {"领导力": 15, "教学能力": 10}),
    ],
}


class LifeSandbox:
    """人生学习沙盒"""

    def __init__(self, student: Student):
        self.student = student
        self.history: list = []
        self.current_age = student.age

    def advance_stage(self, new_stage: LifeStage) -> str:
        """推进人生阶段"""
        old_stage = self.student.stage
        self.student.stage = new_stage
        self.current_age = STAGE_AGES.get(new_stage, self.current_age)
        self.student.age = self.current_age

        result = f"""
╔══════════════════════════════════════╗
║   🎉 人生阶段推进！                    ║
║   {old_stage.value} → {new_stage.value}                        ║
║   年龄: {self.current_age}岁                              ║
╚══════════════════════════════════════╝
"""
        events = _STAGE_EVENTS.get(new_stage, [])
        if events:
            result += f"\n📢 触发了 {len(events)} 个事件，请选择：\n"
            for i, event in enumerate(events, 1):
                result += (f"  {i}. {event.title}: {event.description}\n"
                           f"     选项: {' / '.join(event.choices)}\n")

        self.history.append({"action": "stage_advance", "from": old_stage.value,
                             "to": new_stage.value, "age": self.current_age})
        return result

    def make_choice(self, event_index: int, choice_index: int) -> str:
        """做出选择"""
        events = _STAGE_EVENTS.get(self.student.stage, [])
        if event_index >= len(events):
            return "❌ 无效的事件索引。"

        event = events[event_index]
        if choice_index >= len(event.choices):
            return "❌ 无效的选择。"

        choice = event.choices[choice_index]
        result = f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━
🎮 事件: {event.title}
📖 {event.description}
✅ 你的选择: {choice}
"""
        if choice != event.choices[-1]:
            for skill_name, exp in event.effects.items():
                existing = next((s for s in self.student.skills if s.name == skill_name), None)
                if existing:
                    existing.add_exp(exp)
                elif exp > 0:
                    new_skill = Skill(name=skill_name)
                    new_skill.add_exp(exp)
                    self.student.add_skill(new_skill)
            self.student.motivation = min(100, self.student.motivation + 5)
            result += f"\n✨ 获得经验值: {event.effects}\n"
        else:
            self.student.motivation = max(0, self.student.motivation - 3)
            result += "\n😐 你选择了不行动，失去了一次成长机会。\n"

        result += "━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        self.history.append({"action": "choice", "event": event.title,
                             "choice": choice, "age": self.current_age})
        return result

    def simulate_years(self, years: int = 1) -> str:
        """模拟指定年数的生活"""
        result = f"\n⏳ 模拟了 {years} 年的生活...\n"
        self.current_age += years
        self.student.age = self.current_age
        self.student.total_study_hours += years * 200

        events = _STAGE_EVENTS.get(self.student.stage, [])
        if events and random.random() > 0.5:
            event = random.choice(events)
            choice_idx = random.randint(0, len(event.choices) - 1)
            choice = event.choices[choice_idx]
            result += f"📌 发生了事件: {event.title} → {choice}\n"
            if choice != event.choices[-1]:
                for skill_name, exp in event.effects.items():
                    existing = next((s for s in self.student.skills if s.name == skill_name), None)
                    if existing:
                        existing.add_exp(exp)

        for kp in self.student.knowledge_points:
            if not kp.mastered and kp.practice_count > 2:
                if random.random() > 0.6:
                    kp.mastered = True
                    result += f"✨ 自然掌握: [{kp.subject.value}] {kp.name}\n"

        self.history.append({"action": "simulate", "years": years, "age": self.current_age})
        return result

    def get_life_report(self) -> str:
        """获取人生报告"""
        skills_summary = "\n".join(
            f"  • {s.name}: Lv.{s.level} (EXP: {s.experience})"
            for s in self.student.skills
        ) or "  (暂无技能)"

        report = f"""
╔════════════════════════════════════════╗
║        📜 人生学习沙盒报告                ║
╠════════════════════════════════════════╣
║  姓名: {self.student.name:<20}  ║
║  年龄: {self.current_age}岁                                ║
║  阶段: {self.student.stage.value:<16}  ║
║  学习时长: {self.student.total_study_hours:.1f}小时                     ║
║  知识点: {len(self.student.knowledge_points)}个                          ║
║  掌握率: {self.student.get_mastery_rate():.1f}%                          ║
╠════════════════════════════════════════╣
║  技能树:                                  ║
{chr(10).join(f'║    {s:<32}  ║' for s in skills_summary.split(chr(10)))}
╠════════════════════════════════════════╣
║  决策历史: {len(self.history)}次                        ║
╚════════════════════════════════════════╝
"""
        return report
