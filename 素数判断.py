import math

def is_prime(n):
    # 基础判断：处理小数字和明显非质数的尾数
    if n <= 1:
        return False
    if n in (2, 3, 5):
        return True
    last_digit = n % 10
    if last_digit not in (1, 3, 7, 9):
        return False  # 非1/3/7/9结尾的数为合数（已排除2和5）
    
    max_divisor = math.isqrt(n)  # 试除上限为平方根
    
    # 生成器：生成尾数为1/3/7/9的候选除数（3,7,9,11,13,17,19,...）
    def candidate_divisors():
        yield 3
        yield 7
        k = 1
        while True:
            base = 10 * k
            for delta in (1, 3, 7, 9):
                candidate = base + delta
                if candidate > max_divisor:
                    return
                yield candidate
            k += 1
    
    # 检查是否能被候选除数整除
    for d in candidate_divisors():
        if d >= n:
            break  # 避免d=n时的冗余检查（如n=3）
        if n % d == 0:
            return False
    return True