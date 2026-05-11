"""生成项目架构图 - 使用 Graphviz"""
import os
from graphviz import Digraph

def generate_architecture():
    """绘制系统架构图"""
    os.makedirs('docs', exist_ok=True)

    dot = Digraph(
        'EduAgent Architecture',
        comment='EduAgent System Architecture',
        format='png',
        engine='dot',
    )

    # 全局设置
    dot.attr(
        rankdir='TB',
        size='12,8',
        dpi='200',
        bgcolor='transparent',
        fontname='Arial',
        fontsize='16',
        label='''EduAgent 教育系统架构
教育Agent + 智能批改 + 人生学习沙盒''',
        labelloc='t',
    )

    # 颜色方案
    colors = {
        'main': '#FF6B6B',
        'core': '#4ECDC4',
        'storage': '#FFE66D',
        'utils': '#95E1D3',
        'data': '#F38181',
        'border': '#2D3436',
    }

    # === Main 层 ===
    with dot.subgraph(name='cluster_main') as s:
        s.attr(
            label='系统入口层',
            style='filled',
            color='#E8E8E8',
            fillcolor='#F8F9FA',
            fontsize='14',
            fontcolor='#333333',
        )
        s.node(
            'main',
            'main.py\n系统入口 / CLI交互',
            shape='box',
            style='filled,rounded',
            fillcolor=colors['main'],
            fontcolor='white',
            fontsize='14',
            fontname='Arial',
            width='2',
            height='0.8',
        )

    # === Core 层 ===
    with dot.subgraph(name='cluster_core') as s:
        s.attr(
            label='核心业务层',
            style='filled',
            color='#E8E8E8',
            fillcolor='#F0FFF4',
            fontsize='14',
            fontcolor='#333333',
        )
        # 数据模型
        s.node(
            'models',
            'models.py\n数据模型',
            shape='box',
            style='filled,rounded',
            fillcolor=colors['core'],
            fontcolor='white',
            fontsize='12',
            fontname='Arial',
        )
        # 教育Agent
        s.node(
            'agent',
            'agent.py\n教育Agent',
            shape='box',
            style='filled,rounded',
            fillcolor=colors['core'],
            fontcolor='white',
            fontsize='12',
            fontname='Arial',
        )
        # 智能批改
        s.node(
            'grader',
            'grader.py\n智能批改',
            shape='box',
            style='filled,rounded',
            fillcolor=colors['core'],
            fontcolor='white',
            fontsize='12',
            fontname='Arial',
        )
        # 人生沙盒
        s.node(
            'sandbox',
            'sandbox.py\n人生沙盒',
            shape='box',
            style='filled,rounded',
            fillcolor=colors['core'],
            fontcolor='white',
            fontsize='12',
            fontname='Arial',
        )
        # 题库管理
        s.node(
            'question_bank',
            'question_bank.py\n题库管理',
            shape='box',
            style='filled,rounded',
            fillcolor=colors['core'],
            fontcolor='white',
            fontsize='12',
            fontname='Arial',
        )
        # 课程配置
        s.node(
            'curriculum',
            'curriculum.py\n课程配置',
            shape='box',
            style='filled,rounded',
            fillcolor=colors['core'],
            fontcolor='white',
            fontsize='12',
            fontname='Arial',
        )

    # === Storage 层 ===
    with dot.subgraph(name='cluster_storage') as s:
        s.attr(
            label='数据存储层',
            style='filled',
            color='#E8E8E8',
            fillcolor='#FFF8E7',
            fontsize='14',
            fontcolor='#333333',
        )
        s.node(
            'store',
            'student_store.py\n数据持久化 / JSON存储',
            shape='box',
            style='filled,rounded',
            fillcolor=colors['storage'],
            fontcolor='black',
            fontsize='12',
            fontname='Arial',
        )

    # === Utils 层 ===
    with dot.subgraph(name='cluster_utils') as s:
        s.attr(
            label='工具辅助层',
            style='filled',
            color='#E8E8E8',
            fillcolor='#E8F8F5',
            fontsize='14',
            fontcolor='#333333',
        )
        s.node(
            'utils',
            'formatting.py\n格式化输出',
            shape='box',
            style='filled,rounded',
            fillcolor=colors['utils'],
            fontcolor='black',
            fontsize='12',
            fontname='Arial',
        )

    # === Data 层 ===
    with dot.subgraph(name='cluster_data') as s:
        s.attr(
            label='数据文件层',
            style='filled',
            color='#E8E8E8',
            fillcolor='#FFE8E8',
            fontsize='14',
            fontcolor='#333333',
        )
        s.node(
            'data',
            'data/*.json\n学生数据持久化',
            shape='folder',
            style='filled,rounded',
            fillcolor=colors['data'],
            fontcolor='white',
            fontsize='12',
            fontname='Arial',
        )

    # === 箭头连接 ===
    # Main -> Core
    dot.edge('main', 'models', color='#FF6B6B80', penwidth='2')
    dot.edge('main', 'agent', color='#FF6B6B80', penwidth='2')
    dot.edge('main', 'grader', color='#FF6B6B80', penwidth='2')
    dot.edge('main', 'sandbox', color='#FF6B6B80', penwidth='2')

    # Core 内部连接
    dot.edge('models', 'agent', color='#4ECDC480', style='dashed')
    dot.edge('agent', 'grader', color='#4ECDC480', style='dashed')
    dot.edge('agent', 'question_bank', color='#4ECDC480', style='dashed')
    dot.edge('curriculum', 'agent', color='#4ECDC480', style='dashed')
    dot.edge('grader', 'sandbox', color='#4ECDC480', style='dashed')

    # Storage -> Data
    dot.edge('store', 'data', color='#FFE66D80', penwidth='2')

    # Core -> Storage
    dot.edge('models', 'store', color='#FFE66D80', style='dashed')
    dot.edge('sandbox', 'store', color='#FFE66D80', style='dashed')

    # Core -> Utils
    dot.edge('agent', 'utils', color='#95E1D380', style='dotted')
    dot.edge('grader', 'utils', color='#95E1D380', style='dotted')

    # 保存
    filepath = dot.render('docs/architecture', cleanup=True)
    print(f"✅ 架构图已生成: {filepath}")
    return filepath


def generate_data_flow():
    """绘制数据流图"""
    dot = Digraph(
        'Data Flow',
        comment='EduAgent Data Flow',
        format='png',
        engine='dot',
    )

    dot.attr(
        rankdir='LR',
        size='14,6',
        dpi='200',
        bgcolor='transparent',
        fontname='Arial',
        fontsize='14',
        label='EduAgent 数据流程图',
        labelloc='t',
    )

    colors = {
        'student': '#FF6B6B',
        'agent': '#4ECDC4',
        'bank': '#FFE66D',
        'grader': '#95E1D3',
        'sandbox': '#F38181',
        'store': '#AA96DA',
    }

    # 节点
    nodes = [
        ('student', '学生模型\nStudent', colors['student']),
        ('agent', '教育Agent\nEduAgent', colors['agent']),
        ('bank', '题库\nQuestionBank', colors['bank']),
        ('grader', '批改器\nGrader', colors['grader']),
        ('sandbox', '人生沙盒\nSandbox', colors['sandbox']),
        ('store', '存储层\nStore', colors['store']),
    ]

    for node_id, label, color in nodes:
        dot.node(
            node_id, label,
            shape='box',
            style='filled,rounded',
            fillcolor=color,
            fontcolor='white',
            fontsize='12',
            fontname='Arial',
        )

    # 数据流
    flows = [
        ('student', 'agent', '学习/练习'),
        ('agent', 'bank', '出题'),
        ('bank', 'grader', '测验'),
        ('grader', 'student', '批改反馈'),
        ('agent', 'sandbox', '状态更新'),
        ('student', 'store', '保存/加载'),
    ]

    for src, dst, label in flows:
        dot.edge(
            src, dst, label=label,
            color='#666666',
            fontcolor='#666666',
            fontsize='10',
            fontname='Arial',
            arrowsize='0.8',
        )

    filepath = dot.render('docs/data_flow', cleanup=True)
    print(f"✅ 数据流图已生成: {filepath}")
    return filepath


def generate_sandbox_flow():
    """绘制人生沙盒流程图"""
    dot = Digraph(
        'Sandbox Flow',
        comment='EduAgent Life Sandbox',
        format='png',
        engine='dot',
    )

    dot.attr(
        rankdir='TB',
        size='12,10',
        dpi='200',
        bgcolor='transparent',
        fontname='Arial',
        fontsize='14',
        label='人生沙盒 - 阶段演进与事件系统',
        labelloc='t',
    )

    # 颜色
    stage_colors = {
        '幼儿园': '#FF6B6B',
        '小学': '#4ECDC4',
        '初中': '#FFE66D',
        '高中': '#95E1D3',
        '大学': '#F38181',
        '职业': '#AA96DA',
        '退休': '#FCBAD3',
    }

    # 阶段节点
    for stage, color in stage_colors.items():
        dot.node(
            stage, stage,
            shape='box',
            style='filled,rounded',
            fillcolor=color,
            fontcolor='white' if color != '#FFE66D' else 'black',
            fontsize='14',
            fontname='Arial',
            width='2',
            height='0.8',
        )

    # 阶段推进
    stages = ['幼儿园', '小学', '初中', '高中', '大学', '职业', '退休']
    for i in range(len(stages) - 1):
        dot.edge(
            stages[i], stages[i+1],
            color='#FFD700',
            arrowsize='1.0',
            penwidth='2',
        )

    # 事件选择流程
    event_label = '触发事件 → 选择分支 → 获得经验'
    dot.node(
        'event_flow',
        event_label,
        shape='note',
        style='filled',
        fillcolor='#E8E8E8',
        fontcolor='#333333',
        fontsize='12',
        fontname='Arial',
    )

    # 事件影响各阶段
    for stage in stages[:6]:
        dot.edge(
            'event_flow', stage,
            color='#AAAAAA',
            style='dashed',
            arrowsize='0.5',
        )

    filepath = dot.render('docs/sandbox_flow', cleanup=True)
    print(f"✅ 沙盒流程图已生成: {filepath}")
    return filepath


if __name__ == '__main__':
    generate_architecture()
    generate_data_flow()
    generate_sandbox_flow()
    print("\n✅ 所有架构图已生成到 docs/ 目录")
