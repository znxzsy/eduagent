"""EduAgent 系统入口 - 交互式 CLI"""

import random
import sys
import os

# 支持直接运行
_edu = os.path.dirname(os.path.abspath(__file__))
if _edu not in sys.path:
    sys.path.insert(0, _edu)

from core.models import Student, LifeStage, Subject, Difficulty, Skill
from core.agent import EduAgent
from core.grader import Grader
from core.sandbox import LifeSandbox
from core.question_bank import QuestionBank
from storage.student_store import StudentStore
from utils.formatting import separator, progress_bar
from core.multimodal import MMGrader, ImageInput


def banner():
    print("""
╔════════════════════════════════════════════╗
║  🎓  EduAgent 教育系统 v2.0 (MM)          ║
║   教育 Agent + 智能批改 + 人生学习沙盒      ║
║      + 多模态手写识别/视觉推理              ║
╚════════════════════════════════════════════╝
""")


def demo_mode():
    """演示模式 - 自动运行所有功能"""
    student = Student(name="小明", age=10, stage=LifeStage.PRIMARY)
    agent = EduAgent(student)
    grader = Grader()
    sandbox = LifeSandbox(student)

    print(agent.introduce())

    # === 1. 知识点讲解 ===
    print(separator("【演示 1】教育 Agent - 知识点讲解"))
    print(agent.teach(Subject.MATH, "一元二次方程"))
    print(agent.teach(Subject.MATH, "勾股定理"))
    print(agent.teach(Subject.PHYSICS, "牛顿第二定律"))

    # === 2. 测验批改 ===
    print(separator("【演示 2】智能批改 - 测验"))
    quiz = agent.generate_quiz(Subject.MATH, count=5, difficulty=Difficulty.MEDIUM)
    if not quiz:
        print("  题库暂无题目")
        return
    print(f"\n📝 数学测验 (5 题):\n")
    for q in quiz:
        print(f"  {q['index']}. {q['question']}")
        print(f"     {q['options']}")

    answers = [q["answer"] if random.random() > 0.3 else random.choice(q["options"])
               for q in quiz]
    print(f"\n💬 学生答案：{answers}")

    result = grader.grade_quiz(student, quiz, answers)
    print(f"\n📊 批改结果：{result['score']}分 ({result['grade']}) | "
          f"正确：{result['correct']}/{result['total']}")
    for d in result['details']:
        status = "✅" if d['is_correct'] else "❌"
        print(f"  {status} 第{d['index']}题：{d['user_answer']} → {d['correct_answer']}")

    # === 3. 作文批改 ===
    print(separator("【演示 3】智能批改 - 作文"))
    essay = grader.grade_essay(student, "我的梦想",
        "每个人都有自己的梦想。我的梦想是成为一名科学家。\n"
        "科学家可以探索未知的世界，发现新的知识。\n"
        "为了成为科学家，我要好好学习，天天向上。\n"
        "我相信只要努力，梦想一定会实现。")
    print(essay["feedback"])
    for k, v in essay["scores"].items():
        print(f"  • {k}: {v}/25 {progress_bar(v, 25, 10)}")

    # === 4. 人生沙盒 ===
    print(separator("【演示 4】人生学习沙盒"))
    student.add_skill(Skill("逻辑思维", 1, 0))
    student.add_skill(Skill("阅读能力", 1, 0))
    student.add_skill(Skill("体能", 1, 0))

    print(sandbox.make_choice(0, 0))
    print(sandbox.make_choice(1, 0))
    print(sandbox.simulate_years(2))

    print(sandbox.advance_stage(LifeStage.MIDDLE))
    print(sandbox.make_choice(1, 0))
    print(sandbox.simulate_years(3))

    print(sandbox.advance_stage(LifeStage.HIGH))
    print(sandbox.simulate_years(3))

    # === 5. 多模态批改 ===
    print(separator("【演示 5】多模态批改（MM）"))
    mm_grader = MMGrader()

    print("""
🔧 多模态批改器已初始化
   支持功能:
   - 手写 OCR 识别
   - 视觉推理（Think-with-Image）
   - 对抗攻击检测
   - 图像批改

   注：当前为演示模式，需接入以下任一服务:
   - GPT-4o / GPT-4V
   - Gemini 2.5 Pro
   - Qwen-VL (阿里云)
   - PaddleOCR (本地 OCR)
""")

    print("📌 攻击检测演示:")
    print("   检测逻辑：模糊检测 → 噪声检测 → 对抗样本检测")
    print("   当前状态：⚪ 等待图像输入")

    # === 6. 数据持久化 ===
    print(separator("【演示 6】数据持久化"))
    store = StudentStore("edu_agent/data")
    path = store.save(student)
    print(f"✅ 学生数据已保存到：{path}")
    print(f"  动力：{progress_bar(student.motivation)}  "
          f"自信：{progress_bar(student.confidence)}  "
          f"掌握率：{progress_bar(student.get_mastery_rate())}")

    # === 7. 最终报告 ===
    print(separator("【最终报告】"))
    print(agent.study_plan())
    print(sandbox.get_life_report())

    stats = grader.batch_grade(grader.grading_records)
    print(f"📈 批改统计：{stats.get('count', 0)}次 | "
          f"均分：{stats.get('average', 0)} | "
          f"最高：{stats.get('highest', 0)} | "
          f"最低：{stats.get('lowest', 0)}")
    print("\n✨ EduAgent 教育系统 v2.0 (Multimodal) 演示完成！")


def interactive_mode():
    """交互模式 - CLI 用户输入指令"""
    print("=== 交互模式 (输入 help 查看指令) ===\n")
    student = Student(name="学生", age=10, stage=LifeStage.PRIMARY)
    agent = EduAgent(student)
    grader = Grader()
    mm_grader = MMGrader()
    sandbox = LifeSandbox(student)
    store = StudentStore("edu_agent/data")

    print(agent.introduce())

    while True:
        try:
            cmd = input("\n> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\n再见！")
            break

        if cmd == "help":
            print("""
可用指令:
  teach <学科> <知识点>    - 讲解知识点
  quiz <学科> <数量>        - 生成测验
  grade <答案 1,答案 2,...>   - 批改上次测验
  essay <标题>              - 批改作文
  plan                     - 查看学习计划
  event <序号> <选项序号>    - 沙盒事件选择
  stage <阶段名>            - 推进人生阶段
  simulate <年数>           - 模拟生活
  status                   - 查看学生状态
  save                     - 保存数据
  load <名字>              - 加载数据
  mm-ocr <图片路径>         - OCR 识别手写
  mm-grade <图片路径> <答案> - 图像批改
  mm-check <图片路径>       - 攻击检测
  quit                     - 退出
""")

        elif cmd == "quit":
            store.save(student)
            print("已保存，再见！")
            break

        elif cmd == "plan":
            print(agent.study_plan())

        elif cmd == "status":
            s = student.get_status()
            print(f"  姓名：{s['name']} | 年龄：{s['age']} | "
                  f"阶段：{s['stage']}")
            print(f"  知识点：{s['knowledge_count']} | 掌握率：{s['mastery_rate']}%")
            print(f"  动力：{s['motivation']} | 自信：{s['confidence']}")

        elif cmd.startswith("teach "):
            parts = cmd.split(" ", 2)
            if len(parts) < 3:
                print("用法：teach <学科> <知识点>")
                continue
            subject_map = {s.value: s for s in Subject}
            subject = subject_map.get(parts[1])
            if not subject:
                print(f"未知学科：{parts[1]}")
                continue
            print(agent.teach(subject, parts[2]))

        elif cmd.startswith("quiz "):
            parts = cmd.split()
            subject_map = {s.value: s for s in Subject}
            subject = subject_map.get(parts[1]) if len(parts) > 1 else Subject.MATH
            if not subject:
                print("未知学科")
                continue
            count = int(parts[2]) if len(parts) > 2 else 5
            quiz = agent.generate_quiz(subject, count)
            if not quiz:
                print("暂无题目")
                continue
            for q in quiz:
                print(f"  {q['index']}. {q['question']} {q['options']}")
            interactive_mode._current_quiz = quiz

        elif cmd.startswith("grade "):
            if not hasattr(interactive_mode, "_current_quiz"):
                print("请先用 quiz 命令生成测验")
                continue
            answers = [a.strip() for a in cmd[6:].split(",")]
            result = grader.grade_quiz(student, interactive_mode._current_quiz, answers)
            print(f"  得分：{result['score']}分 ({result['grade']}) | "
                  f"正确：{result['correct']}/{result['total']}")

        elif cmd.startswith("essay "):
            title = cmd[6:].strip() or "未命名"
            print("输入作文内容 (空行结束):")
            lines = []
            while True:
                try:
                    line = input()
                    if not line:
                        break
                    lines.append(line)
                except (EOFError, KeyboardInterrupt):
                    break
            essay = grader.grade_essay(student, title, "\n".join(lines))
            print(essay["feedback"])
            for k, v in essay["scores"].items():
                print(f"  • {k}: {v}/25")

        elif cmd.startswith("event "):
            parts = cmd.split()
            if len(parts) < 3:
                print("用法：event <事件序号> <选项序号>")
                continue
            print(sandbox.make_choice(int(parts[1]) - 1, int(parts[2]) - 1))

        elif cmd.startswith("stage "):
            stage_map = {s.value: s for s in LifeStage}
            stage = stage_map.get(cmd[6:].strip())
            if not stage:
                print("未知阶段")
                continue
            print(sandbox.advance_stage(stage))

        elif cmd.startswith("simulate "):
            years = int(cmd.split()[1]) if len(cmd.split()) > 1 else 1
            print(sandbox.simulate_years(years))

        elif cmd == "save":
            path = store.save(student)
            print(f"✅ 已保存：{path}")

        elif cmd.startswith("load "):
            name = cmd[5:].strip()
            try:
                if name in store.list_students():
                    student = store.load(name)
                    agent = EduAgent(student)
                    sandbox = LifeSandbox(student)
                    print(f"✅ 已加载：{name}")
                else:
                    print(f"未找到：{name}")
            except Exception as e:
                print(f"❌ 错误：{e}")

        # Multimodal commands
        elif cmd.startswith("mm-ocr "):
            img_path = cmd[7:].strip()
            if not img_path:
                print("Usage: mm-ocr <image_path>")
                continue
            try:
                img = ImageInput(path=img_path)
                result = mm_grader.ocr(img)
                print(f"OCR Result:\n{result.text}")
                print(f"   Confidence: {result.confidence:.1%}")
                print(f"   Handwritten: {'Yes' if result.is_handwritten else 'No'}")
                print(f"   Quality: {result.quality_score:.2f}")
            except Exception as e:
                print(f"Error: {e}")

        elif cmd.startswith("mm-grade "):
            parts = cmd[8:].split(None, 1)
            if len(parts) < 2:
                print("Usage: mm-grade <image_path> <answer>")
                continue
            img_path, answer = parts
            try:
                img = ImageInput(path=img_path)
                result = mm_grader.grade_image(img, answer)
                if result.get("status") == "blocked":
                    print(f"Blocked: {result['reason']}")
                else:
                    print(f"Grade Result:")
                    print(f"   Student: {result.get('student_answer')}")
                    print(f"   Reference: {answer}")
                    print(f"   Correct: {'Yes' if result.get('is_correct') else 'No'}")
                    print(f"   Confidence: {result.get('confidence', 0):.1%}")
            except Exception as e:
                print(f"Error: {e}")

        elif cmd.startswith("mm-check "):
            img_path = cmd[10:].strip()
            if not img_path:
                print("Usage: mm-check <image_path>")
                continue
            try:
                img = ImageInput(path=img_path)
                result = mm_grader.detect_attack(img)
                if result.is_attack:
                    print(f"Attack Detected: {result.attack_type}")
                    print(f"   Risk: {result.risk_level}")
                    print(f"   Confidence: {result.confidence:.1%}")
                else:
                    print("No attack detected")
                    print(f"   Confidence: {result.confidence:.1%}")
            except Exception as e:
                print(f"Error: {e}")

        elif cmd == "":
            pass
        else:
            print("未知指令，输入 help 查看可用指令")


def main():
    banner()
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        interactive_mode()
    else:
        demo_mode()


if __name__ == "__main__":
    main()
