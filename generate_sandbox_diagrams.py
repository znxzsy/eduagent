"""人生沙盒架构图生成器 - 专业版"""
import os
from graphviz import Digraph

os.makedirs('docs', exist_ok=True)

# ============================================================
# 图 1: 人生沙盒完整架构图
# ============================================================
def generate_sandbox_architecture():
    dot = Digraph('Sandbox Architecture', format='png', engine='dot')
    dot.attr(
        rankdir='TB',
        size='24,18',
        dpi='300',
        bgcolor='transparent',
        fontname='Arial',
        label='''🎯 人生学习沙盒 v2.0 - 完整架构
从第一性原理出发：运气因子 (~10%) + 知识点匹配 + 防背题机制''',
        labelloc='t',
        fontsize='18',
        fontcolor='#2C3E50',
    )

    # 现代莫兰迪色系
    colors = {
        'input': '#F5E6E8',      # 输入层 - 淡粉
        'env': '#E8F4F8',        # 仿真 - 淡蓝
        'attack': '#FCE8E6',     # 攻击 - 淡红
        'defense': '#E6E8F4',    # 防御 - 淡紫
        'trajectory': '#F8F0E6', # 轨迹 - 淡橙
        'eval': '#F0E8F4',       # 评估 - 淡紫
        'data': '#FFF4E6',       # 数据 - 淡黄
    }

    # 节点通用样式
    node_attrs = {
        'style': 'filled,rounded',
        'penwidth': '1.5',
        'fontname': 'Arial',
    }

    # === 第 1 层：用户输入 ===
    with dot.subgraph(name='cluster_input') as s:
        s.attr(label='👤 用户输入层', style='filled,rounded', fillcolor=colors['input'],
               fontsize='13', penwidth='2', color='#E0B0B8')
        s.node('user_profile', '用户画像\n(年龄/阶段/偏好)', shape='box',
               style='filled,rounded', fillcolor='#FFB6C1', penwidth='1.5')
        s.node('skill_config', '技能配置\n(初始技能树)', shape='box',
               style='filled,rounded', fillcolor='#FFB6C1', penwidth='1.5')
        s.node('env_config', '环境配置\n(难度/随机种子)', shape='box',
               style='filled,rounded', fillcolor='#FFB6C1', penwidth='1.5')

    # === 第 2 层：仿真环境 ===
    with dot.subgraph(name='cluster_simulation') as s:
        s.attr(label='🌍 仿真环境层', style='filled,rounded', fillcolor=colors['env'],
               fontsize='13', penwidth='2', color='#7EC8E3')
        s.node('stage_engine', '阶段引擎\n(7 人生阶段)', shape='box',
               style='filled,rounded', fillcolor='#4ECDC4', penwidth='1.5')
        s.node('event_generator', '事件生成器\n(随机/脚本)', shape='box',
               style='filled,rounded', fillcolor='#4ECDC4', penwidth='1.5')
        s.node('choice_system', '选择系统\n(分支决策)', shape='box',
               style='filled,rounded', fillcolor='#4ECDC4', penwidth='1.5')
        s.node('skill_tracker', '技能追踪器\n(EXP/Level)', shape='box',
               style='filled,rounded', fillcolor='#4ECDC4', penwidth='1.5')

    # === 第 3 层：攻击模块 ===
    with dot.subgraph(name='cluster_attack') as s:
        s.attr(label='🔴 攻击模块 (Adversarial)', style='filled,rounded', fillcolor=colors['attack'],
               fontsize='13', penwidth='2', color='#E88080')
        s.node('attack_gen', '攻击生成器', shape='box',
               style='filled,rounded', fillcolor='#FF6B6B', fontcolor='white', penwidth='1.5')
        s.node('noise_inject', '噪声注入\n(模糊/涂抹/遮挡)', shape='box',
               style='filled,rounded', fillcolor='#FF6B6B', fontcolor='white', penwidth='1.5')
        s.node('adv_perturb', '对抗扰动\n(FGSM/PGD)', shape='box',
               style='filled,rounded', fillcolor='#FF6B6B', fontcolor='white', penwidth='1.5')
        s.node('logic_attack', '逻辑攻击\n(矛盾/陷阱)', shape='box', style='filled,rounded', fillcolor='#FF6B6B', fontcolor='white')

    # === 第 4 层：防御模块 ===
    with dot.subgraph(name='cluster_defense') as s:
        s.attr(label='防御模块 (Robustness)', style='filled', fillcolor=colors['defense'], fontsize='14')

        s.node('defense_detect', '攻击检测\n(异常识别)', shape='box', style='filled,rounded', fillcolor='#4169E1', fontcolor='white')
        s.node('defense_filter', '输入过滤\n(去噪/修复)', shape='box', style='filled,rounded', fillcolor='#4169E1', fontcolor='white')
        s.node('defense_verify', '一致性验证\n(多模型交叉)', shape='box', style='filled,rounded', fillcolor='#4169E1', fontcolor='white')
        s.node('defense_fallback', '降级策略\n(规则回退)', shape='box', style='filled,rounded', fillcolor='#4169E1', fontcolor='white')

    # === 第 5 层：轨迹生成 ===
    with dot.subgraph(name='cluster_trajectory') as s:
        s.attr(label='轨迹生成层', style='filled', fillcolor=colors['trajectory'], fontsize='14')

        s.node('traj_collector', '轨迹收集器', shape='box', style='filled,rounded', fillcolor='#FFA500')
        s.node('traj_encoder', '轨迹编码器\n(State-Action-Reward)', shape='box', style='filled,rounded', fillcolor='#FFA500')
        s.node('traj_storage', '轨迹存储\n(JSON/Parquet)', shape='cylinder', style='filled', fillcolor='#FFA500')
        s.node('traj_augment', '轨迹增强\n(采样/插值)', shape='box', style='filled,rounded', fillcolor='#FFA500')

    # === 第 6 层：评估优化 ===
    with dot.subgraph(name='cluster_eval') as s:
        s.attr(label='评估优化层', style='filled', fillcolor=colors['eval'], fontsize='14')

        s.node('eval_luck', '🎲 运气因子\n(~10% 概率)', shape='box', style='filled,rounded', fillcolor='#FFB6C1', fontsize='11')
        s.node('eval_knowledge', '知识点匹配评估\n(掌握度 vs 题目)', shape='box', style='filled,rounded', fillcolor='#9370DB', fontsize='11')
        s.node('eval_variant', '变形式验证\n(防背题检测)', shape='box', style='filled,rounded', fillcolor='#9370DB', fontsize='11')
        s.node('eval_consistency', '一致性评估\n(自洽性检查)', shape='box', style='filled,rounded', fillcolor='#9370DB')
        s.node('eval_robustness', '鲁棒性评估\n(攻击成功率)', shape='box', style='filled,rounded', fillcolor='#9370DB')
        s.node('knowledge_trace', '📊 知识追踪\n(IRT/BKT 模型)', shape='hexagon', style='filled', fillcolor='#BA68C8', fontsize='11')
        s.node('optimizer', '优化器\n(RL/梯度更新)', shape='box', style='filled,rounded', fillcolor='#9370DB')

    # === 第 7 层：数据输出 ===
    with dot.subgraph(name='cluster_output') as s:
        s.attr(label='数据输出层', style='filled', fillcolor=colors['data'], fontsize='14')

        s.node('dataset', '轨迹数据集\n(labeled_trajectories)', shape='cylinder', style='filled', fillcolor='#FFD700')
        s.node('metrics', '评估指标\n(Acc/Robust/F1)', shape='box', style='filled,rounded', fillcolor='#FFD700')
        s.node('report', '分析报告\n(可视化/统计)', shape='note', style='filled', fillcolor='#FFD700')

    # 连接关系
    # 输入 → 仿真
    dot.edge('user_profile', 'stage_engine')
    dot.edge('skill_config', 'skill_tracker')
    dot.edge('env_config', 'event_generator')

    # 仿真内部
    dot.edge('stage_engine', 'event_generator', style='dashed')
    dot.edge('event_generator', 'choice_system', style='dashed')
    dot.edge('choice_system', 'skill_tracker', style='dashed')

    # 仿真 → 攻击
    dot.edge('choice_system', 'attack_gen', color='#FF6B6B80')

    # 攻击内部
    dot.edge('attack_gen', 'noise_inject', style='dashed', color='#FF6B6B80')
    dot.edge('attack_gen', 'adv_perturb', style='dashed', color='#FF6B6B80')
    dot.edge('attack_gen', 'logic_attack', style='dashed', color='#FF6B6B80')

    # 攻击 → 防御
    dot.edge('noise_inject', 'defense_detect', color='#4169E180')
    dot.edge('adv_perturb', 'defense_detect', color='#4169E180')
    dot.edge('logic_attack', 'defense_verify', color='#4169E180')

    # 防御内部
    dot.edge('defense_detect', 'defense_filter', style='dashed', color='#4169E180')
    dot.edge('defense_filter', 'defense_fallback', style='dashed', color='#4169E180')

    # 防御 → 轨迹
    dot.edge('defense_filter', 'traj_collector', color='#FFA50080')
    dot.edge('skill_tracker', 'traj_collector', color='#FFA50080')

    # 轨迹内部
    dot.edge('traj_collector', 'traj_encoder', style='dashed', color='#FFA50080')
    dot.edge('traj_encoder', 'traj_storage', style='dashed', color='#FFA50080')
    dot.edge('traj_storage', 'traj_augment', style='dashed', color='#FFA50080')

    # 轨迹 → 评估
    dot.edge('traj_storage', 'eval_knowledge', color='#9370DB80')
    dot.edge('traj_storage', 'eval_variant', color='#9370DB80')
    dot.edge('traj_storage', 'eval_consistency', color='#9370DB80')
    dot.edge('traj_storage', 'eval_robustness', color='#9370DB80')

    # 运气因子影响评估
    dot.edge('eval_luck', 'eval_knowledge', style='dotted', color='#FFB6C180', label='10% 概率')

    # 评估内部
    dot.edge('eval_knowledge', 'knowledge_trace', style='dashed', color='#9370DB80')
    dot.edge('eval_variant', 'knowledge_trace', style='dashed', color='#9370DB80')
    dot.edge('knowledge_trace', 'optimizer', style='dashed', color='#BA68C880')
    dot.edge('eval_consistency', 'optimizer', style='dashed', color='#9370DB80')
    dot.edge('eval_robustness', 'optimizer', style='dashed', color='#9370DB80')

    # 评估 → 输出
    dot.edge('knowledge_trace', 'dataset', color='#FFD70080')
    dot.edge('eval_robustness', 'metrics', color='#FFD70080')
    dot.edge('optimizer', 'report', color='#FFD70080')

    # 反馈循环
    dot.edge('optimizer', 'defense_filter', constraint='false', style='dotted', color='#9370DB80')
    dot.edge('metrics', 'event_generator', constraint='false', style='dotted', color='#FFD70080')

    filepath = dot.render('docs/sandbox_architecture', cleanup=True)
    print(f"✅ 沙盒架构图已生成：{filepath}")
    return filepath


# ============================================================
# 图 2: 攻击 - 防守对抗流程
# ============================================================
def generate_attack_defense_flow():
    dot = Digraph('Attack-Defense Flow', format='png', engine='dot')
    dot.attr(
        rankdir='LR',
        size='18,10',
        dpi='300',
        bgcolor='transparent',
        fontname='Arial',
        label='攻击 - 防守对抗流程',
        labelloc='t',
        fontsize='18',
    )

    # 攻击方
    with dot.subgraph(name='cluster_attacker') as s:
        s.attr(label=' 攻击方 (Adversary)', style='filled', fillcolor='#FFE0E0', fontsize='14')
        s.node('adv_input', '对抗输入\n(手写扰动)', shape='box', style='filled,rounded', fillcolor='#FF4444', fontcolor='white')
        s.node('adv_noise', '噪声层\n(高斯/椒盐)', shape='box', style='filled,rounded', fillcolor='#FF4444', fontcolor='white')
        s.node('adv_logic', '逻辑陷阱\n(矛盾陈述)', shape='box', style='filled,rounded', fillcolor='#FF4444', fontcolor='white')
        s.node('adv_combine', '攻击融合', shape='diamond', style='filled', fillcolor='#FF4444', fontcolor='white')

    # 防守方
    with dot.subgraph(name='cluster_defender') as s:
        s.attr(label='🔵 防守方 (Defender)', style='filled', fillcolor='#E0E0FF', fontsize='14')
        s.node('def_detect', '异常检测\n(置信度阈值)', shape='box', style='filled,rounded', fillcolor='#4444FF', fontcolor='white')
        s.node('def_analyze', '攻击分析\n(类型识别)', shape='box', style='filled,rounded', fillcolor='#4444FF', fontcolor='white')
        s.node('def_mitigate', '缓解策略\n(去噪/修复)', shape='box', style='filled,rounded', fillcolor='#4444FF', fontcolor='white')
        s.node('def_verify', '结果验证\n(一致性检查)', shape='box', style='filled,rounded', fillcolor='#4444FF', fontcolor='white')

    # 评估
    with dot.subgraph(name='cluster_eval_flow') as s:
        s.attr(label='📊 评估模块', style='filled', fillcolor='#E0FFE0', fontsize='14')
        s.node('eval_asr', '攻击成功率\n(ASR)', shape='box', style='filled,rounded', fillcolor='#44AA44', fontcolor='white')
        s.node('eval_robust', '鲁棒性分数', shape='box', style='filled,rounded', fillcolor='#44AA44', fontcolor='white')
        s.node('eval_feedback', '反馈优化', shape='hexagon', style='filled', fillcolor='#44AA44', fontcolor='white')

    # 流程连接
    dot.edge('adv_input', 'adv_noise')
    dot.edge('adv_noise', 'adv_logic')
    dot.edge('adv_logic', 'adv_combine')

    dot.edge('adv_combine', 'def_detect', penwidth='3', color='#FF0000')

    dot.edge('def_detect', 'def_analyze')
    dot.edge('def_analyze', 'def_mitigate')
    dot.edge('def_mitigate', 'def_verify')

    dot.edge('def_verify', 'eval_asr')
    dot.edge('def_verify', 'eval_robust')

    dot.edge('eval_asr', 'eval_feedback', style='dashed')
    dot.edge('eval_robust', 'eval_feedback', style='dashed')

    # 反馈循环
    dot.edge('eval_feedback', 'adv_input', constraint='false', style='dotted', label='迭代优化')
    dot.edge('eval_feedback', 'def_detect', constraint='false', style='dotted', label='策略更新')

    filepath = dot.render('docs/attack_defense_flow', cleanup=True)
    print(f"✅ 攻守对抗流程图已生成：{filepath}")
    return filepath


# ============================================================
# 图 3: 轨迹数据生成与评估
# ============================================================
def generate_trajectory_pipeline():
    dot = Digraph('Trajectory Pipeline', format='png', engine='dot')
    dot.attr(
        rankdir='TB',
        size='20,24',
        dpi='300',
        bgcolor='transparent',
        fontname='Arial',
        label='''📊 轨迹数据生成与评估流水线
第一性原理：运气因子 (~10%) + 知识点匹配 + 防背题机制''',
        labelloc='t',
        fontsize='16',
        fontcolor='#2C3E50',
    )

    # 阶段 1: 数据采集
    with dot.subgraph(name='cluster_collect') as s:
        s.attr(label='📥 数据采集', style='filled,rounded', fillcolor='#FFF0E0',
               fontsize='13', penwidth='2', color='#FFB380')
        s.node('raw_events', '原始事件\n(决策点)', shape='box',
               style='filled,rounded', fillcolor='#FFA07A', penwidth='1.5')
        s.node('raw_states', '状态序列\n(S₁,S₂,...,Sn)', shape='box',
               style='filled,rounded', fillcolor='#FFA07A', penwidth='1.5')
        s.node('raw_actions', '动作序列\n(A₁,A₂,...,An)', shape='box', style='filled,rounded', fillcolor='#FFA07A')
        s.node('raw_rewards', '奖励信号\n(R₁,R₂,...,Rn)', shape='box', style='filled,rounded', fillcolor='#FFA07A')

    # 阶段 2: 轨迹编码
    with dot.subgraph(name='cluster_encode') as s:
        s.attr(label='📐 轨迹编码', style='filled', fillcolor='#E0FFF0', fontsize='14')
        s.node('encode_sar', 'SAR 编码\n(State-Action-Reward)', shape='box', style='filled,rounded', fillcolor='#66CDAA')
        s.node('encode_feature', '特征提取\n(决策特征)', shape='box', style='filled,rounded', fillcolor='#66CDAA')
        s.node('encode_label', '标签生成\n(正确/错误)', shape='box', style='filled,rounded', fillcolor='#66CDAA')

    # 阶段 3: 质量评估
    with dot.subgraph(name='cluster_quality') as s:
        s.attr(label='🔍 质量评估', style='filled', fillcolor='#E0E0FF', fontsize='14')

        s.node('quality_luck', '🎲 运气因子\n(~10% 概率)', shape='box', style='filled,rounded',
               fillcolor='#FFB6C1', fontsize='10')
        s.node('quality_knowledge', '知识点匹配评估\n(掌握度 vs 题目)', shape='box',
               style='filled,rounded', fillcolor='#9370DB', fontsize='10')
        s.node('quality_variant', '变形式验证\n(防背题检测)', shape='box',
               style='filled,rounded', fillcolor='#9370DB', fontsize='10')
        s.node('quality_filter', '质量过滤\n(真理解/假理解)', shape='diamond',
               style='filled', fillcolor='#9370DB', fontsize='10')

        s.edge('quality_luck', 'quality_knowledge', style='dotted', color='#FF69B480')
        s.edge('quality_knowledge', 'quality_filter')
        s.edge('quality_variant', 'quality_filter')

    # 阶段 4: 数据存储
    with dot.subgraph(name='cluster_store') as s:
        s.attr(label='💾 数据存储 + 知识追踪', style='filled', fillcolor='#FFF8E0', fontsize='14')
        s.node('store_train', '训练集\n(80%)', shape='cylinder', style='filled', fillcolor='#FFD700')
        s.node('store_knowledge', '知识追踪\n(IRT/BKT 模型)', shape='hexagon', style='filled', fillcolor='#BA68C8')
        s.node('store_variant', '变式题库\n(同一知识点多题)', shape='cylinder', style='filled', fillcolor='#FFD700')

    # 阶段 5: 批改优化
    with dot.subgraph(name='cluster_optimize') as s:
        s.attr(label='⚙️ 批改优化', style='filled', fillcolor='#FFE0F0', fontsize='14')
        s.node('opt_model', '批改模型\n(Grader)', shape='box', style='filled,rounded', fillcolor='#DB7093')
        s.node('opt_train', '模型训练\n(CrossEntropy)', shape='box', style='filled,rounded', fillcolor='#DB7093')
        s.node('opt_eval', '性能评估\n(Acc/F1/AUC)', shape='box', style='filled,rounded', fillcolor='#DB7093')
        s.node('opt_deploy', '部署更新', shape='hexagon', style='filled', fillcolor='#DB7093')

    # 连接
    dot.edge('raw_events', 'encode_sar')
    dot.edge('raw_states', 'encode_sar')
    dot.edge('raw_actions', 'encode_sar')
    dot.edge('raw_rewards', 'encode_sar')

    dot.edge('encode_sar', 'encode_feature')
    dot.edge('encode_feature', 'encode_label')

    dot.edge('encode_label', 'quality_knowledge')
    dot.edge('encode_label', 'quality_variant')
    dot.edge('encode_label', 'quality_luck')

    dot.edge('quality_filter', 'store_train')
    dot.edge('quality_filter', 'store_knowledge')
    dot.edge('quality_filter', 'store_variant')

    dot.edge('store_train', 'opt_model')
    dot.edge('store_knowledge', 'opt_eval')
    dot.edge('store_variant', 'opt_eval')

    dot.edge('opt_eval', 'opt_deploy')
    dot.edge('opt_deploy', 'opt_model', constraint='false', style='dashed', label='模型更新')

    filepath = dot.render('docs/trajectory_pipeline', cleanup=True)
    print(f"✅ 轨迹流水线图已生成：{filepath}")
    return filepath


# ============================================================
# 图 4: 人生阶段决策树
# ============================================================
def generate_life_decision_tree():
    dot = Digraph('Life Decision Tree', format='png', engine='dot')
    dot.attr(
        rankdir='TB',
        size='20,24',
        dpi='300',
        bgcolor='transparent',
        fontname='Arial',
        label='人生阶段决策树 - 完整仿真路径',
        labelloc='t',
        fontsize='20',
    )

    # 阶段颜色
    stage_colors = {
        '幼儿园': '#FFB6C1',
        '小学': '#98FB98',
        '初中': '#87CEEB',
        '高中': '#DDA0DD',
        '大学': '#FFA07A',
        '职业': '#F0E68C',
        '退休': '#B0C4DE',
    }

    # 创建各阶段节点
    stages = ['幼儿园', '小学', '初中', '高中', '大学', '职业', '退休']

    for i, stage in enumerate(stages):
        with dot.subgraph(name=f'cluster_{stage}') as s:
            s.attr(label=f'{stage}阶段', style='filled', fillcolor=f'{stage_colors[stage]}40', fontsize='14')

            # 阶段入口
            s.node(f'{stage}_entry', f'{stage}\n(入口)', shape='doublecircle', style='filled', fillcolor=stage_colors[stage])

            # 事件节点
            if i < 6:  # 退休没有后续
                s.node(f'{stage}_event1', '事件 A\n(学习/成长)', shape='box', style='filled,rounded', fillcolor=stage_colors[stage])
                s.node(f'{stage}_event2', '事件 B\n(挑战/机遇)', shape='box', style='filled,rounded', fillcolor=stage_colors[stage])

                # 决策分支
                s.node(f'{stage}_choice1', '选择 1', shape='diamond', style='filled', fillcolor='#FFFFFF')
                s.node(f'{stage}_choice2', '选择 2', shape='diamond', style='filled', fillcolor='#FFFFFF')
                s.node(f'{stage}_choice3', '选择 3', shape='diamond', style='filled', fillcolor='#FFFFFF')

                # 技能获取
                s.node(f'{stage}_skill', '技能获取\n(+EXP)', shape='hexagon', style='filled', fillcolor='#90EE90')

                # 内部连接
                s.edge(f'{stage}_entry', f'{stage}_event1')
                s.edge(f'{stage}_entry', f'{stage}_event2')
                s.edge(f'{stage}_event1', f'{stage}_choice1')
                s.edge(f'{stage}_event1', f'{stage}_choice2')
                s.edge(f'{stage}_event2', f'{stage}_choice2')
                s.edge(f'{stage}_event2', f'{stage}_choice3')
                s.edge(f'{stage}_choice1', f'{stage}_skill')
                s.edge(f'{stage}_choice2', f'{stage}_skill')
                s.edge(f'{stage}_choice3', f'{stage}_skill')

    # 阶段间连接
    for i in range(len(stages) - 1):
        current = stages[i]
        next_stage = stages[i + 1]
        dot.edge(f'{current}_skill', f'{next_stage}_entry', penwidth='2', color='#666666', label=f'→ {next_stage}')

    # 攻击点标记
    for stage in stages[:5]:
        dot.node(f'{stage}_attack', '⚠️ 攻击点', shape='triangle', style='filled', fillcolor='#FF6B6B', fontcolor='white')
        dot.edge(f'{stage}_choice1', f'{stage}_attack', style='dashed', color='#FF0000')

    # 防守点标记
    for stage in stages[:5]:
        dot.node(f'{stage}_defense', '🛡️ 防守点', shape='invtriangle', style='filled', fillcolor='#4169E1', fontcolor='white')
        dot.edge(f'{stage}_attack', f'{stage}_defense', style='dotted', color='#0000FF')

    filepath = dot.render('docs/life_decision_tree', cleanup=True)
    print(f"✅ 人生决策树已生成：{filepath}")
    return filepath


# ============================================================
# 图 4: 人类技能体系 v2 (学术/认知/社交/实践)
# ============================================================
def generate_skill_tree_v2():
    """人类基本技能体系 - 更贴近真实学习成长"""
    dot = Digraph('Skill Tree v2', format='png', engine='dot')
    dot.attr(
        rankdir='TB',
        size='20,16',
        dpi='300',
        bgcolor='transparent',
        fontname='Arial',
        label='🧠 人类技能体系 v2.0\n学术能力 × 认知能力 × 社交能力 × 实践能力',
        labelloc='t',
        fontsize='20',
    )

    colors = {
        'academic': '#E3F2FD',
        'cognitive': '#F3E5F5',
        'social': '#E8F5E9',
        'practical': '#FFF3E0',
    }

    # 学术能力
    with dot.subgraph(name='cluster_academic') as s:
        s.attr(label='📚 学术能力', style='filled', fillcolor=colors['academic'], fontsize='14', penwidth='2')

        s.node('lang', '语言能力\n(阅读/写作/表达)', shape='box', style='filled,rounded',
               fillcolor='#64B5F6', fontsize='11')
        s.node('math', '数学能力\n(逻辑/计算/建模)', shape='box', style='filled,rounded',
               fillcolor='#64B5F6', fontsize='11')
        s.node('science', '科学素养\n(物理/化学/生物)', shape='box', style='filled,rounded',
               fillcolor='#64B5F6', fontsize='11')
        s.node('humanities', '人文素养\n(历史/地理/文化)', shape='box', style='filled,rounded',
               fillcolor='#64B5F6', fontsize='11')

    # 认知能力
    with dot.subgraph(name='cluster_cognitive') as s:
        s.attr(label='🧩 认知能力', style='filled', fillcolor=colors['cognitive'], fontsize='14', penwidth='2')

        s.node('memory', '记忆力\n(工作记忆/长时记忆)', shape='box', style='filled,rounded',
               fillcolor='#BA68C8', fontsize='11')
        s.node('attention', '注意力\n(专注/分配/切换)', shape='box', style='filled,rounded',
               fillcolor='#BA68C8', fontsize='11')
        s.node('reasoning', '推理能力\n(演绎/归纳/类比)', shape='box', style='filled,rounded',
               fillcolor='#BA68C8', fontsize='11')
        s.node('metacognition', '元认知\n(自我监控/调节)', shape='box', style='filled,rounded',
               fillcolor='#BA68C8', fontsize='11')

    # 社交能力
    with dot.subgraph(name='cluster_social') as s:
        s.attr(label='🤝 社交能力', style='filled', fillcolor=colors['social'], fontsize='14', penwidth='2')

        s.node('communication', '沟通能力\n(倾听/表达/反馈)', shape='box', style='filled,rounded',
               fillcolor='#81C784', fontsize='11')
        s.node('collaboration', '协作能力\n(团队/领导/协调)', shape='box', style='filled,rounded',
               fillcolor='#81C784', fontsize='11')
        s.node('empathy', '共情能力\n(理解/回应情感)', shape='box', style='filled,rounded',
               fillcolor='#81C784', fontsize='11')
        s.node('conflict', '冲突解决\n(协商/调解)', shape='box', style='filled,rounded',
               fillcolor='#81C784', fontsize='11')

    # 实践能力
    with dot.subgraph(name='cluster_practical') as s:
        s.attr(label='🛠️ 实践能力', style='filled', fillcolor=colors['practical'], fontsize='14', penwidth='2')

        s.node('problem_solve', '问题解决\n(分析/方案/执行)', shape='box', style='filled,rounded',
               fillcolor='#FFB74D', fontsize='11')
        s.node('creativity', '创造力\n(发散/聚合思维)', shape='box', style='filled,rounded',
               fillcolor='#FFB74D', fontsize='11')
        s.node('time_mgmt', '时间管理\n(规划/优先级)', shape='box', style='filled,rounded',
               fillcolor='#FFB74D', fontsize='11')
        s.node('adaptability', '适应力\n(应变/学习迁移)', shape='box', style='filled,rounded',
               fillcolor='#FFB74D', fontsize='11')

    # 跨领域连接
    dot.edge('lang', 'communication', style='dashed', color='#90CAF9', penwidth='2',
             label='表达→沟通')
    dot.edge('math', 'reasoning', style='dashed', color='#90CAF9', penwidth='2',
             label='逻辑→推理')
    dot.edge('reasoning', 'problem_solve', style='dashed', color='#90CAF9', penwidth='2',
             label='推理→解决问题')
    dot.edge('attention', 'time_mgmt', style='dashed', color='#90CAF9', penwidth='2',
             label='专注→时间管理')
    dot.edge('metacognition', 'adaptability', style='dashed', color='#90CAF9', penwidth='2',
             label='自我调节→适应力')

    filepath = dot.render('docs/skill_tree_v2', cleanup=True)
    print(f"✅ 人类技能体系图 v2 已生成：{filepath}")
    return filepath


# ============================================================
# 图 5: 学习成长决策树 v2 (基于技能发展)
# ============================================================
def generate_life_decision_tree_v2():
    """学习成长决策树 - 基于技能发展的真实路径"""
    dot = Digraph('Decision Tree v2', format='png', engine='dot')
    dot.attr(
        rankdir='TB',
        size='18,20',
        dpi='300',
        bgcolor='transparent',
        fontname='Arial',
        label='📚 学习成长决策树 v2.0\n基于技能发展的教育路径',
        labelloc='t',
        fontsize='20',
    )

    colors = {
        'stage': '#E3F2FD',
        'choice': '#FFF3E0',
        'skill': '#E8F5E9',
        'outcome': '#F3E5F5',
    }

    stages = [
        ('启蒙期', '3-6 岁', '语言/认知启蒙', '#FFCDD2'),
        ('基础期', '6-12 岁', '学科基础建立', '#C8E6C9'),
        ('发展期', '12-15 岁', '抽象思维发展', '#FFF9C4'),
        ('深化期', '15-18 岁', '专业能力深化', '#B2DFDB'),
        ('专业期', '18-22 岁', '专业方向选择', '#FFCCBC'),
        ('实践期', '22-60 岁', '职业发展/终身学习', '#D1C4E9'),
    ]

    for i, (stage_name, age_range, focus, color) in enumerate(stages):
        with dot.subgraph(name=f'cluster_stage_{i}') as s:
            s.attr(label=f'{stage_name}', style='filled', fillcolor=colors['stage'],
                   fontsize='13', penwidth='2')

            # 阶段节点
            s.node(f'stage_{i}', f'{stage_name}\n{age_range}\n重点：{focus}',
                   shape='box', style='filled,rounded', fillcolor=color,
                   fontsize='11', penwidth='2')

            # 关键决策点
            if i < len(stages) - 1:
                s.node(f'choice_{i}', '关键决策', shape='diamond',
                       style='filled', fillcolor='#FFE0B2', fontsize='10')

                next_stage = stages[i + 1]
                s.node(f'path_a', '学术路线\n(深入学习)', shape='box',
                       style='filled,rounded', fillcolor='#A5D6A7', fontsize='9')
                s.node(f'path_b', '实践路线\n(应用探索)', shape='box',
                       style='filled,rounded', fillcolor='#90CAF9', fontsize='9')

                s.edge(f'stage_{i}', f'choice_{i}', penwidth='2')
                s.edge(f'choice_{i}', 'path_a', penwidth='2', color='#2E7D32')
                s.edge(f'choice_{i}', 'path_b', penwidth='2', color='#1565C0')

                # 技能获取
                s.node(f'skill_{i}', '技能发展', shape='hexagon',
                       style='filled', fillcolor='#C8E6C9', fontsize='10')
                s.edge('path_a', f'skill_{i}', style='dashed')
                s.edge('path_b', f'skill_{i}', style='dashed')

    # 阶段间连接
    for i in range(len(stages) - 1):
        dot.edge(f'skill_{i}', f'stage_{i+1}', penwidth='2', color='#1976D2',
                 label='进入下一阶段', fontsize='9')

    # 评估与反馈
    with dot.subgraph(name='cluster_eval') as s:
        s.attr(label='📊 评估与反馈', style='filled', fillcolor=colors['outcome'],
               fontsize='13', penwidth='2')

        s.node('assess', '能力评估\n(标准化测试)', shape='box',
               style='filled,rounded', fillcolor='#CE93D8', fontsize='10')
        s.node('feedback', '反馈调整\n(弱项强化)', shape='box',
               style='filled,rounded', fillcolor='#CE93D8', fontsize='10')
        s.node('optimize', '路径优化\n(动态调整)', shape='note',
               style='filled', fillcolor='#CE93D8', fontsize='10')

        s.edge('assess', 'feedback')
        s.edge('feedback', 'optimize')

    # 评估连接到各阶段
    dot.edge('skill_4', 'assess', penwidth='2', color='#7B1FA2',
             label='阶段性评估', constraint='false')
    dot.edge('optimize', 'choice_2', penwidth='1.5', color='#7B1FA2',
             style='dotted', label='反馈调整', constraint='false')
    dot.edge('optimize', 'choice_3', penwidth='1.5', color='#7B1FA2',
             style='dotted', constraint='false')

    filepath = dot.render('docs/life_decision_tree_v2', cleanup=True)
    print(f"✅ 学习成长决策树 v2 已生成：{filepath}")
    return filepath


# ============================================================
# 图 6: 人生沙盒核心流程 (美化版)
# ============================================================
def generate_sandbox_flow_v2():
    """美化版人生沙盒流程图 - 展示完整的事件驱动和成长系统"""
    dot = Digraph('Sandbox Flow v2', format='png', engine='dot')
    dot.attr(
        rankdir='TB',
        size='24,18',
        dpi='300',
        bgcolor='transparent',
        fontname='Arial',
        label='''🎮 人生沙盒核心流程 v2.0
事件驱动 × 选择分支 × 技能成长 × 攻守对抗''',
        labelloc='t',
        fontsize='22',
    )

    # 颜色方案
    colors = {
        'stage': '#E3F2FD',
        'event': '#FFF3E0',
        'choice': '#F3E5F5',
        'skill': '#E8F5E9',
        'attack': '#FFEBEE',
        'defense': '#ECEFF1',
    }

    # === 第 1 层：人生阶段 ===
    with dot.subgraph(name='cluster_stages') as s:
        s.attr(label='📍 人生阶段', style='filled', fillcolor=colors['stage'], fontsize='14', penwidth='2')

        stages = [
            ('kindergarten', '幼儿园\n(3-6 岁)', '#FFCDD2'),
            ('primary', '小学\n(6-12 岁)', '#C8E6C9'),
            ('middle', '初中\n(12-15 岁)', '#FFF9C4'),
            ('high', '高中\n(15-18 岁)', '#B2DFDB'),
            ('university', '大学\n(18-22 岁)', '#FFCCBC'),
            ('career', '职业\n(22-60 岁)', '#D1C4E9'),
            ('retirement', '退休\n(60 岁+)', '#BCAAA4'),
        ]

        prev_stage = None
        for stage_id, stage_label, color in stages:
            s.node(stage_id, stage_label, shape='box', style='filled,rounded',
                   fillcolor=color, fontsize='13', penwidth='2')
            if prev_stage:
                s.edge(prev_stage, stage_id, penwidth='3', color='#1976D2',
                       label='阶段推进', fontsize='10')
            prev_stage = stage_id

    # === 第 2 层：事件系统 ===
    with dot.subgraph(name='cluster_events') as s:
        s.attr(label='🎲 事件系统', style='filled', fillcolor=colors['event'], fontsize='14', penwidth='2')

        s.node('event_trigger', '事件触发\n(随机/ scripted)', shape='hexagon',
               style='filled', fillcolor='#FFB74D', fontsize='12', penwidth='2')

        s.node('event_learn', '📚 学习事件\n(上课/培训)', shape='box',
               style='filled,rounded', fillcolor='#81C784', fontsize='11')
        s.node('event_challenge', '⚡ 挑战事件\n(考试/面试)', shape='box',
               style='filled,rounded', fillcolor='#E57373', fontsize='11', fontcolor='white')
        s.node('event_opportunity', '🎁 机遇事件\n(社团/项目)', shape='box',
               style='filled,rounded', fillcolor='#64B5F6', fontsize='11')
        s.node('event_random', '🎰 随机事件\n(偶遇/意外)', shape='box',
               style='filled,rounded', fillcolor='#BA68C8', fontsize='11')

        s.edge('event_trigger', 'event_learn', style='dashed', color='#81C78480')
        s.edge('event_trigger', 'event_challenge', style='dashed', color='#E5737380')
        s.edge('event_trigger', 'event_opportunity', style='dashed', color='#64B5F680')
        s.edge('event_trigger', 'event_random', style='dashed', color='#BA68C880')

    # === 第 3 层：选择系统 ===
    with dot.subgraph(name='cluster_choices') as s:
        s.attr(label='🤔 选择系统', style='filled', fillcolor=colors['choice'], fontsize='14', penwidth='2')

        s.node('choice_branch', '决策分支点', shape='diamond',
               style='filled', fillcolor='#CE93D8', fontsize='12', penwidth='2')

        s.node('choice_a', '选择 A\n(保守路线)', shape='box',
               style='filled,rounded', fillcolor='#A5D6A7', fontsize='10')
        s.node('choice_b', '选择 B\n(冒险路线)', shape='box',
               style='filled,rounded', fillcolor='#EF9A9A', fontsize='10')
        s.node('choice_c', '选择 C\n(平衡路线)', shape='box',
               style='filled,rounded', fillcolor='#90CAF9', fontsize='10')

        s.edge('choice_branch', 'choice_a', style='solid', color='#2E7D32')
        s.edge('choice_branch', 'choice_b', style='solid', color='#C62828')
        s.edge('choice_branch', 'choice_c', style='solid', color='#1565C0')

    # === 第 4 层：技能成长 ===
    with dot.subgraph(name='cluster_skills') as s:
        s.attr(label='📈 技能成长系统', style='filled', fillcolor=colors['skill'], fontsize='14', penwidth='2')

        s.node('skill_exp', '经验获取\n(+EXP)', shape='hexagon',
               style='filled', fillcolor='#81C784', fontsize='11')

        s.node('skill_tree', '技能树\n(学科/软技能)', shape='box',
               style='filled', fillcolor='#4DB6AC', fontsize='11')
        s.node('skill_level', '等级提升\n(Level Up)', shape='box',
               style='filled', fillcolor='#4DB6AC', fontsize='11')
        s.node('skill_achievement', '成就解锁\n(里程碑)', shape='note',
               style='filled', fillcolor='#FFD54F', fontsize='11')

        s.edge('skill_exp', 'skill_tree', style='dashed')
        s.edge('skill_tree', 'skill_level', style='dashed')
        s.edge('skill_level', 'skill_achievement', style='dashed')

    # === 第 5 层：攻守对抗 ===
    with dot.subgraph(name='cluster_combat') as s:
        s.attr(label='⚔️ 攻守对抗', style='filled', fillcolor='#FFCDD2', fontsize='14', penwidth='2')

        # 攻击方
        with s.subgraph(name='cluster_attacker_flow') as att:
            att.attr(label='🔴 攻击方', style='filled', fillcolor='#FFEBEE', fontsize='12')
            att.node('atk_noise', '噪声攻击\n(模糊/遮挡)', shape='box',
                    style='filled,rounded', fillcolor='#EF5350', fontsize='10', fontcolor='white')
            att.node('atk_logic', '逻辑攻击\n(矛盾/陷阱)', shape='box',
                    style='filled,rounded', fillcolor='#EF5350', fontsize='10', fontcolor='white')
            att.edge('atk_noise', 'atk_logic', style='dotted', color='#C62828')

        # 防守方
        with s.subgraph(name='cluster_defender_flow') as dfn:
            dfn.attr(label='🔵 防守方', style='filled', fillcolor='#E3F2FD', fontsize='12')
            dfn.node('def_detect', '攻击检测\n(异常识别)', shape='box',
                    style='filled,rounded', fillcolor='#42A5F5', fontsize='10', fontcolor='white')
            dfn.node('def_mitigate', '缓解策略\n(去噪/修复)', shape='box',
                    style='filled,rounded', fillcolor='#42A5F5', fontsize='10', fontcolor='white')
            dfn.edge('def_detect', 'def_mitigate', style='dotted', color='#1565C0')

        # 攻守连接
        s.edge('atk_logic', 'def_detect', penwidth='2', color='#F44336')

    # === 跨层连接 ===
    # 阶段 → 事件
    dot.edge('middle', 'event_trigger', penwidth='2', color='#1976D2', constraint='false')

    # 事件 → 选择
    dot.edge('event_learn', 'choice_branch', penwidth='2', color='#FF9800')
    dot.edge('event_challenge', 'choice_branch', penwidth='2', color='#F44336')
    dot.edge('event_opportunity', 'choice_branch', penwidth='2', color='#2196F3')

    # 选择 → 技能
    dot.edge('choice_a', 'skill_exp', penwidth='2', color='#4CAF50')
    dot.edge('choice_b', 'skill_exp', penwidth='2', color='#F44336')
    dot.edge('choice_c', 'skill_exp', penwidth='2', color='#2196F3')

    # 技能 → 攻守
    dot.edge('skill_tree', 'atk_noise', penwidth='1.5', color='#EF5350',
             style='dashed', label='技能依赖')
    dot.edge('skill_level', 'def_detect', penwidth='1.5', color='#42A5F5',
             style='dashed', label='等级增益')

    # 攻守 → 下一阶段 (反馈)
    dot.edge('def_mitigate', 'primary', penwidth='1.5', color='#9E9E9E',
             style='dotted', label='防御成功→推进', constraint='false')
    dot.edge('atk_logic', 'primary', penwidth='1.5', color='#F44336',
             style='dotted', label='攻击成功→阻碍', constraint='false')

    # 成就解锁反馈
    dot.edge('skill_achievement', 'kindergarten', penwidth='2', color='#FFD54F',
             style='dashed', label='成就解锁新路径', constraint='false')

    filepath = dot.render('docs/sandbox_flow_v2', cleanup=True)
    print(f"✅ 人生沙盒核心流程图 v2 已生成：{filepath}")
    return filepath


if __name__ == '__main__':
    generate_sandbox_architecture()
    generate_attack_defense_flow()
    generate_trajectory_pipeline()
    generate_skill_tree_v2()
    generate_life_decision_tree_v2()
    generate_sandbox_flow_v2()
    print("\n✅ 所有人生沙盒架构图已生成到 docs/ 目录")
