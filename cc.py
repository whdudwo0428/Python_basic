"""import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
font = pygame.font.SysFont("Courier", 24)  # 모노스페이스 글꼴 설정
text = font.render("Hello, World!", True, (255, 255, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    screen.blit(text, (50, 100))
    pygame.display.flip()

pygame.quit()"""

print("별 찍기")
print("1.☆")
print("2.★")
print("3.#")
print("4.○")
print("5.●")

mode = int(input("모드를 선택하시오 :"))
len = int(input("길이를 입력하시오 :"))

if mode == 1:
    mode = "1.☆"
elif mode == 2:
    mode = "★"

elif mode == 3:
    mode = "#"
elif mode == 4:
    mode = "○"
elif mode == 5:
    mode = "●"

"""
match mode:
    case 1 | 2:
        #start
        
    case 3:
        #start
        

    case 4 | 5:
        #start
        """
#if mode ==1 or mode ==2:
#mod in [1,2]
for i in range(len):        # 1~len번째줄 / len+1줄
    if i == 0:
        print(" "*(len*3-(i+2)) + mode)
    else :
        print(" "*(len*3-(i+2)) + mode + "  "*(i-1) + mode + " "*(len*3-(i+1)))
    if i+1 == len:
        print(mode*(len+1) + "  "*(i) + mode*(len+1))
#for j in range():

for i in range(len):
    if i == 0:
        print(" " * (len * 3 - (i + 2)) + mode)
    else:
        print(" " * (len * 3 - (i + 2)) + mode + "  " * (i - 1) + mode + " " * (len * 3 - (i + 1)))
    if i + 1 == len:
        print(mode * (len + 1) + "  " * (i) + mode * (len + 1))



"""
☆☆☆☆☆
       ☆   7,☆
       
             ☆ 13,☆
            ☆☆   12,☆,0       
           ☆  ☆     11,☆,2
          ☆    ☆     10.☆.4 
         ☆      ☆        9.☆.6
☆☆☆☆☆☆        ☆☆☆☆☆☆    
       ☆                          7     # ☆2개
      ☆                            6    # ☆2개
☆
                            5
                            4
                            3
                            2
☆                            1
                            
1번 노란별
2번 빨간별
3번 파란별
4번 검은별


5번 노란o
6번 빨간o
            ☆ 12,☆
           ☆☆   11,☆,0       
          ☆  ☆     10,☆,2
         ☆    ☆     9.☆.4 
        ☆      ☆      8.☆.6
☆☆☆☆☆        ☆☆☆☆☆ ☆,8
   ☆    3
      ☆ 6
     ☆  5
    ☆   4
   ☆    3
  ☆     2
  
   
"""