# -Prime-Number-Check-Optimization-
代码说明‌
‌基础判断‌

直接排除 n ≤ 1 的情况。
处理 2/3/5 的特殊质数。
若末位非 1/3/7/9，则直接返回 False（如 0/2/4/5/6/8 结尾的数）。
‌生成器逻辑‌

生成从 3 开始、尾数为 1/3/7/9 的候选除数（如 3,7,9,11,13,17,19,...）。
终止条件：候选除数超过 √n（避免无效计算）。
‌试除验证‌

若 n 被任意候选除数整除，则返回 False（合数）。
若所有候选除数均无法整除，则返回 True（质数）。

---------
进一步改进：
建立一个质数的m叉树存储，根据这个质数的树进行试除可以更使质数判断具有效率，也更容易进行质数扩增。
