import numpy as np

'''numpy的数据类型start
Numpy类型	            C类型	                描述
np.bool	                bool	                存储为字节的布尔值（True或False）
np.byte	                signed char	            平台定义
np.ubyte	            unsigned char	        平台定义
np.short	            short	                平台定义
np.ushort	            unsigned short	        平台定义
np.intc	                int	                    平台定义
np.uintc	            unsigned int	        平台定义
np.int_	                long	                平台定义
np.uint	                unsigned long	        平台定义
np.longlong	            long long	            平台定义
np.ulonglong	        unsigned long long	    平台定义
np.half/np.float16                              半精度浮点数：符号位，5位指数，10位尾数
np.single/np.float32    float	                平台定义的单精度浮点数：通常为符号位，8位指数，23位尾数
np.double/np.float64    double	                平台定义的双精度浮点数：通常为符号位，11位指数，52位尾数。
np.longdouble	        long double	            平台定义的扩展精度浮点数
np.csingle	            float complex	        复数，由两个单精度浮点数（实部和虚部）表示
np.cdouble	            double complex	        复数，由两个双精度浮点数（实部和虚部）表示。
np.clongdouble	        long double complex	    复数，由两个扩展精度浮点数（实部和虚部）表示。
numpy的数据类型end'''

# 构造二维数组
x = np.array([[1, 2, 3],
              [4, 5, 6]], dtype=np.single)

type(x)  # 返回结果：<class 'numpy.ndarray'>

print(x)


