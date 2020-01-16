# This is a test file.
# 导入时间库，下面可以用它来控制程序休眠，进而记录真实时间
import time

# 目标计时时间
target_time = 300

# 再声明一个变量，用来记录初始时间
keep_time = 0

# 因为我们并不在while后控制循环的结束，所以这里将条件永远设置为真
# 但是这个时候需要注意的是，一定要在while代码块中明确循环跳出的条件，并且这个条件一定会在某一时刻达到，否则就会变成死循环。
while True:
    # 首先确定循环跳出的条件
    if keep_time > target_time:
        break

    # keep_time对3600取整除，就是小时
    h = keep_time // 3600
    # keep_time 对3600取余数，然后对60取整除，就是分钟
    m = keep_time % 3600 // 60
    # keep_time 对3600取余数，然后对60取余数，就是秒
    s = keep_time % 3600 % 60

    # 计算计时时间
    # 当计时时间大于3600秒时，时间超过1小时，将换算成时分秒的形式后打印
    if keep_time >= 3600:
        print(h, m, s)
    # 当计时时间大于等于60秒，并小于3600时候，将时间换算成分和秒的形式后打印
    elif keep_time >= 60:
        print(m, s)
    # 其他的时候，也就是keep_time时间小于60的时候,我们直接打印秒
    else:
        print(s)
    # 这里控制时间,我们程序休眠1秒，则计时增加一秒，与现实生活中的时间对应
    time.sleep(1)
    keep_time = keep_time + 1

