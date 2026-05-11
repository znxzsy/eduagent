"""课程配置 - 各阶段学科设置、教学话术模板"""

from .models import LifeStage, Subject


# 各阶段核心学科
STAGE_CURRICULUM = {
    LifeStage.KINDERGARTEN: [Subject.MATH],
    LifeStage.PRIMARY: [Subject.MATH, Subject.CHINESE, Subject.ENGLISH],
    LifeStage.MIDDLE: [Subject.MATH, Subject.CHINESE, Subject.ENGLISH,
                       Subject.PHYSICS, Subject.HISTORY, Subject.GEOGRAPHY],
    LifeStage.HIGH: [Subject.MATH, Subject.CHINESE, Subject.ENGLISH,
                     Subject.PHYSICS, Subject.CHEMISTRY, Subject.BIOLOGY,
                     Subject.HISTORY, Subject.POLITICS],
    LifeStage.UNIVERSITY: [Subject.CS, Subject.MATH, Subject.PHYSICS],
    LifeStage.CAREER: [Subject.CS],
}

# 教学话术模板
EXPLANATIONS = {
    Subject.MATH: [
        "让我们用数学的方式来思考这个问题。首先，我们需要理解已知条件和目标。",
        "数学的核心是逻辑推理。我们一步步来，先把问题分解成小部分。",
        "这个概念可以用公式来表达。记住，数学语言是最精确的语言。",
    ],
    Subject.CHINESE: [
        "语文学习重在积累和理解。我们先来分析这篇文章的结构和主旨。",
        "中文的美感在于表达的层次。我们可以从修辞和意境两个角度来欣赏。",
        "写作时，要注意逻辑清晰、用词准确、情感真挚。",
    ],
    Subject.ENGLISH: [
        "英语学习需要多听多说多读多写。我们先从语法结构入手。",
        "英语的时态系统是其核心。让我们通过例句来理解。",
        "词汇量是基础，但在语境中记忆效果更好。",
    ],
    Subject.PHYSICS: [
        "物理是研究自然规律的科学。我们需要从实验现象出发，找到背后的原理。",
        "分析物理问题的第一步是受力分析。画受力图能帮我们理清思路。",
        "能量守恒是物理学最优美的原理之一。让我们用它来解决这个问题。",
    ],
    Subject.CS: [
        "计算机科学的核心是算法和数据结构。让我们先分析问题需要什么数据结构。",
        "编程不仅是写代码，更重要的是设计思维。先画流程图，再写代码。",
        "抽象是计算机科学最重要的能力。我们需要把复杂问题简化为可计算的模型。",
    ],
}

# 各阶段对应年龄
STAGE_AGES = {
    LifeStage.KINDERGARTEN: 6,
    LifeStage.PRIMARY: 12,
    LifeStage.MIDDLE: 15,
    LifeStage.HIGH: 18,
    LifeStage.UNIVERSITY: 22,
    LifeStage.CAREER: 26,
    LifeStage.RETIREMENT: 60,
}
