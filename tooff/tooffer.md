剑指offer上面的66道算法题是面试高频题

## 1.二维数组中的查找

在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

**思路**

1.暴力遍历整个数组，*O*(n**2)

2.类似于二分查找，根据题目，如果拿数组中任意一个元素与目标数值进行比较，如果该元素小于目标数值，那么目标数值一定是在该元素的下方或右方，如果大于目标数值，那么目标数值一定在该元素的上方或者左方。  对于二分查找来说，每次比较只能移动一个指针，在二维数组的查找中，两个指针是一个上下方向移动，一个是左右方向移动。两个指针可以从同一个角出发。  假设我们从左上角出发，也就是row=0 和 col=0，如果元素小于目标数值，我们会将row往下移或着col往右移，这样，被屏蔽的区域可能会是目标元素所在的区域。比如row+=1，那么第一行除左上角以外的元素就被忽略了，如果col+=1，那么第一列出左上角以外的元素就被忽略了。因此这样是不可行的。所以本题从右上角出发寻找解题思路。

**代码**

```python
class Solution:
    def Find(self, target, array):
        rows = len(array)-1
        cols = len(array[0]) - 1
        i = rows
        j = 0
        while j<=cols and i>=0:
            if target<array[i][j]:
                i -= 1
            elif target>array[i][j]:
                j += 1
            else:
                return True
        return False
```

## 2.替换空格

请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

**代码**

```python
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        result = ''
        for char in s:
            if char == ' ':
                result += '%20'
            else:
                result += char
        return result
```

## 3.从尾到头打印链表

输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

**思路：**使用栈从头到尾push链表的元素，然后pop所有的元素到一个list中并返回。

**代码**

```python
class Solution:
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []
        p = listNode
        stack = []
        res = []
        while p:
            stack.append(p.val)
            p = p.next
        for i in range(len(stack)-1,-1,-1):
             res.append(stack[i])
        return res
```

## 4.重建二叉树

输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

**思路：**先序遍历和中序遍历的关系，先序遍历的第一个值是根节点的值。在中序遍历中，根节点左边的值是左子树，右边的值是右子树上的值。

**代码**

```python
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre:
            return None
        root = TreeNode(pre[0])
        n = tin.index(root.val)    #找到根节点在中序遍历中的下标
        root.left = self.reConstructBinaryTree(pre[1:n+1],tin[:n])
        root.right = self.reConstructBinaryTree(pre[n+1:],tin[n+1:])
        return root
```

## 7.斐波那契数列

要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0），n<=39。

**思路：**菲波那切数列：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）

只需定义3个整型变量，num2表示后面的一个数字，num2表示前面的数字，target为二者之和即可。

**代码**

```python
class Solution:
    def Fibonacci(self, n):
        num1 = 0
        num2 = 1
        target = 0
        for i in range(0,n):
            num1 = num2
            num2 = target
            target = num1 + num2
        return target
```

## 8.跳台阶

一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

**思路：**

一只青蛙可以跳上1级台阶，也可以跳上2两级台阶
当n = 1时，有1种跳法
当n = 2时，有2种跳法
当n = 3时，有3种跳法
当n = 4时，有5种跳法
当n = 5时，有8种跳法
...
等等，1，2，3，5，8...，多么熟悉的数列，斐波那契？

青蛙第一步可以选择跳上1级台阶，则还剩n - 1级台阶需要跳，即F(n - 1)
青蛙第一步也可以选择跳上2级台阶，则还剩n - 2级台阶需要跳，即F(n - 2)

得出动态规划递推式： ![[公式]](https://www.zhihu.com/equation?tex=F%28n%29%3DF%28n-1%29%2BF%28n-2%29)

**代码**

```python
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        elif number == 2:
            return 2
        num1 = 1
        num2 = 2
        target = num1 + num2
        for i in range(2, number-1):
            num1 = num2
            num2 = target
            target = num1 + num2
        return target
```

## 9.变态跳台阶

一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级多少种跳法。

**思路：**
当n = 1时，有1种跳法
当n = 2时，有2种跳法
当n = 3时，有4种跳法
当n = 4时，有8种跳法
......

归纳法得出规律，然后直接由公式2**(n-1)。

```python
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        return 2**(number - 1)
```

## 11.二进制中1的个数

输入一个整数，输出该数二进制表示中1的个数。

**思路：**

如果整数不等于0，那么该整数的二进制表示中至少有1位是1。一个整数减去1，都是把最右边的1变成0，如果它后面还有0，那么0变成1。那么我们把一个整数减去1,与该整数做位运算，相当于把最右边的1变成了0，比如1100与1011做位与运算，得到1000。那么一个整数中有多少个1就可以做多少次这样的运算。

```python
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:#n小于0时会无限循环
            n = n & 0xffffffff
        while n!= 0:
            count += 1
            n = (n-1)& n
        return count
```

## 12.数值的整数次方

给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

**代码：**

```python
class Solution:
    def Power(self, base, exponent):
        if exponent==0: return 1
        if base==0: return 0
        temp = 1
        if exponent<0:
            abs_exponent = -exponent
            while abs_exponent>0:
                temp = temp*base
                abs_exponent = abs_exponent-1
            return 1/temp
        while exponent>0:
            temp = temp*base
            exponent = exponent-1
        return temp
```



## 13.调整数组顺序使奇数位于偶数前面

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

**代码：**

```python
class Solution:
    def reOrderArray(self, array):
        res1 = []
        res2 = []
        for i in array:
            if i%2==1:
                res1.append(i)
            else:
                res2.append(i)
        array = res1 + res2
        return array
```

## 14.链表中的倒数第K个节点

输入一个链表，输出该链表中倒数第k个结点。

**思路：**假设链表中的节点数大于等于k个，那么一定会存在倒数第k个节点，首先使用一个快指针先往前走k步，然后两个指针每次走一步，两个指针之间始终有k的距离，当快指针走到末尾时，慢指针所在的位置就是倒数第k个节点。

**代码:**

```python
class Solution:
    def FindKthToTail(self, head, k):
        if not head or k <=0:
            return None
        p = q = head
        t = 0
        while p and t < k:
            p = p.next
            t = t+1
        if t < k:
            return None
        while p != None:
            p = p.next
            q = q.next
        return q
```

## 28.数组中出现次数超过一半的数字

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

思路：直接用词典进行存储，然后查看数值大小

**代码:**

```Python
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):

        num_dict = {}
        lenght = len(numbers)
        result = 0
        for num in numbers:
            if num in num_dict:
            	num_dict[num] += 1
            else:
            	num_dict[num] = 1
            #num_dict[num] = num_dict.get(num,0)+1
            # try:
            #     num_dict[num] = num_dict[num] + 1
            # except:
            #     num_dict[num] = 1

        for key, values in num_dict.items():
            if values > lenght//2:
                result = key
        return result
```

### 29.最小的k个数：

排序然后取前k个：

**代码:**

```python
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput):
            return []
        tinput = sorted(tinput)
        return tinput[:k]
```

## 30.连续子数组的最大和

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:输入 [-2,1,-3,4,-1,2,1,-5,4],输出: 6

解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

**思路：**如果数组里所有的整数都是负数，那么选择最大的数即可，因为越累加越小。

正负数都有的情况，需要两个变量，一个是*global_max,从全局来看，每次最大的是什么组合，另一个是local_max*，和*global_max*相比，更新*global_max。*

**代码:**

```python
class Solution(object):
    def maxSubArray(self, nums):

        if max(nums) < 0:
            return max(nums)
     
        local_max, global_max = 0, 0
        for i in nums:
            local_max = max(0, local_max + i)
            global_max = max(global_max, local_max)
        return global_max
```

或者暴力求解：

```python
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        maxsum = -1e19
        for i in range(len(array)-1):
            for j in range(i+1, len(array)+1):
                maxsum = max(maxsum, sum(array[i:j]))
        return maxsum
```

## 31.整数中1出现的次数

遍历1到n，然后求包含1的整数个数，对10取余得到个位数，然后依次除以10。

**代码:**

```python
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        result = 0
        for num in range(1,n+1):
            while num != 0:
                if num%10 == 1:
                    result += 1
                num = num//10
        return result
```

