// 演示交互
function runDemo(type) {
    const output = document.getElementById('terminal-output');
    const demos = {
        teach: `
<span class="prompt">$</span> teach 数学 勾股定理

📚 [数学] 勾股定理
━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 这个概念可以用公式来表达：a² + b² = c²
   记住，数学语言是最精确的语言。

📝 已学习次数：1
💪 加油，学习新知识点总是需要时间的！
━━━━━━━━━━━━━━━━━━━━━━━━━━
`,
        quiz: `
<span class="prompt">$</span> quiz 数学 3

📝 数学测验 (3 题):

  1. x² - 4 = 0, x = ?
     ['±2', '±4', '2', '4']
  2. sin(90°) = ?
     ['0', '1', '-1', '0.5']
  3. log₂(8) = ?
     ['2', '3', '4', '6']

💬 请输入答案 (用逗号分隔):
`,
        grade: `
<span class="prompt">$</span> grade ±2,1,3

📊 批改结果：66.7 分 (C (及格))
  正确：2/3

  ✅ 第 1 题：±2 → ±2
  ✅ 第 2 题：1 → 1
  ❌ 第 3 题：3 → 正确答案是 3 (判错了)
`,
        sandbox: `
<span class="prompt">$</span> simulate 3

⏳ 模拟了 3 年的生活...

📌 发生了事件：社团招新 → 科技社
✨ 获得经验：社交能力 +10, 兴趣技能 +15

🎉 人生阶段推进！
   小学 → 初中
   年龄：15 岁
`
    };

    output.innerHTML = output.innerHTML + demos[type];
    output.scrollTop = output.scrollHeight;
}

// 平滑滚动
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// 导航栏滚动效果
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.background = 'rgba(26, 26, 46, 0.95)';
        navbar.style.backdropFilter = 'blur(10px)';
    } else {
        navbar.style.background = 'var(--dark)';
    }
});

// 统计数字动画
function animateStats() {
    const stats = document.querySelectorAll('.stat-number, .about-stat-number');
    stats.forEach(stat => {
        const text = stat.textContent;
        if (text.includes('+') || text.includes('v') || text.includes('MIT')) return;

        const num = parseInt(text);
        if (isNaN(num)) return;

        let current = 0;
        const increment = num / 50;
        const timer = setInterval(() => {
            current += increment;
            if (current >= num) {
                stat.textContent = text;
                clearInterval(timer);
            } else {
                stat.textContent = Math.floor(current) + (text.includes('行') ? '+' : '');
            }
        }, 30);
    });
}

// 页面加载完成后执行
window.addEventListener('load', () => {
    // 检查是否在视口中
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateStats();
            }
        });
    });

    document.querySelectorAll('.hero-stats, .about-stats').forEach(el => {
        observer.observe(el);
    });
});

console.log('%c🎓 EduAgent v2.0', 'font-size: 20px; color: #4ECDC4;');
console.log('%cAI 教育系统 | 多模态支持', 'font-size: 14px; color: #FF6B6B;');
console.log('GitHub: https://github.com/yourusername/eduagent');
