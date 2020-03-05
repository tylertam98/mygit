# -*- coding:utf-8 -*-\
# *args 把参数打包成tuple供函数调用。**kwargs把 x = a，y=b打包成字典{x:a,y:b}供函数调用
import sys
sys.setrecursionlimit(20)

import operator

MAX=100 #环路最大顶点数
cur=0 #cur环路当前下标，
cntl=0 #cntl环路个数,
loopn=0 #loopn环路长度
loopfirst=0 #环路的第一个顶点
vexnum=50 #顶点个数
loop={} #当前环路
graph=[]
All={}#环路
edge=[0,10,10,1,1,11,11,0,1,12,12,3,3,13,13,1,3,14,14,1,1,15,15,1,1,16,
    16,1,1,17,17,1,1,24,24,2,2,22,22,2,2,23,23,1,1,18,18,4,4,19,19,1,2,20,20,4,4,21,
    21,2,4,25,25,26,25,27,27,26,26,27,27,4,26,4,4,28,28,29,29,4,4,32,32,4,4,33,33,4,4,34,
    34,4,4,30,30,5,5,31,31,4,5,35,35,6,6,37,37,6,6,36,36,5,5,38,38,5,5,39,39,5,5,40,
    40,7,7,41,41,5,5,43,43,5,5,45,45,8,8,44,44,5,8,46,46,8,5,47,47,9,9,48,48,5,9,49,
    49,5,5,42,42,0] #所有边
list1=['0首页', '1相册页', '2相机页', '3相册列表页', '4后处理页', '5发布页', '6好友列表页', '7预览页', '8位置选择页', '9可见性选择对话框',
             '10点击加号', '11回退至首页', '12点击箭头展开相册列表', '13点击箭头收起相册列表', '14选择相册',
             '15点击比例切换按钮', '16拖动/缩放', '17点击播放/暂停', '18点击下一步至后处理页', '19回退至相册页', '20拍照片/录视频', '21回退至相机页',
             '22切换前后置摄像头', '23点击相册tab', '24点击拍摄tab', '25点击"裁剪"tab', '26滑动裁剪滑块', '27滑动缩略图列表',
             '28点击"封面"tab', '29滑动选封面滑块', '30点击下一步至发布页', '31回退至后处理页', '32立即点其它的滤镜（包括无滤镜）',
             '33点击对比按钮', '34滑动滤镜滑杆', '35点击@', '36选择好友', '37搜索框输入并搜索', '38填写feed文字', '39通过发布页里的位置列表选择位置',
             '40点击缩略图', '41回退至发布页', '42点击发布', '43选择分享平台', '44选择位置', '45点击"所在位置"', '46搜索位置', '47点击"谁可以看"',
             '48选择"朋友"可见', '49选择"所有人"可见']
#设置顶点与环路数据结构
class Node:
    def __init__(self, index):
        self.index=index
        self.next = None
class allloop:
    def __init__(self, count=None):
        self.pl=None
        self.cnt=count

def Init():
    for i in range(vexnum):
        graph.append(Node(i))
        graph[i].next=None


def CreateGraph(i,j):
    add=Node(j)
    add.next=None
    temp=None
    if(graph[i].next==None):
        graph[i].next=add
    else:
        temp=graph[i].next
    while(temp):
        if(temp.next==None):
            temp.next=add
            break
        temp=temp.next

def printlist():
    t=None
    print("*******************************")
    for i in range(vexnum):
        print(i,":::",end='')
        t=graph[i].next
        while(t):
            print(t.index,"\t",end='')
            t=t.next
        print("\n")
    print("*******************************")    

def FirstAdj(v):
    #print("FirstAdj:",v)
    t=None
    for i in range(vexnum):
        if(graph[i].index==v):
            break
    t=graph[i].next
    #print("FirstAdj..t.index:",t.index)
    if(t==None):
        return -1
    else:
        return t.index

def NextAdj(v,w):
    #print("NextAdj:v=",v,"w=",w)
    t=None
    for i in range(vexnum):
        if(graph[i].index==v):
            break
    t=graph[i].next
    #print("t=",t)
    if(t==None):
        return -1
    while(1):
        if(t.index==w):
            t=t.next
            if(t==None):
                return -1
            else:
                return t.index
        else:
            t=t.next
            if(t==None):
                return -1
            else:
                continue

def DFStraverse(visit):
    global cur,loopfirst
    for v in range(vexnum):
        #print("DFStraverse:v更新了=",v)
        cur=0
        loopfirst=v
        loopn=0
        for i in range(vexnum):
            visit[i]=0
        #print("visit",visit)
        if(visit[v]==0):#####
            DFS(v,visit)
            

def DFS(v,visit):
    global cur,loopn,loopfirst,cntl
    visit[v]=1
    loop[cur]=v #######
    cur+=1
    loopn+=1
    #print("v",v)
    w=FirstAdj(v)
    #print("w:",w)
    while(w>=0):
        #print("loopfirst",loopfirst)
        if(w==loopfirst):
            #print("w==loopfirst^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            if(cntl==0):
                #print("create1********************")
                createloop()
            else:
                if(compare()==0):
                    #print("create2*********************")
                    createloop()
        if(visit[w]==0):
            #print("visit[w]=",visit[w],"该点未访问")
            DFS(w,visit)

        w=NextAdj(v,w)
        #print("w2:",w)
    cur-=1
    loopn-=1
    #print("cur:",cur,"loopn:",loopn)

def createloop():
    global cntl,cur
    l={}
    All[cntl]=allloop()
    All[cntl].pl={}
    All[cntl].cnt=loopn
    for i in range(cur):
        l[i]=loop[i]
    All[cntl].pl=l######
    #print("All:[",cntl,"]=",All[cntl].pl)
    #print("当前路径长度为",All[cntl].cnt)
    cntl+=1

def compare():
    n=0
    k=0
    i=0
    #print("cntl=",cntl)
    while(i<=(cntl-1)):
        #print("loopn=",loopn,"All[i].cnt=",All[i].cnt)
        if(loopn==All[i].cnt):
            k=incompare(All[i])
            if(k==0):
                n+=1
        else:
            n+=1
        i+=1
    #print("n=",n)
    if(n==cntl):
        #print("compare:n==cntl")
        return 0
    else:
        #print("compare:n!=cntl")
        return 1

def incompare(a):
    i=0
    j=0
    k=0
    while(i<a.cnt):
        if(loop[0]==a.pl[i]):
            break
        i+=1

    for j in range(cur):
        if(loop[j]==a.pl[(j+i)%(a.cnt)]):
            k+=1
        else:
            break
    if(k==a.cnt):
        #print("incompare:k==a.cnt")
        return 1
    else:
        #print("incompare:k!=a.cnt")
        return 0

def printloop():
    for i in range(cntl):
        print("第",i,"个环路为:")
        circle.append([])
        for j in range(len(All[i].pl)):
            print(list1[All[i].pl[j]],"-->",end='')
            circle[i].append(All[i].pl[j])
        print(list1[All[i].pl[0]])
        circle[i].append(All[i].pl[0])    
        print("环路长度:",All[i].cnt,"\n")

def order_by():
  for i in range(len(circle)):
    #进入每一个环查看是否第一个节点为最小值
    min_node=circle[i][0] #初始化
    location=-1#初始化
    for j in range(len(circle[i])):
      if (circle[i][j]<min_node):
        min_node=circle[i][j]
        location=j
        
    if(min_node<circle[i][0]):
      
      circle[i].pop()
      
      circle[i]=move_bit(circle[i],location)
      
      circle[i].append(circle[i][0])
      
  



def move_bit(lst, k):#循环左移（k>0）和右移（k<0）
    
    return lst[k:]+lst[:k]

def create_reference_table():
  for i in range(len(circle)):
    if(circle[i][0] not in reference_table):
      reference_table.append(circle[i][0])
  #reference_table.remove(0)


def auto_create_1(l):
    
    num1=None
    storage[l[0]]+=1
    if(l[0]<10):
      num1='_0'+str(l[0])
    else:
      num1='_'+str(l[0])
    if(storage[l[0]]<10):
      num2='_0'+ str(storage[l[0]])
    else:
      num2='_'+ str(storage[l[0]])
    name='Cy'+num1+num2
    base_circle[name]=l


def auto_create_final():
  for x in range(len(reference_table)-1,-1,-1):
    head=reference_table[x]#头，从大到小
    if(head!=0):
      for key,value in base_circle.items():#子环
        if(head==int(key[3:5])):#寻找子环
          find_father_circle(head,value)
      process_base_circle()    

def find_father_circle(match_head,son_circle):
  for key in base_circle.keys():
    #先判断是不是新增环
    if(len(key)<=8):
      for v in range(len(base_circle[key])):#对每一条环路遍历
        if(base_circle[key][v]==match_head):
          father_circle=base_circle[key]
          insert(key,match_head,father_circle,son_circle,v)

def insert(name,match_head,father,son,location):
  tem=0
  if(match_head<10):
    name=name+'_0'+str(match_head)+'_00'
  else:
    name=name+'_'+str(match_head)+'_00'
  while(name in base_circle_2.keys()):
    tem+=1
    if(tem<10):
      name=name[:-3]+'_0'+str(tem)
    else:
      name=name[:-3]+'_'+str(tem)
  #命名结束
  base_circle_2[name]=father[:location]+son+father[location+1:]

def process_base_circle():
  #更新base_circle
  base_circle.update(base_circle_2)
  #清空base_circle_2
  base_circle_2.clear()
      




def output_to_txt():
    counter=0
    with open("count_final.txt","w") as f:
        for key,value in final_circle.items():
          f.write(key)
          f.write("环路(")
          f.write(str(counter+1))
          f.write(")为：")
          for i in value:
            f.write(list1[i])
            f.write("-->")
          f.write("环结束!\n")
          counter+=1
    f.close()                
        


        



if __name__ == '__main__':
    Init()
    side=0
    visited={}
    circle=[]#所有环路
    while(side<len(edge)-1):
        i=edge[side]
        j=edge[side+1]
        CreateGraph(i,j)
        side+=2
    # for i in range(len(graph)):
    #     print("i",graph[i].index)
    #printlist()
    DFStraverse(visited)
    print("\n\n")
    printloop()
    print("原来的circle：",circle)
    order_by()
    print("\n\n")
    #print(circle)
    circle.sort(key=operator.itemgetter(0),reverse=False)#circle排序 
    #print(circle)

    base_circle={}
    base_circle_2={}
    final_circle={}
    storage={}
    reference_table=[]#存放circle第一位，无重复
    #初始化storage
    for i in range(cntl):
      storage[i]=0

    for i in range(len(circle)):
      auto_create_1(circle[i])
    print(base_circle)

    create_reference_table()
    print("reference_table",reference_table)
    #print(transform_key_into_num('Cy_58_00'))
    # print("\n\n\n")
    # for key,value in base_circle.items():
    #   print(key,"(首尾为",key[3:5],"的所有环):")
    #   for i in value:
    #     print(list1[i],"-->",end='')
    #   print("环结束!")
    num=0
    auto_create_final()
    for key,value in base_circle.items():
      if(value[0]==0):
        final_circle[key]=value
        print(key,end='')
        print(value)
        num+=1
      
    print(num)
    output_to_txt()

    



