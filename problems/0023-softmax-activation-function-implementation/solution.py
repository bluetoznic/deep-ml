import math

def softmax(scores: list[float]) -> list[float]:
    max_score = max(scores)
    
    # 2. 减去最大值后再求 exp，防止溢出
    exps = [math.exp(s - max_score) for s in scores]
    
    # 3. 求和
    total = sum(exps)
    
    # 4. 返回结果
    return [e / total for e in exps]
