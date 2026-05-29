# Question Patterns

Ask at most one question. Prefer a default statement when stored preferences or safe defaults are enough.

## Open-ended stock review

Question:

```text
你想重点看价格趋势、估值指标、同业对比，还是风险变化？如果你不指定，我会默认按最近一年从趋势、估值和风险三个角度看。
```

Default statement:

```text
我会按最近一年，从趋势、估值和风险三个角度看，先给文字结论和关键表格；不自动生成 HTML 图表。
```

## Comparison With Missing Benchmark

Question:

```text
你想和哪一个标的或基准对比？如果不指定，我会优先使用同类标的或可用基准做参考。
```

## Date Range Unknown

Default statement:

```text
我会先按最近一年分析；如果你有指定日期区间，我可以改用你的区间。
```

## Visualization preference

Question:

```text
你需要我生成可视化 HTML 报告吗？如果不需要，我先给文字结论和关键表格。
```

Default statement:

```text
我先不生成可视化 HTML；你需要图表时我再调用可视化报告流程。
```

## Personalized Analysis Missing Investment Profile

Question:

```text
你希望我按什么投资周期和风险偏好来看？如果不提供，我会只做客观数据分析，不套用个人画像。
```
